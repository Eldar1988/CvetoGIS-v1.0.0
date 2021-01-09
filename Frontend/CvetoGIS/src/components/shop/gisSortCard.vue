<template>
  <article v-if="sort !== null">
    <router-link :to="`/sort/${sort.slug}`">
      <q-card
        class="rounded shadow-lt"
      >
        <q-img
          :src="sort.miniature"
          height="120px"
          class="img-overlay-2"
        >
          <div class="category-card-title">
            <p class="text-h6 text-weight-bold text-dark">{{ sort.title }}</p>
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
  name: "gisSortCard",
  props: {
    sort: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
