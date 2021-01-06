<template>
  <div>
    <!--    Табы   -->
    <div class="home-tabs q-mt-lg q-mb-lg">
      <q-tabs
        v-model="tab"
        inline-label
        class="" active-bg-color="dark" active-color="white"
      >
        <q-tab
          class="home-product-tab q-ma-sm"
          name="sale" icon="mdi-sale"
          @click="getSaleProducts"
        >
          <h3 class="home-tab-header q-ml-sm">Спецпредложения</h3>
        </q-tab>
        <q-tab
          class="home-product-tab q-ma-sm"
          name="alarms"
          icon="mdi-fire"
          @click="getFutureProducts"
        >
          <h3 class="home-tab-header q-ml-sm">Хиты продаж</h3>
        </q-tab>
        <q-tab
          v-for="category in categories" :key="category.id"
          :name="category.id"
          class="home-product-tab q-ma-sm"
          @click="getProductsByCategory(category.slug)"
          style="padding: 0 !important;"
        >
          <h3 class="home-tab-header q-ml-sm q-pr-lg" style="margin-left: 5px">
            <q-avatar size="39px">
              <q-img :src="category.miniature" style="min-height: 100%"/>
            </q-avatar>
            <span class="q-ml-sm">
              {{ category.title }}
            </span>
          </h3>
        </q-tab>
      </q-tabs>
    </div>
    <!--    =======================   -->
    <!--    Товары   -->
    <div class="products-wrapper">
      <div class="products-grid" v-if="newProducts.length < 1">
        <div
          v-for="product in products" :key="product.id"
          class="col-12 col-sm-6 col-md-4 col-lg-3">
          <!--   Карточка товара   -->
          <gis-product-card :product="product"/>
          <!--          xxxxx   -->
        </div>
      </div>
      <div class="products-grid" v-else>
        <div
          v-for="product in newProducts" :key="product.id"
          class="col-12 col-sm-6 col-md-4 col-lg-3">
          <!--          Карточка товара   -->
          <gis-product-card :product="product"/>
          <!--   xxxxx   -->
        </div>
      </div>
    </div>
    <!--    ========================   -->
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
    },
    // Загрузка товаров со скидкой
    async getSaleProducts() {
      let citySlug = JSON.parse(localStorage.getItem('city')).slug
      this.newProducts = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/home_sale_products/${citySlug}`)
        .then(({data}) => {
          return data
        })
    },
    // Загрузка товаров по категории
    async getProductsByCategory(categorySlug) {
      let citySlug = JSON.parse(localStorage.getItem('city')).slug
      this.newProducts = await this.$axios.get(`${this.$store.getters.getServerURL}/shop/home_products_by_category/${citySlug}/${categorySlug}`)
        .then(({data}) => {
          console.log('data', data)
          return data
        })
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
