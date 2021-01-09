<template>
  <article>
    <q-card
      class="rounded shadow-lt"
    >
      <q-img
        :src="product.image"
        height="300px"
        class="product-card-image"
      >
        <template v-slot:loading class="full-width">
          <q-skeleton height="300px" class="full-width"/>
        </template>

        <q-btn
          icon="search"
          color="primary"
          round
          style="position: absolute; right: 8px; top: 8px; z-index: 25"
          @click="goToProductDetail(product.slug)"
        />
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
        <!--      ================   -->
      </q-img>
      <div class="toy-info" style="padding: 5px">
        <h5 class="text-h6 text-weight-bold ellipsis text-center">
          {{ product.title }}
        </h5>
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
        <!--        Добавить в корзину   -->
        <q-card-actions>
          <q-btn
            rounded
            color="secondary"
            icon="mdi-cart-arrow-down"
            size="md"
            @click="addToCart(product, 1, true)"
            class="q-mt-sm full-width text-weight-bold"
            label="Добавить в корзину"
            unelevated
          >
            <q-tooltip content-class="bg-primary" content-style="font-size: 14px" :offset="[10, 10]">
              Добавить в корзину
            </q-tooltip>
          </q-btn>
        </q-card-actions>


      </div>
      <!--        xxxxx    -->
    </q-card>
  </article>
</template>

<script>
export default {
  name: "gisToysProductCard",
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

<style scoped>

</style>
