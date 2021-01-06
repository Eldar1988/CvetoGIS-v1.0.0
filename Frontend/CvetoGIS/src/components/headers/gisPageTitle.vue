<template>
  <q-card class="q-pa-md rounded shadow-lt text-center">
    <h1 class="page-title">{{ title }}</h1>
  </q-card>
</template>

<script>
export default {
  name: "gisPageTitle",
  props: {
    title: {
      type: String,
      default: 'Заголовок страницы'
    }
  }
}
</script>

<style scoped>

</style>
