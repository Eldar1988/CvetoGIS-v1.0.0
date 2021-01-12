<template>
  <q-page>
    <div style="padding: 5px">
      <gis-page-title :title="offer.title"/>
    </div>
    <div class="page-container">
      <div class="q-mt-xl" v-html="offer.text"></div>
    </div>
  </q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";

export default {
  name: "PublicOffer",
  components: {GisPageTitle},
  data() {
    return {
      offer: {}
    }
  },
  mounted() {
    this.loadOffer()
  },
  methods: {
    async loadOffer() {
      this.offer = await this.$axios.get(`${this.$store.getters.getServerURL}/offer`).then(({data}) => {
        return data
      })
    }
  }
}
</script>

<style scoped>

</style>
