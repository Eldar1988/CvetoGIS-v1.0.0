<template>
  <article v-if="testimonial !== null">
    <q-card
      class="rounded shadow-0 q-pt-md q-pb-sm q-px-sm text-center testimonial-card"
    >
      <p class="text-h6 q-py-md">{{ testimonial.name }}</p>
      <q-rating
        v-model="testimonial.rating"
        color="secondary"
        readonly
      />
      <q-scroll-area
        :thumb-style="thumbStyle"
        style="height: 155px; max-width: 550px; margin: 15px auto 0; padding: 0 15px"
      >
        <p style="font-size: 14px">{{ testimonial.text }}</p>
      </q-scroll-area>
      <div
        class="q-mt-md"
      >
        <q-img
          v-if="testimonial.image"
          :src="testimonial.image"
          class="rounded"
          height="200px"
        >
          <template class="full-width" v-slot:loading>
            <q-skeleton
              class="full-width"
              height="200px"
            />
          </template>
        </q-img>
        <q-img
          v-else
          src="../../assets/icon-green.png"
          height="200px"
          contain
        />
      </div>
    </q-card>
  </article>
</template>

<script>
export default {
  name: "gisTestimonialCard",
  props: {
    testimonial: {
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
.testimonial-card
  border: 1px solid $grey-3
</style>
