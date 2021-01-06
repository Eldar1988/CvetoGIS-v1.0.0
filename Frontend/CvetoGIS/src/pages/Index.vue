<template>
  <q-page>
    <!--    Заголовок страницы   -->
    <gis-page-title :title="title"/>
    <!--    xxxxx   -->
    <!--    Слайдер   -->
    <gis-home-slider class="q-mt-md"/>
    <!--    xxxxx   -->
    <!--    Табы с товарами   -->
    <gis-product-tabs/>
    <!--    xxxxx   -->
  </q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";
import GisHomeSlider from "components/home/gisHomeSlider";
import GisProductTabs from "components/home/gisProductTabs";

export default {
  name: 'PageIndex',
  components: {GisProductTabs, GisHomeSlider, GisPageTitle},
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

