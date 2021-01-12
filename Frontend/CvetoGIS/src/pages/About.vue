<template>
  <div>
    <div style="padding: 5px">
      <gis-page-title :title="about.title"/>
    </div>
    <article class="page-container">

      <div class="q-mt-xl" v-html="about.info"></div>
      <div class="about-logo text-center q-mt-xl">
        <q-img :src="about.logo" width="300px" class="q-my-lg"/>
      </div>
    </article>
  </div>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";

export default {
  name: "About",
  components: {GisPageTitle},
  data() {
    return {
      about: ''
    }
  },
  mounted() {
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
