<template>
  <q-page>
    <!--  Заголовок страницы   -->
    <section>
      <gis-page-image-title :obj="sort"/>
    </section>
    <!--  xxxxx   -->
    <!--    Заглушка  -->
    <section v-if="products.length < 1">
      <gis-no-products-notice :text="`Извините, в вашем городе закончились ${sort.title.toLowerCase()}`"/>
    </section>
    <!--    xxxxx   -->
    <!--    Товары   -->
    <section>
      <div class="products-wrapper q-mt-lg">
        <div class="row">
          <div
            v-for="product in products"
            :key="product.id"
            class="col-12 col-sm-6 col-lg-4 q-pa-sm"
          >
            <!--          Карточка товара   -->
            <gis-product-card :product="product"/>
            <!--   xxxxx   -->
          </div>
        </div>
      </div>
    </section>
    <!--   xxxxx   -->
    <gis-cat-sorts-reasons class="q-mt-xl"/>

  </q-page>
</template>

<script>
import GisProductCard from "components/shop/gisProductCard";
import GisPageImageTitle from "components/headers/gisPageImageTitle";
import GisNoProductsNotice from "components/shop/gisNoProductsNotice";
import GisCatSortsReasons from "components/shop/gisCatSortsReasons";

export default {
  name: "SortDetail",
  components: {GisCatSortsReasons, GisNoProductsNotice, GisPageImageTitle, GisProductCard},
  data() {
    return {
      sort: {},
      products: []
    }
  },
  created() {
    this.loadData()
  },
  watch: {
    '$route'() {
      this.loadData()
    }
  },
  methods: {
    async loadData() {
      let cityId = JSON.parse(localStorage.getItem('city')).id
      let data = {}
      data = await this.$axios.get(`${this.$store.getters.getServerURL}/sort_detail/${this.$route.params.slug}/${cityId}`)
        .then(({data}) => {
          return data
        })
      this.sort = data.sort
      this.products = data.products
    }
  }
}
</script>

<style scoped>

</style>
