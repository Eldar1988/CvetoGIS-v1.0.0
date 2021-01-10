<template>
  <q-card class="q-pa-md shadow-0 rounded bg-grey-1 text-center">
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
