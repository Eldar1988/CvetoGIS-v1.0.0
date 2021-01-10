<template>
  <div class="footer-wrapper q-py-sm">
<!--    Преимущества   -->
    <div class="benefits" style="margin-top: 130px">
      <div class="row">
        <div
          v-for="(benefit, index) in benefits"
          :key="index"
          class="col-12 col-md-6 col-lg-3 q-pa-sm"
        >
          <q-card
            class="rounded shadow-lt q-py-lg q-px-sm text-center bg-grey-1"
          >
            <q-icon
              :name="benefit.icon"
              size="lg"
            />
            <p class="text-h6 text-weight-bold q-py-md">{{ benefit.title }}</p>
            <p>{{ benefit.text }}</p>
          </q-card>
        </div>
      </div>
    </div>
<!--    xxxxx   -->
    <footer class="bg-primary rounded q-px-sm q-py-xl gis-footer">
      <div class="text-center">
<!--        Logo   -->
        <q-img
          src="../../assets/logo-white.png"
          width="250px"
        />
<!--        info  -->
        <p class="text-white q-py-md" style="max-width: 500px; width: 80%; margin: auto !important;">
          {{ aboutInfo.short_info }}
        </p>
      </div>

<!--      socials   -->
      <div class="flex flex-center">
        <a
          v-for="social in socials"
          :key="social.id"
          :href="social.url"
          class="q-mx-sm"
          target="_blank"
        >
          <q-icon :name="social.icon" size="lg" color="white" />
        </a>
      </div>

<!--      Links   -->
      <div class="links q-mt-xl text-center">
        <router-link
          class="text-grey-5 block"
          to="/privacy_policy"
        >
          Политика конфиденциальности
        </router-link>
        <router-link
          class="text-grey-5 block q-mt-md"
          to="/public_offer"
        >
         Публичная оферта
        </router-link>
      </div>

      <q-separator class="q-mt-lg" dark />
      <div class="company text-center text-white flex flex-center">
        <small class="text-uppercase q-pt-md">2021 Cvetogis</small>
      </div>
<!--   xxxxx   -->

    </footer>
  </div>
</template>

<script>
export default {
  name: "gisFooter",
  computed: {
    benefits() {
      return this.$store.getters.getBenefits
    },
    aboutInfo() {
      return this.$store.getters.getAboutInfo
    },
    socials() {
      return this.$store.getters.getSocials
    }
  }
}
</script>

<style lang="sass">
.gis-footer
  margin-top: 80px !important

</style>
