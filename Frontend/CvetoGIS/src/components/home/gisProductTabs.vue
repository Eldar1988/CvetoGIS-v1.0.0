<template>
  <div>
    <div class="product-tabs">
      <div class="row q-mt-lg">
        <div class="col-6" style="padding: 2px">
          <q-btn
            label="Спецпредложения"
            @click="getSaleProducts"
            class="rounded full-width text-weight-bold q-py-sm"
            color="primary"
            stack
            icon="mdi-sale"
          />
        </div>
        <div class="col-6" style="padding: 2px">
          <q-btn
            label="Хиты продаж"
            @click="getFutureProducts"
            class="rounded full-width text-weight-bold q-py-sm"
            color="secondary"
            stack
            icon="mdi-fire"
          />
        </div>
<!--        <div-->
<!--          v-for="category in categories" :key="category.id"-->
<!--          :name="category.id"-->
<!--          class="col-6" style="padding: 2px"-->
<!--        >-->
<!--          <q-btn-->
<!--            :label="category.title"-->
<!--            @click="getProductsByCategory(category.slug)"-->
<!--            class="rounded full-width text-weight-bold q-py-sm"-->
<!--            text-color="white"-->
<!--            stack color="dark"-->
<!--            :style="`background-image: url('${category.miniauture}') !important`"-->
<!--          />-->
<!--        </div>-->
      </div>
    </div>

    <!--    Товары   -->
    <div class="products-wrapper q-mt-lg">
      <div class="row" v-if="newProducts.length < 1">
        <div
          v-for="product in products"
          :key="product.id"
          class="col-6 col-sm-4 col-lg-3 product-card-paddings"
        >
          <!--   Карточка товара   -->
          <gis-product-card :product="product"/>
          <!--          xxxxx   -->
        </div>
      </div>
      <div class="row" v-else>
        <div
          v-for="product in newProducts"
          :key="product.id"
          class="col-6 col-sm-4 col-lg-3"
          style="padding: 1px"
        >
          <!--          Карточка товара   -->
          <gis-product-card :product="product"/>
          <!--   xxxxx   -->
        </div>
      </div>
    </div>
    <!--   xxxxx   -->
  </div>
</template>

<script>
import GisProductCard from "components/shop/gisProductCard";

export default {
  name: "gisProductTabs",
  components: {GisProductCard},
  data() {
    return {
      tab: 'sale',
      newProducts: []
    }
  },
  computed: {
    categories() {
      return this.$store.getters.getHomeCategories
    },
    // Товары по умолчанию
    products: {
      get: function () {
        return this.$store.getters.getHomeProducts
      },
      set: function (products) {
        return this.products = products
      }
    }
  },
  mounted() {
    // При смене города обновляем товары со скидкой (по умолчанию) и устснавливаем таб по умолчанию
    this.$root.$on('changeCity', () => {
      let citySlug = JSON.parse(localStorage.getItem('city')).slug
      this.$store.dispatch('fetchHomeData', citySlug)
      this.tab = 'sale'
      this.getSaleProducts()
    })
  },
  methods: {
    // Загрузка избранных товаров (Хиты продаж)
    async getFutureProducts() {
      let citySlug = JSON.parse(localStorage.getItem('city')).slug
      this.newProducts = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/future_products/${citySlug}`)
        .then(({data}) => {
          return data
        })
      document.querySelector('.product-tabs').scrollIntoView({behavior: 'smooth', block: 'start'})
    },
    // Загрузка товаров со скидкой
    async getSaleProducts() {
      let citySlug = JSON.parse(localStorage.getItem('city')).slug
      this.newProducts = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/home_sale_products/${citySlug}`)
        .then(({data}) => {
          return data
        })
      document.querySelector('.product-tabs').scrollIntoView({behavior: 'smooth', block: 'start'})
    },
    // Загрузка товаров по категории
    async getProductsByCategory(categorySlug) {
      let citySlug = JSON.parse(localStorage.getItem('city')).slug
      this.newProducts = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/home_products_by_category/${citySlug}/${categorySlug}`)
        .then(({data}) => {
          return data
        })
      document.querySelector('.product-tabs').scrollIntoView({behavior: 'smooth', block: 'start'})
    }
  }
}
</script>

<style lang="sass">
.home-product-tab
  border-radius: 25px
  border: 1px solid $dark
  box-shadow: 2px 2px 5px 0 rgba(0, 0, 0, .1)
  transition: 1s all

  &:focus
    box-shadow: none

  .q-tab__indicator
    display: none !important

.product-card-image
  height: 400px
  object-fit: cover

.home-tab-header
  font-size: 14px
  line-height: 1
  font-weight: 700


</style>
