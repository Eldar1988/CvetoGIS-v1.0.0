<template>
  <div class="q-ml-md">
    <q-btn-dropdown
      :color="color"
      :label="currentCurrency.title"
      dropdown-icon="mdi-menu-down"
      flat rounded
      class="text-weight-bold"
    >
      <q-list>
        <q-item
          v-for="currency in currencies" :key="currency.id"
          clickable v-close-popup
        >
          <q-item-section @click="setCurrency(currency)">
            <q-item-label>
              {{ currency.title }}
            </q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>

<script>
export default {
  name: "gisCurrency",
  props: {
    color: {
      type: String,
      default: 'white'
    }
  },
  computed: {
    currencies() {
      return this.$store.getters.getCourses
    },
    currentCurrency() {
      return this.$store.getters.getCurrentCurrency
    }
  },
  mounted() {
  },
  methods: {
    setCurrency(currency) {
      return this.$store.dispatch('setCurrentCurrency', currency)
    }
  }
}
</script>

<style scoped>

</style>
