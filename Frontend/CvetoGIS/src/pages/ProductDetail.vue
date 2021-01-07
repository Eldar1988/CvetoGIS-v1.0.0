<template>
  <q-page>
    <article>
      <div class="row">
        <div class="col-12 col-md-6">
          <!--          Слайдер изображений товара   -->
          <gis-product-images-slider :image="product.image" :images="product.images"/>
          <!--          xxxxx   -->
          <!--          Категория   -->
          <q-img
            :src="product.category.miniature"
            no-default-spinner
            class="img-overlay-2 rounded shadow-lt q-mt-md"
            height="50px"
          >
            <div class="image-text-bottom text-dark text-weight-bold text-uppercase q-mb-sm">
              {{ product.category.title }}
            </div>
          </q-img>
          <!--          xxxxx   -->
        </div>

        <div class="col-12 col-md-6 q-pa-md">
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
            <q-rating max="5" style="margin-top: -3px" v-model="product.rating" size="24px" color="secondary"/>
          </p>
          <!--          xxxxx   -->
          <!--          Описание   -->
          <h2 class="product-description q-mt-md">{{ product.short_description }}</h2>
          <!--          xxxxx   -->
<!--          Кнопки   -->
          <q-separator class="q-mt-lg" inset />
          <div class="row q-mt-sm">
<!--            Заказать сейчас   -->
            <div class="col-12 col-sm-6 q-pa-sm">
              <q-btn
                color="secondary"
                class="full-width shadow-lt text-weight-bold q-py-sm"
                rounded unelevated
                @click="addToCart(product, 1, false)"
              >
                Заказать сейчас
                <q-icon name="forward" class="q-ml-sm"/>
                <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
                  Заказ в один клик
                </q-tooltip>
              </q-btn>
            </div>
<!--            В корзину   -->
            <div class="col-12 col-sm-6 q-pa-sm">
              <q-btn
                color="primary"
                icon="mdi-cart-arrow-down"
                @click="addToCart(product, 1, true)"
                class="full-width text-weight-bold q-py-sm"
                rounded outline
              >
                Добавить в корзину
                <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
                  Добавить в корзину
                </q-tooltip>
              </q-btn>
            </div>
          </div>
          <q-separator class="q-mt-sm" inset />
<!--          xxxxx   -->
          <!--          Доставка   -->
          <h3 class="product-description text-weight-bold q-mt-lg">
            Доставка в городах:
            <span class="text-weight-regular">{{ product.cities.join(', ') }}</span>
          </h3>
          <!--          xxxxx   -->
          <!--          Состав   -->
          <h3 class="product-description text-weight-bold q-mt-sm">
            Состав:
            <span class="text-weight-regular">{{ product.sort.join(', ') }}</span>
          </h3>
          <!--          xxxxx   -->
          <!--          Поводы   -->
          <h3 class="product-description text-weight-bold q-mt-sm">
            Подходящие поводы:<br>
            <q-btn
              v-for="reason in product.reasons" :key="reason"
              size="sm" :label="reason"
              rounded outline
              color="secondary"
              class="q-mr-sm text-weight-bold q-mt-sm"
            />
          </h3>
          <!--          xxxxx   -->

        </div>
      </div>
    </article>
  </q-page>
</template>

<script>
import GisProductImagesSlider from "components/product/gisProductImagesSlider";

export default {
  name: "ProductDetail",
  components: {GisProductImagesSlider},
  data() {
    return {}
  },
  computed: {
    product() {
      return this.$store.getters.getProduct
    },
    // Иконка валюты
    priceIcon() {
      return this.$store.getters.getCurrentCurrency.icon
    },
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchProduct', currentRoute.params.slug)
  },
  methods: {
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
  font-size: 16px
  line-height: 1.5

@media screen and (max-width: 650px)
  .product-title
    font-size: 22px
</style>
