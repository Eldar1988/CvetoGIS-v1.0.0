<template>
<div>
<h4 class="text-h6 text-center text-weight-bold">
  {{ title }}
</h4>
</div>
</template>

<script>
export default {
  name: "gisSectionsTitle",
  props: {
    title: {
      type: String,
      default: 'title'
    }
  }
}
</script>

<style scoped>

</style>
