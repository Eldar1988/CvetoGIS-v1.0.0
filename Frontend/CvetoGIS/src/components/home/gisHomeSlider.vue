<template>
  <div style="padding: 5px">
    <q-carousel
      swipeable
      animated
      v-model="slide"
      thumbnails
      infinite
      autoplay=""
      class="rounded shadow-lt home-slider"
      navigation-position="top"
    >
      <q-carousel-slide
        v-for="(slide, index) in slides" :key="slide.id"
        :name="index"
        :img-src="slide.image"
        class="img-overlay-1"
      >
        <div class="slide-info text-center text-white">
          <h2 class="text-h5 text-weight-bold">
            {{ slide.title }}
          </h2>
          <p class="q-py-sm">{{ slide.text }}</p>
          <q-btn
            :to="slide.button_url"
            color="secondary"
            rounded unelevated
            class="q-px-lg q-mt-md text-weight-bold"
            :label="slide.button_text"
          />
        </div>
      </q-carousel-slide>

    </q-carousel>
  </div>
</template>

<script>
export default {
  name: "gisHomeSlider",
  data() {
    return {
      slide: 0
    }
  },
  computed: {
    slides() {
      return this.$store.getters.getSlides
    }
  }
}
</script>

<style lang="sass">
.slide-info
  position: absolute
  bottom: 15px
  left: 10px
  right: 10px
  z-index: 10

.home-slider
  height: 500px

@media screen and (max-width: 650px)
  .home-slider
    height: 350px
</style>
