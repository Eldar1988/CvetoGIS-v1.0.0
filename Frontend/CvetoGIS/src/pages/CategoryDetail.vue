<template>
  <q-page>
    <!--  Заголовок страницы   -->
    <section style="padding: 5px">
      <gis-page-image-title :obj="category"/>
    </section>
    <!--  xxxxx   -->
    <!--  Заглушка   -->
    <section v-if="products.length < 1">
      <gis-no-products-notice :text="`Извините, в вашем городе закончились '${category.title}'`"/>
    </section>
    <!--  xxxxx   -->
    <!--    Товары   -->
    <section>
      <div class="products-wrapper q-mt-lg">
        <div class="row">
          <div
            v-for="product in products"
            :key="product.id"
            class="col-6 col-sm-4 col-lg-3 product-card-paddings"
          >
            <!--          Карточка товара   -->
            <gis-product-card :product="product"/>
            <!--   xxxxx   -->
          </div>
        </div>
      </div>
    </section>
    <!--   xxxxx   -->
    <gis-cat-sorts-reasons class="q-mt-xl" />
  </q-page>
</template>

<script>
import GisProductCard from "components/shop/gisProductCard";
import GisPageImageTitle from "components/headers/gisPageImageTitle";
import GisNoProductsNotice from "components/shop/gisNoProductsNotice";
import GisCatSortsReasons from "components/shop/gisCatSortsReasons";

export default {
  name: "CategoryDetail",
  components: {GisCatSortsReasons, GisNoProductsNotice, GisPageImageTitle, GisProductCard},
  data() {
    return {
      category: {},
      products: []
    }
  },
  mounted() {
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
      data = await this.$axios.get(`${this.$store.getters.getServerURL}/category_detail/${this.$route.params.slug}/${cityId}`)
        .then(({data}) => {
          return data
        })
      this.category = data.category
      this.products = data.products
    }
  }

}
</script>

<style scoped>

</style>
