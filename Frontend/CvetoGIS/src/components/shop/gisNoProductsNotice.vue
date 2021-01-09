<template>
<article class="q-pa-sm">
    <q-card class="bg-secondary q-pa-xl rounded shadow-lt q-mt-lg">
      <q-card-section class="text-center">
        <h2 class="text-h6 text-white text-center">{{ text }}</h2>
        <q-btn rounded outline color="white" class="q-px-md q-mt-md text-weight-bold" @click="goToHome">Вернуться в магазин</q-btn>
      </q-card-section>
    </q-card>
</article>
</template>

<script>
export default {
  name: "gisNoProductsNotice",
  props: {
    text: {
      type: String,
      default: null
    }
  },
  methods: {
    // Переход на главную страницу
    goToHome() {
      let city = JSON.parse(localStorage.getItem('city'))
      if (city.slug === 'karaganda') {
        this.$store.dispatch('fetchHomeData', city.slug)
        this.$router.push(`/`)
      } else {
        this.$router.push(`/city/${city.slug}`)
      }
    }
  }
}
</script>

<style scoped>

</style>
