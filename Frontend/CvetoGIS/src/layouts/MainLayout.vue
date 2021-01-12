<template>
  <q-layout view="hHh lpR ffr" style="position: relative">
    <!--    Header   -->
    <q-header class="bg-primary text-white" style="height: 55px">
      <q-toolbar>
        <!--   Логотип   -->
        <img src="../assets/logo-white.png" style="width: 150px; cursor: pointer" @click="goToHome"/>
        <!--   xxxxx   -->
        <q-space/>
        <!--   Обратный звонок   -->
        <GisCallBack class="hide-on-mobile"/>
        <!--   xxxxx   -->
        <!--   Выбор города  -->
        <gis-cities class="hide-on-mobile"/>
        <!--   xxxxx   -->
        <!--   Выбор валюты   -->
        <gisCurrency/>
        <!--   xxxxx   -->
        <!--        Корзина   -->
        <gis-cart-icon class="q-ml-lg hide-on-mobile"/>
        <!--        xxxxx   -->
        <!--   Кнопка управляющая меню   -->
        <q-btn dense flat size="lg" icon="view_list" @click="right = !right"/>
        <!--   xxxxx   -->
      </q-toolbar>
    </q-header>
    <!--    xxxxx   -->

    <!--    Content   -->
    <q-page-container
      style="padding-top: 60px !important; margin: 0 2px"
    >
      <router-view/>
      <!--    Footer   -->
      <gis-footer/>
      <!--   xxxxx   -->
    </q-page-container>
    <!--    xxxxx   -->

    <!--    Menu   -->
    <q-drawer show-if-above v-model="right" side="right" bordered>
      <q-header class="bg-primary hide-on-desktop" style="height: 55px">
        <q-toolbar class="">
          <q-toolbar-title class="text-uppercase text-weight-bold flex" style="align-items: center">
            <gis-logo-icon class="q-mr-sm"/>
            Меню
          </q-toolbar-title>
          <q-btn flat v-close-popup round dense icon="mdi-close" @click="right = false"/>
        </q-toolbar>
      </q-header>
      <gis-drawer-content/>
    </q-drawer>
    <!--    xxxxx   -->
    <!--    Mobile Bottom Bar   -->
    <gis-mobile-bottom-bar @openMenu="right = !right"/>
    <!--    xxxxx   -->
    <gis-added-to-cart-dialog/>
  </q-layout>
</template>

<script>

import GisCallBack from "components/header/gisCallBack";
import gisCurrency from "components/header/gisCurrency";
import GisDrawerContent from "components/header/gisDrawerContent";
import GisCities from "components/header/gisCities";
import GisLogoIcon from "components/header/gisLogoIcon";
import GisAddedToCartDialog from "components/shop/gisAddedToCartDialog";
import GisFooter from "components/footer/gisFooter";
import GisMobileBottomBar from "components/utils/gisMobileBottomBar";
import GisCartIcon from "components/utils/gisCartIcon";

export default {
  name: 'MainLayout',
  components: {
    GisCartIcon,
    GisMobileBottomBar,
    GisFooter, GisAddedToCartDialog, GisLogoIcon, GisCities, GisDrawerContent, gisCurrency, GisCallBack
  },
  data() {
    return {
      right: false
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchMainData', currentRoute.params.slug)
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


