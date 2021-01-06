<template>
  <div>
    <!--  Обратный звонок   -->
    <gis-call-back
      color="primary"
      class="hide-on-desktop full-width"
      style="margin-top: 65px; height: 55px; padding: 0 10px"
    />
    <!--   xxxxx   -->
    <!--   Выбор города   -->
    <gis-cities
      class="hide-on-desktop full-width text-center"
      color="primary"
    />
    <!--   xxxxx   -->
<!--    Меню   -->
    <gis-nav-menu />
<!--    xxxxx   -->
  </div>
</template>

<script>
import GisCallBack from "components/header/gisCallBack";
import GisCities from "components/header/gisCities";
import GisNavMenu from "components/header/gisNavMenu";

export default {
  name: "gisDrawerContent",
  components: {GisNavMenu, GisCities, GisCallBack}
}
</script>

<style scoped>

</style>
