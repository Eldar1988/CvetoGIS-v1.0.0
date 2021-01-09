<template>
<section>
  <div class="section">
    <gis-sections-title title="Отзывы наших клиентов" />
    <!--    Scroll controls   -->
    <div class="scroll-controls text-center q-mt-md">
      <q-btn
        @click="scrollLeft"
        icon="navigate_before"
        round
        color="primary"
      />
      <q-btn
        @click="scrollRight"
        icon="navigate_next"
        round
        color="primary"
        class="q-ml-sm"
      />
    </div>
    <!--   xxxxx   -->
    <!--    Scroll Area   -->
    <q-scroll-area
      ref="scrollFutureProducts"
      horizontal
      class="full-width q-mt-md"
      style="height: 540px; width: 100%"
      :thumb-style="{ display: 'none' }"
    >
      <div class="row no-wrap q-mt-md">
        <div
          v-for="(testimonial, index) in testimonials" :key="index"
          class="product-wrapper"
          style="width: 320px; padding: 0 7px"
        >
          <gis-testimonial-card
            :testimonial="testimonial"
          />
        </div>
      </div>
    </q-scroll-area>
    <!--  xxxxx   -->
    <div class="text-center">
    <q-btn
      icon-right="mark_chat_read"
      label="Все отзывы"
      rounded
      color="primary"
      class="q-py-sm q-px-md shadow-lt text-weight-bold"
      to="/testimonials"
    />
    </div>
  </div>
</section>
</template>

<script>
import GisTestimonialCard from "components/shop/gisTestimonialCard";
import GisSectionsTitle from "components/headers/gisSectionsTitle";
export default {
  name: "gisTestimonials",
  components: {GisSectionsTitle, GisTestimonialCard},
  data() {
    return {
      position: 0
    }
  },
  computed: {
    testimonials() {
      return this.$store.getters.getTestimonials
    }
  },
  methods: {
    // Скролл вправо
    scrollRight() {
      // Проверка: количество карточек * ширину экрана (98% ширина контейнера)
      if (this.position < this.testimonials.length * 320 - (window.innerWidth * 0.98)) {
        this.position += 320
        this.$refs.scrollFutureProducts.setScrollPosition(this.position, 500)
      }
    },
    // Левый скролл
    scrollLeft() {
      if (this.position !== 0) {
        this.position = this.position - 320
        this.$refs.scrollFutureProducts.setScrollPosition(this.position, 500)
      }
    }
  }
}
</script>

<style scoped>

</style>
