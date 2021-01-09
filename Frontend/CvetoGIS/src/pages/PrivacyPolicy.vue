<template>
<q-page>
  <gis-page-title :title="policy.title" />
  <div class="q-mt-xl" v-html="policy.text"></div>
</q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";
export default {
  name: "PrivacyPolicy",
  components: {GisPageTitle},
  data() {
    return {
      policy: ''
    }
  },
  created() {
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
