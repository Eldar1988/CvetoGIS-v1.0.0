<template>
  <div class="q-ml-md">
    <q-btn-dropdown
      :color="color"
      :label="currentCity"
      icon="mdi-google-maps"
      dropdown-icon="mdi-menu-down"
      flat rounded
      class="text-weight-bold"
    >
      <q-list>
        <q-item
          v-for="city in cities" :key="city.id"
          clickable v-close-popup
          @click="onItemClick">
          <q-item-section @click="setCity(city)"
          >
            <q-item-label>{{ city.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>

<script>
export default {
  name: "gisCities",
  props: {
    color: {
      type: String,
      default: 'white'
    }
  },
  data() {
    return {
      dialog: false,
      currentCity: ''
    }
  },
  mounted() {
    this.setCityBySlug()
  },
  computed: {
    cities() {
      return this.$store.getters.getCities;
    }
  },
  methods: {
    onItemClick() {
    },

    // Изменение - установление города из меню
    setCity(city) {
      localStorage.setItem('city', JSON.stringify(city))
      let currentCityObj = JSON.parse(localStorage.getItem('city'))
      this.currentCity = currentCityObj.title
      this.$root.$emit('changeCity')
      if (city.slug === 'karaganda') {
        this.$store.dispatch('fetchHomeData', city.slug)
        this.$router.push(`/`)
      } else {
        this.$router.push(`/${city.slug}`)
      }
      let cart = []
      localStorage.setItem('cart', JSON.stringify(cart))
    },

    // Установление города по слагу
    setCityBySlug() {
      let cities = this.$store.getters.getCities // Получаем список городов
      // Если слаг совпадает со слагом города устанавливаем город в хранилище
      cities.forEach((item) => {
        if (this.$route.params.slug === item.slug) {
          localStorage.setItem('city', JSON.stringify(item))
          let currentCityObj = JSON.parse(localStorage.getItem('city'))
          return this.currentCity = currentCityObj.title
        }
      })

      // Устанавливаем город из хранилища. если его нет в слаге
      if (localStorage.getItem('city') !== null) {
        let currentCityObj = JSON.parse(localStorage.getItem('city'))
        this.currentCity = currentCityObj.title
        return
      }

      // Устанавливаем город по умолчанию, если нет слага и нет города в хранилище
      let defaultCity = this.$store.getters.getDefaultCity
      if (this.$route.params.slug === undefined) {
        localStorage.setItem('city', JSON.stringify(defaultCity))
        this.currentCity = defaultCity.title
      }
    }
  }
}
</script>

<style scoped>

</style>
