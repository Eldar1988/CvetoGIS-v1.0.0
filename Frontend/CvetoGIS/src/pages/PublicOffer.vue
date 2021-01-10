<template>
  <q-page>
    <gis-page-title :title="offer.title" />
    <div class="q-mt-xl" v-html="offer.text"></div>
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
  created() {
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
