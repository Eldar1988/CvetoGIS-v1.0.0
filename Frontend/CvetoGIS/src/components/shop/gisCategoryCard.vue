<template>
  <article v-if="category !== null">
    <router-link :to="`/category/${category.slug}`">
      <q-card
        class="rounded shadow-lt"
      >
        <q-img
          :src="category.miniature"
          height="120px"
          class="img-overlay-2"
        >
          <div class="category-card-title">
            <p class="text-h6 text-weight-bold text-dark">{{ category.title }}</p>
          </div>
          <template
            class="full-width"
            v-slot:loading
          >
            <q-skeleton
              height="120px"
              class="full-width"
            />
          </template>
        </q-img>
      </q-card>
    </router-link>
  </article>
</template>

<script>
export default {
  name: "gisCategoryCard",
  props: {
    category: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.category-card-title
  position: absolute
  bottom: -5px
  left: 5px
  right: 5px
  text-align: center
  z-index: 25
</style>
