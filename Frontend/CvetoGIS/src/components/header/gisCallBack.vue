<template>
  <div>
    <q-btn
      class="q-px-md text-weight-bold full-width rounded"
      :color="color"
      outline unelevated
      @click="dialog = true"
      label="Обратный звонок"
      icon-right="phone_callback"
    />

    <!--    Диалог   -->
    <q-dialog v-model="dialog">
      <q-card class="text-dark" style="width: 600px; max-width: 80vw;">
        <!--        Верхняя панель   -->
        <q-toolbar class="bg-primary">
          <gis-logo-icon/>
          <q-space/>
          <q-btn
            dense flat
            icon="mdi-close"
            color="white"
            rounded
            @click="dialog = false"/>
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
              v-model="callBackData.name"
              label="Ваше имя*"
              :dense="dense"
              class="q-mt-sm shadow-lt rounded q-px-md"
              borderless
            />
            <q-input
              type="number"
              v-model="callBackData.phone"
              label="Номер телефона*"
              :dense="dense"
              class="q-mt-md shadow-lt rounded q-px-md"
              borderless
            />
            <q-btn
              class="q-mt-lg block full-width shadow-lt q-py-sm text-weight-bold rounded"
              color="secondary"
              unelevated
              label="Отправить"
              @click="sendCallBack"
              :loading="loading"
            >
              <q-icon name="mdi-send" color="white" class="q-pl-sm"/>
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
  created() {
    this.$root.$on('callBack', () => this.dialog = !this.dialog)
  },
  data() {
    return {
      dialog: false,
      callBackData: {
        name: '',
        phone: '',
      },
      dense: false,
      loading: false
    }
  },
  methods: {
    async sendCallBack() {
      if (this.callBackData.name.length < 2) {
        this.$q.notify({
          message: 'Необходимо указать Ваше имя*',
          color: 'secondary'
        })
        return null
      }
      if (this.callBackData.phone.length < 5) {
        this.$q.notify({
          message: 'Необходимо указать номер телефона*',
          color: 'secondary'
        })
        return null
      }
      this.loading = true
      await fetch(`${this.$store.getters.getServerURL}/orders/call_back/`,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.callBackData)
      }).then(response => {
        if (response.status === 201) {
          setTimeout(() => {
            this.loading = false
            this.$router.push(
              '/call_back_thanks'
            )
          },1500)
        } else {
          this.$q.notify({
            message: 'Извините, что-то пошло не так. Пожалуйста, попробуйте еще раз*',
            color: 'secondary'
          })
        }

      })

    }
  }
}
</script>

<style scoped>

</style>
