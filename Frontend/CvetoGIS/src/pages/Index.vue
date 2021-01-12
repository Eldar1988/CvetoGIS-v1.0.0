<template>
  <q-page>
    <!--    Заголовок страницы   -->
    <gis-page-title :title="title"/>
    <!--    xxxxx   -->
    <!--    Слайдер   -->
    <gis-home-slider class="q-mt-sm"/>
    <!--    xxxxx   -->
    <!--    Табы с товарами   -->
    <gis-product-tabs/>
    <!--    xxxxx   -->
    <!--    Категории - Поводы - Цветы -->
    <gis-cat-sorts-reasons class="q-mt-lg"/>
    <!--    xxxxx   -->
    <!--    Отзывы   -->
    <gis-testimonials class="section q-pt-md"/>
    <!--    xxxxx   -->
  </q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";
import GisHomeSlider from "components/home/gisHomeSlider";
import GisProductTabs from "components/home/gisProductTabs";
import GisCatSortsReasons from "components/shop/gisCatSortsReasons";
import GisTestimonials from "components/home/gisTestimonials";

export default {
  name: 'PageIndex',
  components: {GisTestimonials, GisCatSortsReasons, GisProductTabs, GisHomeSlider, GisPageTitle},
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchHomeData', currentRoute.params.slug)
  },
  computed: {
    title() {
      return this.$store.getters.getHomeInfo.site_title
    }
  }
}
</script>

