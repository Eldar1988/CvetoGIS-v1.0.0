<template>
  <article>
    <q-card class="my-card shadow-lt rounded">
      <router-link :to="`/product/${product.slug}`">
        <q-img
          :src="product.image"
          class="product-card-image"
          spinner-color="secondary"
          style="max-width: 100%"
          @click="goToProductDetail(product.slug)"
          height="400px"
        >
          <template v-slot:loading class="full-width">
              <q-skeleton height="400px" class="full-width" />
          </template>

          <!--      Рейтинг товара  -->
          <q-rating
            readonly v-model="product.rating"
            :max="5"
            size="32px"
            icon="mdi-star"
            icon-half="mdi-star-outline"
            class="product-card-rating"
            color="amber"
            :title="`Рейтинг: ${product.rating} из 5`"
          >
          </q-rating>
          <!--      ================   -->
          <!--      Процент скидки   -->
          <q-btn
            v-if="product.old_price"
            color="secondary" rounded
            style="top: 55px; left: 15px; opacity: .8; z-index: 15"
            unelevated
          >
            {{ getSalePercent }}
            <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
              Скидка {{ getSalePercent }}
            </q-tooltip>
          </q-btn>
          <!--      ====================   -->

          <!--      Сорта и поводы   -->
          <div class="product-card-reasons text-center">
            <q-btn
              v-for="sort in product.sort" :key="sort"
              color="accent" text-color="dark"
              no-caps rounded
              size="sm"
              class="reasons-btn" unelevated
            >{{ sort }}
              <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
                Сорт
              </q-tooltip>
            </q-btn>
            <q-btn
              v-for="reason in product.reasons" :key="reason"
              color="accent" text-color="dark"
              no-caps rounded
              size="sm"
              class="reasons-btn" unelevated
            >{{ reason }}
              <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
                Подходящий повод
              </q-tooltip>
            </q-btn>
          </div>
        </q-img>
      </router-link>
      <q-card-section class="q-pb-none">
        <div class="items-center">
          <!--        Название товара   -->
          <router-link :to="`/product/${product.slug}`">
            <h4 class="col text-h6 ellipsis text-center text-weight-bold">
              {{ product.title }}
              <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[0, 0]">
                Подробнее
              </q-tooltip>
            </h4>
          </router-link>
          <!--        =======================   -->
          <!--        Цена товара   -->
          <p class="text-h6 text-primary relative-position text-center q-pt-sm text-weight-bold">
            {{ getPrice(product.price) }}
            <q-icon :name="priceIcon" color="primary" size="16px"/>
            <span class="old-price" v-if="product.old_price">{{ getPrice(product.old_price) }}
          </span>
            <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, -60]">
              Цена
            </q-tooltip>
          </p>
          <!--        ======================    -->
        </div>
      </q-card-section>

      <!--    Заказ в один клик   -->
      <q-card-actions>
        <div class="row full-width">

          <div class="col-10 text-center">
            <q-btn
              color="secondary"
              class="full-width shadow-lt q-mt-sm text-weight-bold q-py-sm"
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

          <div class="col-2 text-right">
            <!--      Кнопка в корзину   -->
            <q-btn
              round
              color="primary"
              icon="mdi-cart-arrow-down"
              glossy
              size="17px"
              @click="addToCart(product, 1, true)"
              class="q-mt-sm"
            >
              <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
                Добавить в корзину
              </q-tooltip>
            </q-btn>
          </div>
        </div>
        <!--      ==============   -->
      </q-card-actions>
      <!--    =======================    -->
    </q-card>
  </article>
</template>

<script>
export default {
  name: "gisProductCard",
  props: {
    product: {
      type: Object,
      default: null,
      addToCardSuccessDialog: false
    }
  },
  computed: {
    // Иконка валюты
    priceIcon() {
      return this.$store.getters.getCurrentCurrency.icon
    },
    // Получаем процент скидки
    getSalePercent: function () {
      let percent = Math.round(100 - (this.product.price * 100 / this.product.old_price))
      return `-${percent}%`
    }
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
    },
    goToProductDetail(slug) {
      this.$router.push(`/product/${slug}`)
    }
    // ==================================================================
    // Показываем корзину
  }
}
</script>

<style lang="sass">
.product-card-image
  position: relative

  &:after
    content: ""
    position: absolute
    left: 0
    top: 0
    bottom: 0
    right: 0
    background: linear-gradient(180deg, rgba(0, 0, 0, 0) 70%, #fff 100%)
    z-index: 0

.product-card-rating
  position: absolute
  z-index: 15

.old-price
  font-size: 16px
  text-decoration: line-through
  color: grey
  margin-left: 10px
  top: -15px
  display: inline-block

.product-card-reasons
  z-index: 15
  bottom: -15px

.reasons-btn
  margin: 5px
</style>
