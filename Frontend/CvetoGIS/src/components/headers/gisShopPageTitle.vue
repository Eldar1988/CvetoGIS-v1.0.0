<template>
  <q-card class="q-pa-md rounded shadow-lt text-center">
    <q-icon :name="iconName" size="lg" color="secondary"/>
    <h1 class="page-title">{{ title }}</h1>
    <p class="q-pt-sm">{{ description }}</p>
  </q-card>
</template>

<script>
export default {
  name: "gisShopPageTitle",
  props: {
    title: {
      type: String,
      default: 'Заголовок страницы'
    },
    description: {
      type: String,
      default: ''
    },
    iconName: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>

</style>
