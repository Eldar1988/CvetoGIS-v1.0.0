<template>
<span class="text-center">
  <q-btn
    outline
    class=""
    icon="settings"
    color="white"
    @click="settingDialog = !settingDialog"
    style="padding: 4px 0"
  />

  <!--    Диалог   -->
  <q-dialog v-model="settingDialog" position="top" >
    <q-card class="text-white bg-primary text-center q-pb-lg" style="width: 600px; max-width: 100vw;">
      <!--        Верхняя панель   -->
      <q-toolbar>
        <gis-logo-icon />
        <q-space/>
        <q-btn
          dense flat
          icon="mdi-close"
          color="white"
          rounded
          @click="settingDialog = false"/>
      </q-toolbar>
<!--      xxxxx   -->
      <q-separator dark inset />
      <p class="q-py-md">Ваш город:</p>
      <gis-cities />
      <q-separator class="q-mt-lg" dark inset />
      <p class="q-py-md">Валюта:</p>
      <gis-currency />
    </q-card>
  </q-dialog>
<!--  xxxxx   -->
</span>
</template>

<script>
import GisLogoIcon from "components/header/gisLogoIcon";
import GisCities from "components/header/gisCities";
import GisCurrency from "components/header/gisCurrency";
export default {
  name: "gisCustomizationIcon",
  components: {GisCurrency, GisCities, GisLogoIcon},
  data() {
    return {
      settingDialog: false
    }
  },
}
</script>

<style scoped>

</style>
