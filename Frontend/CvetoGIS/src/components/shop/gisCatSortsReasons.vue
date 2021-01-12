<template>
  <section>
    <div class="row">
      <!--    Категории   -->
      <div class="col-12 col-md-4 section">
        <gis-sections-title title="Категории"/>
        <div class="row q-mt-md">
          <div
            v-for="(category, index) in categories"
            :key="index"
            class="col-6"
            style="padding: 2px"
          >
            <gis-category-card :category="category"/>
          </div>
        </div>
      </div>
      <!--    xxxxx   -->
      <!--    Поводы   -->
      <div class="col-12 col-md-4 section">
        <gis-sections-title title="Поводы"/>
        <div class="row q-mt-md">
          <div
            v-for="(reason, index) in reasons"
            :key="index"
            class="col-6" style="padding: 2px"
          >
            <gis-reason-card :reason="reason"/>
          </div>
        </div>
      </div>
      <!--    xxxxx   -->
      <!--    Цветы   -->
      <div class="col-12 col-md-4 section">
        <gis-sections-title title="Цветы"/>
        <div class="row q-mt-md">
          <div
            v-for="(sort, index) in sorts"
            :key="index"
            class="col-6" style="padding: 2px"
          >
            <gis-sort-card :sort="sort"/>
          </div>
        </div>
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
