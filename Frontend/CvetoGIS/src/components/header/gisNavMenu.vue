<template>
  <nav class="right-menu-wrapper">
    <!--    Поводы   -->
    <div>
      <q-toolbar class="bg-grey-3 text-dark text-uppercase">
        <q-toolbar-title class="text-weight-bold text-h6">
          Поводы
        </q-toolbar-title>
      </q-toolbar>
      <q-list class="rounded-borders text-primary text-weight-bold">

        <q-item
          v-for="reason in reasons" :key="reason.id"
          clickable
          v-ripple
          class="text-dark"
          exact-active-class="text-secondary"
          :to="`/reason/${reason.slug}`"
        >
            <q-item-section avatar>
              <q-icon :name="reason.icon"/>
            </q-item-section>
            <q-item-section>{{ reason.title }}</q-item-section>
        </q-item>

      </q-list>
    </div>
    <!--    ================   -->
    <!--    Категории   -->
    <div class="q-mt-md text-weight-bold">
      <q-toolbar class="bg-grey-3 text-dark text-uppercase q-mb-sm">
        <q-toolbar-title class="text-weight-bold text-h6">
          Категории
        </q-toolbar-title>
      </q-toolbar>
      <q-list class="rounded-borders">
        <q-item
          v-for="category in categories" :key="category.id"
          clickable
          v-ripple
          class="text-dark"
          :to="`/category/${category.slug}`"
          exact-active-class="text-primary bg-grey-3"
        >
          <q-img
            :src="category.miniature"
            no-default-spinner
            class="img-overlay-2 rounded shadow-lt"
            height="75px"

          >
            <template v-slot:loading class="full-width">
              <q-skeleton height="75px" class="full-width" />
            </template>
            <div class="image-text-bottom" style="color: inherit">
              {{ category.title }}
            </div>
          </q-img>
        </q-item>
      </q-list>
    </div>
    <!--   xxxxx   -->
    <!--   Сорта   -->
    <div class="q-mt-md text-weight-bold">
      <q-toolbar class="bg-grey-3 text-dark text-uppercase q-mb-sm">
        <q-toolbar-title class="text-weight-bold text-h6">
          Цветы
        </q-toolbar-title>
      </q-toolbar>
      <q-list class="rounded-borders text-primary">
        <q-item
          v-for="sort in sorts" :key="sort.id"
          clickable
          v-ripple
          class="text-dark"
          :to="`/sort/${sort.slug}`"
          exact-active-class="text-secondary"
        >
          <q-avatar class="shadow-lt">
            <q-img
              :src="sort.miniature"
              class=""
              style="height: 100%"
            />
          </q-avatar>
          <q-item-section class="q-ml-sm">{{ sort.title }}</q-item-section>
        </q-item>
      </q-list>
    </div>
    <!--   xxxxx   -->
    <!--   Информация   -->
    <div class="q-mt-md text-weight-bold">
      <q-toolbar class="bg-grey-3 text-dark text-uppercase q-mb-sm">
        <q-toolbar-title class="text-weight-bold text-h6">
          Информация
        </q-toolbar-title>
      </q-toolbar>
      <q-list class="rounded-borders text-primary text-weight-bold">
        <!--   Главная   -->
        <q-item
          clickable
          v-ripple
          class="text-dark"
          @click="goToHome"
          exact-active-class="text-secondary"
        >
          <q-item-section avatar>
            <q-icon name="roofing"/>
          </q-item-section>
          <q-item-section>Главная</q-item-section>
        </q-item>
        <!--   О нас   -->
        <q-item
          clickable
          v-ripple
          class="text-dark"
          exact-active-class="text-secondary"
          to="/about"
        >
          <q-item-section avatar>
            <q-icon name="emoji_nature"/>
          </q-item-section>
          <q-item-section>О нас</q-item-section>
        </q-item>

        <!--   Отзывы   -->
        <q-item
          clickable
          v-ripple
          class="text-dark"
          to="/testimonials"
          exact-active-class="text-secondary"
        >
          <q-item-section avatar>
            <q-icon name="mark_chat_read"/>
          </q-item-section>
          <q-item-section>Отзывы</q-item-section>
        </q-item>
      </q-list>
    </div>
    <!--   xxxxx   -->
  </nav>
</template>

<script>
export default {
  name: "gisNavMenu",
  data() {
    return {
      menuItems: []
    }
  },
  computed: {
    categories() {
      return this.$store.getters.getCategories
    },
    reasons() {
      return this.$store.getters.getReasons
    },
    sorts() {
      return this.$store.getters.getSorts
    }
  },
  methods: {
    // Переход на главную страницу
    goToHome() {
      let city = JSON.parse(localStorage.getItem('city'))
      if (city.slug === 'karaganda') {
        this.$store.dispatch('fetchHomeData', city.slug)
        this.$router.push(`/`)
      } else {
        this.$router.push(`/city/${city.slug}`)
      }
    }
  }
}
</script>

<style lang="sass">
.right-menu-wrapper
  margin-top: 50px

.q-item__section
  font-size: 16px

@media screen and (max-width: 800px)
  .right-menu-wrapper
    margin-top: 5px
</style>
