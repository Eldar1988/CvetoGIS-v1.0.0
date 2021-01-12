<template>
  <q-page>
    <section>
      <article>
        <div class="row" v-if="product">
          <div class="col-12 col-md-6" style="padding: 5px">
            <!--          Слайдер изображений товара   -->
            <gis-product-images-slider :image="product.image" :images="product.images" />
            <!--          xxxxx   -->
          </div>

          <div  class="col-12 col-md-6 q-pa-md">
            <!--          Заголовок   -->
            <h1 class="page-title">
              {{ product.title }}
            </h1>
            <!--          xxxxx   -->
            <!--          Цена   -->
            <p class="product-price text-primary">
              <q-icon name="payments"/>
              {{ getPrice(product.price) }}
              <q-icon size="30px" :name="priceIcon"/>
              <small class="product-old-price" v-if="product.old_price">{{ getPrice(product.old_price) }}</small>
            </p>
            <!--          xxxxx   -->
            <!--          Рейтинг    -->
            <p class="product-description text-weight-bold q-pt-sm">Рейтинг:
              <q-rating readonly max="5" style="margin-top: -3px" v-model="product.rating" size="24px" color="secondary"/>
            </p>
            <!--          xxxxx   -->
            <!--          Описание   -->
            <h2 class="product-description q-mt-md">{{ product.short_description }}</h2>
            <!--          xxxxx   -->
            <!--          Кнопки   -->
            <q-separator class="q-mt-lg" inset/>
            <div class="row q-mt-sm">
              <!--            Заказать сейчас   -->
              <div class="col-12 col-sm-6" style="padding: 3px">
                <q-btn
                  color="secondary"
                  class="full-width q-py-sm text-weight-bold rounded"
                  unelevated
                  @click="addToCart(product, 1, false)"
                >
                  Заказать сейчас
                  <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
                    Заказ в один клик
                  </q-tooltip>
                </q-btn>
              </div>
              <!--            В корзину   -->
              <div class="col-12 col-sm-6" style="padding: 3px">
                <q-btn
                  color="primary"
                  icon="mdi-cart-arrow-down"
                  @click="addToCart(product, 1, true)"
                  class="full-width text-weight-bold q-py-sm rounded"
                  outline
                >
                  В корзину
                  <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
                    Добавить в корзину
                  </q-tooltip>
                </q-btn>
              </div>
            </div>
            <q-separator class="q-mt-sm" inset/>
            <!--          xxxxx   -->
            <!--          Доставка   -->
            <h3 class="product-description text-weight-bold q-mt-lg">
              Доставка в городах:
              <span v-if="product.cities" class="text-weight-regular">{{ product.cities.join(', ') }}</span>
            </h3>
            <!--          xxxxx   -->
            <!--          Поводы   -->
            <h3 v-if="product.reasons" class="product-description text-weight-bold q-mt-sm">
              Подходящие поводы:<br>
              <q-btn
                v-for="(reason, index) in product.reasons" :key="index"
                size="sm"
                :label="reason.title"
                rounded outline
                color="secondary"
                class="q-mr-sm text-weight-bold q-mt-sm"
                :to="`/reason/${reason.slug}`"
              />
            </h3>
            <!--          xxxxx   -->
            <!--          Продавец   -->
            <div
              v-if="product.seller"
              class="product-description text-weight-bold q-mt-md"
            >
              Продавец:
              <q-btn
                :label="product.seller.title"
                rounded outline flat
                color="dark"
                icon-right="emoji_nature"
                class="q-mr-sm text-weight-bold"
              />
            </div>
            <!--          xxxxx   -->
<!--            Дополнительная информация   -->
            <div v-if="product.description" v-html="product.description" class="rounded q-mt-md" style="border: 1px solid #efefef; padding: 5px"></div>
          </div>
        </div>
      </article>
    </section>

    <!--      Игрушки   -->
    <section class="section" v-if="!product.suggest">
      <gis-sections-title title="Вместе с этим товаром покупают"/>
      <div class="q-mt-lg">
        <!--    Scroll controls   -->
        <div class="scroll-controls text-center hide-on-mobile">
          <q-btn
            @click="scrollLeft"
            icon="navigate_before"
            round
            color="primary"
          />
          <q-btn
            @click="scrollRight"
            icon="navigate_next"
            round
            color="primary"
            class="q-ml-sm"
          />
        </div>
        <!--    ==============   -->
        <!--    Scroll Area   -->
        <q-scroll-area
          ref="scrollFutureProducts"
          horizontal
          class="full-width q-mt-md"
          style="height: 470px; width: 100%"
          :thumb-style="{ display: 'none' }"
        >
          <div class="row no-wrap">
            <div
              v-for="(toy, index) in toys" :key="index"
              class="product-wrapper"
              style="width: 300px; padding: 0 4px"
            >
              <gis-toys-product-card :product="toy"/>
            </div>
          </div>
        </q-scroll-area>
        <!--    ============   -->
      </div>
    </section>
    <!--      xxxxx   -->

    <!--      Дополнительные товары   -->
    <section class="section" v-if="product.category">
      <gis-sections-title :title="`Другие ${product.category.title.toLowerCase()}`"/>
      <div class="products-wrapper q-mt-md">
        <div class="row">
          <div
            v-for="(product, index) in products"
            :key="index"
            class="col-6 col-sm-4 col-lg-3 product-card-paddings"
          >
            <!--          Карточка товара   -->
            <gis-product-card :product="product"/>
            <!--   xxxxx   -->
          </div>
        </div>
      </div>
    </section>
    <!--      xxxxx   -->

  </q-page>
