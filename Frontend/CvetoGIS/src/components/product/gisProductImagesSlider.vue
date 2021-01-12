<template>
  <q-carousel
    swipeable
    animated
    v-model="slide"
    thumbnails
    infinite
    class="rounded shadow-lt product-slider"
  >
    <q-carousel-slide
      :name="10"
      :img-src="image"
    />
    <q-carousel-slide
      v-for="image in images"
      :key="image.id"
      :name="image.id"
      :img-src="image.image"
    />
  </q-carousel>
</template>

<script>
export default {
  name: "gisProductImagesSlider",
  props: {
    image: {
      type: String,
      default: ''
    },
    images: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      slide: 10
    }
  },
}
</script>

<style lang="sass">
.product-slider
  height: 800px

@media screen and (max-width: 1400px)
  .product-slider
    height: 650px

@media screen and (max-width: 650px)
  .product-slider
    height: 500px
</style>
