<template>
  <div>
    <q-btn
      class="q-px-md text-weight-bold full-width shadow-lt"
      :color="color"
      outline rounded unelevated
      @click="dialog = true"
      label="Обратный звонок"
      icon-right="phone_callback"
    />

    <!--    Диалог   -->
    <q-dialog v-model="dialog">
      <q-card class="text-dark" style="width: 600px; max-width: 80vw;">
        <!--        Верхняя панель   -->
        <q-toolbar class="bg-primary">
          <gis-logo-icon />
          <q-space/>
          <q-btn
            dense flat
            icon="mdi-close"
            color="white"
            rounded
            v-close-popup/>
        </q-toolbar>
        <!--        ================   -->
        <!--        Тело диалогового окна   -->
        <q-card-section class="q-pt-md">
          <h6 class="q-mt-sm text-weight-bold">Обратный звонок</h6>
          <p class="q-pt-md">
            Заполните форму обратной связи<br>
            Мы свяжемся с Вами в ближайшее время
          </p>
          <q-form class="q-mt-lg">
            <q-input
              v-model="name"
              label="Ваше имя*"
              :dense="dense"
              class="q-mt-sm shadow-lt rounded-35 q-px-md"
              rounded borderless
            />
            <q-input
              type="number"
              v-model="phone"
              label="Номер телефона*"
              :dense="dense"
              class="q-mt-md shadow-lt rounded-35 q-px-md"
              rounded borderless
            />
            <q-btn
              class="q-mt-lg block full-width shadow-lt q-py-sm text-weight-bold"
              color="secondary"
              unelevated rounded
              label="Отправить"
            >
              <q-icon name="mdi-send" color="white" class="q-pl-sm" />
            </q-btn>
          </q-form>
        </q-card-section>
        <!--        ===================   -->
      </q-card>
    </q-dialog>
    <!--    ==========   -->
  </div>
</template>

<script>
import GisLogoIcon from "components/header/gisLogoIcon";
export default {
  name: "gisCallBack",
  components: {GisLogoIcon},
  props: {
    color: {
      type: String,
      default: 'white'
    }
  },
  data() {
    return {
      dialog: false,
      name: '',
      phone: '',
      dense: false
    }
  }
}
</script>

<style scoped>

</style>
