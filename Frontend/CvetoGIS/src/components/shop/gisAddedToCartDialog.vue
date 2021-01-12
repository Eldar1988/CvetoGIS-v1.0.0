<template>
  <!--    Диалог   -->
  <q-dialog v-model="dialog">
    <q-card class="text-white bg-primary text-center q-pa-sm" style="width: 600px; max-width: 80vw;">
      <!--        Верхняя панель   -->
      <q-toolbar class="bg-primary">
        <gis-logo-icon />
        <!--          <q-toolbar-title class="text-white text-uppercase">Обратный звонок</q-toolbar-title>-->
        <q-space/>
        <q-btn dense flat icon="mdi-close" color="white" v-close-popup/>
      </q-toolbar>
      <!--        ================   -->
      <!--        Тело диалогового окна   -->
      <q-card-section class="q-pt-md">
        <h6 class="">"{{ title }}" <br> теперь в вашей корзине</h6>
      </q-card-section>
      <!--        ===================   -->
      <!--      Кнопки корзины   -->
      <q-card-actions class="row justify-center">
        <q-btn outline class="q-px-md q-mt-md text-weight-bold rounded" to="/cart" icon-right="forward">Перейти в корзину</q-btn>
        <q-btn flat class="q-px-md q-mt-md text-weight-bold rounded" v-close-popup>Продолжить покупки</q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>
  <!--    ==========   -->
</template>

<script>
import GisLogoIcon from "components/header/gisLogoIcon";
export default {
name: "gisAddedToCartDialog",
  components: {GisLogoIcon},
  data() {
    return {
      dialog: false,
      title: ''
    }
  },
  mounted() {
    this.addedProduct()
    this.$root.$on('addToCartDialog', () => {
      setTimeout(() => {
        this.title = localStorage.getItem('addedProduct')
        this.dialog = true
      }, 100)
    })
  },
  methods: {
    addedProduct() {
      return localStorage.getItem('addedProduct')
    }
  }
}
</script>

<style scoped>

</style>
