<template>
<article>
  <q-img
    :src="obj.image"
    class="rounded img-overlay-2 page-title-image"
  >
  <template v-slot:loading class="full-width">
    <q-skeleton class="full-width" height="450px" />
  </template>
    <div class="page-title-image-text text-dark text-center">
      <h1 class="page-title">
        {{ obj.title }}
      </h1>
      <q-scroll-area
        :thumb-style="thumbStyle"
        style="height: 130px; max-width: 550px; margin: 15px auto 0"
      >
        <p>{{ obj.description }}</p>
      </q-scroll-area>
    </div>
  </q-img>

</article>
</template>

<script>
export default {
  name: "gisPageImageTitle",
  props: {
    obj: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      thumbStyle: {
        right: '2px',
        borderRadius: '5px',
        backgroundColor: '#477b78',
        width: '5px',
        opacity: 0.75
      }
    }
  },
}
</script>

<style lang="sass">
.page-title-image-text
  position: absolute
  bottom: 0
  left: 10px
  right: 10px
  z-index: 25

.page-title-image
  height: 450px

@media screen and (max-width: 650px)
  .page-title-image
    height: 350px

</style>