</template>

<script>
import GisProductImagesSlider from "components/product/gisProductImagesSlider";
import GisSectionsTitle from "components/headers/gisSectionsTitle";
import GisToysProductCard from "components/shop/gisToysProductCard";
import GisProductCard from "components/shop/gisProductCard";

export default {
  name: "ProductDetail",
  components: {GisProductCard, GisToysProductCard, GisSectionsTitle, GisProductImagesSlider},
  data() {
    return {
      toys: [],
      products: [],
      product: {},
      position: 0,
      productId: null
    }
  },
  computed: {
    // Иконка валюты
    priceIcon() {
      return this.$store.getters.getCurrentCurrency.icon
    },
  },
  watch: {
    '$route'() {
      this.loadData()
    }
  },
  mounted() {
    this.loadData()
  },
  // preFetch({store, currentRoute}) {
  //   return store.dispatch('fetchProduct', currentRoute.params.slug)
  // },
  methods: {
    // Товар
    async loadData() {
      await this.loadProduct()
      await this.loadAdditionalProducts()
    },
    async loadProduct() {
      this.product = await this.$axios.get(`${this.$store.getters.getServerURL}/product/${this.$route.params.slug}/`)
        .then(({data}) => {
          this.productId = data.product.id
          return data.product
        })
    },
    // Дополнительные товары
    async loadAdditionalProducts() {
      let cityID = JSON.parse(localStorage.getItem('city')).id
      console.log(`${this.$store.getters.getServerURL}/additional_products/${cityID}/${this.product.id}/`)
      let products = {}

      products = await this.$axios.get(`${this.$store.getters.getServerURL}/additional_products/${cityID}/${this.product.category.id}/`)
        .then(({data}) => {
          return data
        })
      this.toys = products.toys
      this.products = products.products
    },
    // Получаем цену (форматированная и в валюте)
    getPrice(price) {
      let course = this.$store.getters.getCurrentCurrency.value
      let newPrice = price / parseInt(course)
      newPrice = Math.ceil(newPrice)
      newPrice = newPrice.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
      return newPrice
    },
    // Добавление товара в корзину
    async addToCart(product, quantity, showCart) {
      product.quantity = quantity
      let productInCart = false
      let cart = [] // Создаем новую корзину (на случай, если у пользователя еще нет корзины)
      // Проверяем если добавляемый товар в существующей корзине
      if (localStorage.getItem('cart') !== null) {
        cart = JSON.parse(localStorage.cart) // Получаем существующую корзину и перезаписываем текущую корзину
        cart.forEach((item) => {
          // Если добавляемый товар уже есть в корзине - увеличиваем его количество на 1
          if (item.id === product.id) {
            item.quantity++
            productInCart = true
          }
        })
      }
      // Если добавляемого товара нет в корзине - добавляем его
      if (!productInCart) {
        cart.push(product)
      }
      // Записываем обновленную корзину в localStorage
      localStorage.setItem('cart', JSON.stringify(cart))
      if (showCart) {
        this.$root.$emit('addToCartDialog') // Вызываем окно корзины
        localStorage.setItem('addedProduct', product.title)
      }
      if (!showCart) {
        this.addToCardSuccessDialog = true // Показываем диалаоговое окно
        await this.$router.push('/cart')
      }
      this.$root.$emit('updateCart')

    },
    // Скролл вправо
    scrollRight() {
      // Проверка: количество карточек * ширину экрана (98% ширина контейнера)
      if (this.position < this.toys.length * 300 - (window.innerWidth * 0.98)) {
        this.position += 300
        this.$refs.scrollFutureProducts.setScrollPosition(this.position, 500)
      }
    },
    // Левый скролл
    scrollLeft() {
      if (this.position !== 0) {
        this.position = this.position - 300
        this.$refs.scrollFutureProducts.setScrollPosition(this.position, 500)
      }
    }
  }
}
</script>

<style lang="sass">
.product-title
  font-size: 30px
  line-height: 1.2
  font-weight: 700

.product-price
  font-size: 46px
  font-weight: 700

.product-old-price
  font-size: 26px
  text-decoration: line-through
  color: grey
  margin-left: 10px
  display: inline-block

.product-description
  font-size: 14px
  line-height: 1.5

@media screen and (max-width: 650px)
  .product-title
    font-size: 22px
</style>
