<template>
  <q-page>

  </q-page>
</template>

<script>
export default {
  name: 'PageIndex',
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchHomeData', currentRoute.params.slug)
  },
  computed: {
    slides() {
      return this.$store.getters.getSlides
    }
  }
}
</script>
