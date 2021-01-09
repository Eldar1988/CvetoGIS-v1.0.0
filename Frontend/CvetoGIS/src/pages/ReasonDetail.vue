<template>
  <q-page>
    <!--  Заголовок страницы   -->
    <section>
      <gis-shop-page-title :title="reason.title" :description="reason.description" :icon-name="reason.icon"/>
    </section>
    <!--  xxxxx   -->
    <!--    Заглушка   -->
    <section v-if="products.length < 1">
      <gis-no-products-notice
        :text="`Извините, мы не нашли ничего подходящего ${reason.title.toLowerCase()} в вашем городе`"/>
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
    <!--    Категории - Поводы - Цветы-->
    <gis-cat-sorts-reasons class="q-mt-xl"/>
    <!--    xxxxx   -->
  </q-page>
</template>

<script>
import GisShopPageTitle from "components/headers/gisShopPageTitle";
import GisProductCard from "components/shop/gisProductCard";
import GisCatSortsReasons from "components/shop/gisCatSortsReasons";
import GisNoProductsNotice from "components/shop/gisNoProductsNotice";

export default {
  name: "ReasonDetail",
  components: {GisNoProductsNotice, GisCatSortsReasons, GisProductCard, GisShopPageTitle},
  data() {
    return {
      reason: {},
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
      data = await this.$axios.get(`${this.$store.getters.getServerURL}/reason_detail/${this.$route.params.slug}/${cityId}`)
        .then(({data}) => {
          return data
        })
      this.reason = data.reason
      this.products = data.products
    }
  }
}
</script>

<style lang="sass">

</style>
