<template>
<q-page style="padding: 5px">
  <div >
      <gis-page-title title="Ваша корзина" />
      <!--      Товары в корзине  -->
      <div v-if="cart.length > 0">
        <p class="q-pt-lg product-card-price text-weight-bold">Количество товаров: {{ cart.length }}</p>

        <!--        Товары в корзине  -->
        <div class="products-grid q-mt-lg">
          <div class="col-12 col-sm-6 -col-md-6 col-lg-4" v-for="product in cart" :key="product.id">
            <gis-cart-item :product="product"/>
          </div>
        </div>
        <!--        ===================  -->
        <p class="q-pt-lg product-card-price text-weight-bold">
          Общая сумма: {{ getPrice(cartSum) }}
          <q-icon :name="priceIcon" size="18px" style="margin-left: -5px; margin-top: -3px"/>
        </p>
      </div>
      <!--      =====================    -->
      <!--      Заглушка, если нет товаров   -->
      <div v-if="cart.length === 0">
        <q-card class="bg-secondary q-pa-xl rounded shadow-lt q-mt-lg">
          <q-card-section class="text-center">
            <h2 class="text-h6 text-white text-center">В вашей корзине пока нет товаров.</h2>
            <q-btn rounded outline color="white" class="q-px-md q-mt-md text-weight-bold" @click="goToHome">Вернуться в магазин</q-btn>
          </q-card-section>
        </q-card>
      </div>
      <!--      =========================   -->
    </div>

    <!--    Оформление заказа   -->
    <div v-if="cart.length > 0">
      <gis-page-title class="q-mt-xl" title="Оформление заказа"/>
      <gis-checkout-form :sum="cartSum"/>
    </div>
</q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";
import GisCartItem from "components/shop/gisCartItem";
import GisCheckoutForm from "components/shop/gisCheckoutForm";
export default {
  name: "Cart",
  components: {GisCheckoutForm, GisCartItem, GisPageTitle},
  data() {
    return {
      cart: [],
      cartLen: 0,
      cartSum: 0
    }
  },
  computed: {
    // Иконка валюты
    priceIcon() {
      return this.$store.getters.getCurrentCurrency.icon
    },
  },
  mounted() {
    // Проверяем: если у клиента есть корзина то получаем ее и записываем в cart компонента
    if (localStorage.getItem('cart') !== null) {
      this.cart = JSON.parse(localStorage.cart)
      this.cartLen = this.cart.length // присваеваем количество товаров в корзине в элементе
      let cartSum = 0 // Сумма тенге в корзине
      this.cart.forEach((item) => {
        let itemSum = parseInt(item.price) * item.quantity // получаем сумму каждого товара в корзине
        cartSum += itemSum // Прибавляем к общей сумме товаров в корзине
      })
      this.cartSum = cartSum

    }
    this.$root.$on('updateCart', () => {
      this.cart = JSON.parse(localStorage.getItem('cart'))
      let cartSum = 0 // Сумма тенге в корзине
      this.cart.forEach((item) => {
        let itemSum = parseInt(item.price) * item.quantity // получаем сумму каждого товара в корзине
        cartSum += itemSum // Прибавляем к общей сумме товаров в корзине
      })
      this.cartSum = cartSum

    })
  },
  methods: {
    // Получаем цену (форматированная и в валюте)
    getPrice(price) {
      let course = this.$store.getters.getCurrentCurrency.value
      let newPrice = parseInt(price) / parseInt(course)
      newPrice = Math.ceil(newPrice)
      newPrice = newPrice.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
      return newPrice
    },
    // Переход на главную страницу
    goToHome() {
      let city = JSON.parse(localStorage.getItem('city'))
      if (city.slug === 'karaganda') {
        this.$store.dispatch('fetchHomeData', city.slug)
        this.$router.push(`/`)
      } else {
        this.$router.push(`/city/${city.slug}`)
      }
    }
  },
}
</script>

<style scoped>

</style>
