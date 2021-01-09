<template>
  <article v-if="reason !== null">
    <router-link :to="`/reason/${reason.slug}`">
      <q-card
        class="rounded shadow-lt flex flex-center bg-accent"
        style="height: 120px"
      >
          <div class="reason-card-title text-center">
            <q-icon :name="reason.icon" size="lg" />
            <p class="text-h6 text-weight-bold">{{ reason.title }}</p>
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
      </q-card>
    </router-link>
  </article>
</template>

<script>
export default {
  name: "gisReasonCard",
  props: {
    reason: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
