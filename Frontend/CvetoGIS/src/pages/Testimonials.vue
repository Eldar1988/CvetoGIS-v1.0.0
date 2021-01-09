<template>
  <q-page>
    <gis-page-title title="Отзывы наших клиентов"/>
    <!--  Отзывы   -->
    <section class="section text-center">
      <div class="row">
        <div
          v-for="(testimonial, index) in testimonials"
          :key="index"
          class="col-12 col-sm-6 col-md-6 col-lg-3 q-pa-sm"
        >
          <gis-testimonial-card :testimonial="testimonial"/>
        </div>
      </div>
      <q-btn
        class="q-py-sm q-px-md text-weight-bold shadow-lt q-mt-lg"
        label="Добавить отзыв"
        @click="addTestimonialDialog = true"
        rounded
        color="primary"
        icon-right="add_comment"
        unelevated
      />
    </section>
    <!--  xxxxx   -->
    <!--  Добавить отзыв диалог   -->
    <q-dialog
      v-model="addTestimonialDialog"
    >
      <q-card
        style="max-width: 550px; width: 550px"
      >
        <q-toolbar class="bg-primary text-white">
          <q-avatar>
            <gis-logo-icon/>
          </q-avatar>
          <q-space/>
          <q-btn flat round dense icon="close" v-close-popup/>
        </q-toolbar>

        <div class="col-12 col-md-6 q-pa-md">
          <p class="q-py-sm">Для того, чтобы оставить отзыв,<br>заполните форму ниже</p>
          <!--          Оценка   -->
          <div class="rating text-center q-my-md">
            <p class="q-py-sm text-weight-bold">Ваша оценка {{
                newTestimonial.rating ? newTestimonial.rating : `*`
              }}</p>
            <q-rating
              v-model="newTestimonial.rating"
              size="32px"
              color="secondary"
            />
          </div>
          <!--   Имя   -->
          <q-input
            rounded
            class="shadow-lt rounded-35 q-pl-md"
            borderless
            v-model="newTestimonial.name"
            label="Ваше имя*"
          />
          <!--   Текст   -->
          <q-input
            rounded
            class="shadow-lt rounded-35 q-pl-md q-mt-lg"
            borderless
            type="textarea"
            v-model="newTestimonial.text"
            label="Ваш отзыв*"
          />
          <!--   Фото   -->
<!--          <q-file-->
<!--            rounded borderless-->
<!--            name="Фото"-->
<!--            v-model="newTestimonial.image"-->
<!--            class="shadow-lt rounded-35 q-pl-md q-mt-lg"-->
<!--            label="Добавить фото"-->
<!--          >-->
<!--            <template v-slot:prepend>-->
<!--              <q-icon name="attach_file"/>-->
<!--            </template>-->
<!--          </q-file>-->

          <q-slide-transition>
            <q-btn
              v-if="showAddTestimonialButton"
              rounded
              class="full-width shadow-lt q-py-sm q-px-md q-mt-xl text-weight-bold"
              label="Отправить"
              color="primary"
              icon-right="send"
              :loading="loading"
              @click="addTestimonial"
            />
          </q-slide-transition>

        </div>
      </q-card>
    </q-dialog>
    <!--  xxxxx   -->
  </q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";
import GisTestimonialCard from "components/shop/gisTestimonialCard";
import GisLogoIcon from "components/header/gisLogoIcon";

export default {
  name: "Testimonials",
  components: {GisLogoIcon, GisTestimonialCard, GisPageTitle},
  data() {
    return {
      testimonials: [],
      newTestimonial: {
        name: '',
        text: '',
        rating: 0,
        image: []
      },
      addTestimonialDialog: false,
      loading: false
    }
  },
  computed: {
    showAddTestimonialButton() {
      return this.newTestimonial.name && this.newTestimonial.text && this.newTestimonial.rating
    }
  },
  created() {
    this.loadTestimonials()
  },
  methods: {
    async loadTestimonials() {
      this.testimonials = await this.$axios.get(`${this.$store.getters.getServerURL}/testimonials/`)
        .then(({data}) => {
          return data
        })
    },

    async addTestimonial() {
      this.loading = true
      await fetch(`${this.$store.getters.getServerURL}/testimonials/`,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.newTestimonial)
      }).then(response => {
        if(response.status === 201) {
          setTimeout(
            () => {
              this.loading = false
              this.$q.notify({
                  color: 'secondary',
                  message: 'Спасибо! Ваш отзыв скоро появится на сайте.'
                }
              )
              this.addTestimonialDialog = false
            }, 2000
          )
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
