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
          active-class="primary"
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
      <q-list class="rounded-borders text-primary">
        <q-item
          v-for="category in categories" :key="category.id"
          clickable
          v-ripple
          class="text-dark"
          active-class="primary"
        >
          <q-img
            :src="category.miniature"
            no-default-spinner
            class="img-overlay-2 rounded shadow-lt"
            style="max-height: 50px; width: 100%; object-fit: cover"
          >
            <div class="image-text-bottom text-dark">
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
          Сорта
        </q-toolbar-title>
      </q-toolbar>
      <q-list class="rounded-borders text-primary">
        <q-item
          v-for="sort in sorts" :key="sort.id"
          clickable
          v-ripple
          class="text-dark"
          active-class="primary"
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
          active-class="primary"
          to=""
        >
          <q-item-section avatar>
            <q-icon name="roofing"/>
          </q-item-section>
          <q-item-section>Главная</q-item-section>
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
