<template>
  <section>
    <div class="row">
      <!--    Категории   -->
      <div class="col-12 col-md-4 q-pa-sm section">
        <gis-sections-title title="Категории"/>
        <gis-category-card
          class="q-mt-md "
          v-for="(category, index) in categories"
          :key="index"
          :category="category"/>
      </div>
      <!--    xxxxx   -->
      <!--    Поводы   -->
      <div class="col-12 col-md-4 q-pa-sm section">
        <gis-sections-title title="Поводы"/>
        <gis-reason-card
          class="q-mt-md "
          v-for="(reason, index) in reasons"
          :key="index"
          :reason="reason"
        />
      </div>
      <!--    xxxxx   -->
      <!--    Цветы   -->
      <div class="col-12 col-md-4 q-pa-sm section">
        <gis-sections-title title="Цветы"/>
        <gis-sort-card
          class="q-mt-md "
          v-for="(sort, index) in sorts"
          :key="index"
          :sort="sort"
        />
      </div>
      <!--    xxxxx   -->
    </div>
  </section>
</template>

<script>
import GisCategoryCard from "components/shop/gisCategoryCard";
import GisSectionsTitle from "components/headers/gisSectionsTitle";
import GisReasonCard from "components/shop/gisReasonCard";
import GisSortCard from "components/shop/gisSortCard";

export default {
  name: "gisCatSortsReasons",
  components: {GisSortCard, GisReasonCard, GisSectionsTitle, GisCategoryCard},
  computed: {
    categories() {
      return this.$store.getters.getCategories
    },
    reasons() {
      return this.$store.getters.getReasons
    },
    sorts() {
      return this.$store.getters.getSorts
    }
  },
}
</script>

<style>

</style>
