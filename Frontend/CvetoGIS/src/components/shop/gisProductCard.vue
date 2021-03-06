<template>
  <article>
    <q-card class="product-card shadow-0 rounded">
      <router-link :to="`/product/${product.slug}`">
        <q-img
          :src="product.image"
          class="product-card-image"
          spinner-color="secondary"
          style="max-width: 100%"
          @click="goToProductDetail(product.slug)"
        >
          <template v-slot:loading class="full-width">
              <q-skeleton class="full-width product-card-image" />
          </template>

          <!--      Рейтинг товара  -->
          <q-rating
            readonly v-model="product.rating"
            :max="5"
            size="22px"
            icon="mdi-star"
            icon-half="mdi-star-outline"
            class="product-card-rating"
            color="amber"
            :title="`Рейтинг: ${product.rating} из 5`"
          >
          </q-rating>
          <!--   xxxxx   -->
          <!--      Процент скидки   -->
          <q-btn
            v-if="product.old_price"
            color="secondary" round
            style="position: absolute; bottom: 10px; right: 10px; opacity: .8; z-index: 15"
            unelevated
            size="sm"
            class="text-weight-bold"
          >
            {{ getSalePercent }}
            <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
              Скидка {{ getSalePercent }}
            </q-tooltip>
          </q-btn>
          <!--   xxxxx   -->
        </q-img>
      </router-link>
      <q-card-section class="q-pb-none">
        <div class="items-center">
          <!--        Название товара   -->
          <router-link :to="`/product/${product.slug}`">
            <h4 class="col ellipsis text-center text-weight-bold product-card-title">
              {{ product.title }}
              <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[0, 0]">
                Подробнее
              </q-tooltip>
            </h4>
          </router-link>
          <!--   xxxxx   -->
          <!--        Цена товара   -->
          <p class="text-primary relative-position text-center text-weight-bold product-card-price">
            {{ getPrice(product.price) }}
            <q-icon :name="priceIcon" color="primary" size="18px" style="margin-top: -3px; margin-left: -7px"/>
            <span class="old-price" v-if="product.old_price">{{ getPrice(product.old_price) }}
          </span>
            <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, -60]">
              Цена
            </q-tooltip>
          </p>
          <!--   xxxxx   -->
        </div>
      </q-card-section>

      <!--    Заказ в один клик   -->
      <q-card-actions style="padding: 2px">
        <div class="row full-width">

          <div class="col-9 text-center" style="padding: 2px">
            <q-btn
              color="secondary"
              class="full-width shadow-lt rounded card-action-btn text-weight-bold"
              unelevated
              @click="addToCart(product, 1, false)"
            >
              Заказать сейчас
              <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
                Заказ в один клик
              </q-tooltip>
            </q-btn>
          </div>

          <div class="col-3 text-right" style="padding: 2px">
            <!--      Кнопка в корзину   -->
            <q-btn
              color="primary"
              icon="mdi-cart-arrow-down"
              outline
              @click="addToCart(product, 1, true)"
              class="full-width rounded card-action-btn"
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

      this.$root.$emit('updateCart')
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

</style>
