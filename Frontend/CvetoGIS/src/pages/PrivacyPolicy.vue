<template>
  <q-page>
    <div style="padding: 5px">
      <gis-page-title :title="policy.title"/>
    </div>
    <div class="q-pt-xl page-container" v-html="policy.text"></div>
  </q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";

export default {
  name: "PrivacyPolicy",
  components: {GisPageTitle},
  data() {
    return {
      policy: {}
    }
  },
  mounted() {
    this.loadPolicy()
  },
  methods: {
    async loadPolicy() {
      this.policy = await this.$axios.get(`${this.$store.getters.getServerURL}/policy`).then(({data}) => {
        return data
      })
    }
  }
}
</script>

<style scoped>

</style>
