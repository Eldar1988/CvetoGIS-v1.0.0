<template>
  <q-page>
    <article>
      <gis-page-title :title="about.title"/>
      <div class="q-mt-xl" v-html="about.info"></div>
      <div class="about-logo text-center">
        <q-img :src="about.logo" width="300px" class="q-my-lg"/>
      </div>
      <gis-sections-title class="q-mt-xl" title="Наши реквизиты:" />
      <div
        v-html="about.requisite"
        style="max-width: 500px; margin: 25px auto"
      ></div>
    </article>
  </q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";
import GisSectionsTitle from "components/headers/gisSectionsTitle";

export default {
  name: "About",
  components: {GisSectionsTitle, GisPageTitle},
  data() {
    return {
      about: ''
    }
  },
  created() {
    this.loadAboutInfo()
  },
  methods: {
    async loadAboutInfo() {
      this.about = await this.$axios.get(`${this.$store.getters.getServerURL}/about`)
        .then(({data}) => {
          return data
        })
    }
  }
}
</script>

<style scoped>

</style>
