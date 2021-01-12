<template>
  <section class="hide-on-desktop">
    <div
      class="mobile-bottom-bar"
      :style="this.$q.platform.is.ios ? `height: 80px !important;` : ``"
    >
      <!--    Phone   -->
      <div class="b-phone text-center">
        <q-fab
          v-model="fabFirst"
          vertical-actions-align="left"
          color="white"
          icon="phone"
          class="" square
          direction="up" outline padding="10px"
        >
          <a :href="`tel:${contacts.phone}`">
            <q-fab-action label-position="right" color="primary" icon="phone_forwarded" label="Позвонить"
                          class="text-weight-bold"/>
          </a>
          <q-fab-action label-position="right" color="secondary" @click="callBack" icon="phone_callback"
                        label="Заказать обратный звонок" class="text-weight-bold"/>
        </q-fab>
      </div>
      <!--    xxxxx   -->
      <!--    Whatsapp   -->
      <div class="b-whatsapp text-center">
        <a :href="`https://wa.me/${contacts.whatsapp}`">
          <q-btn
            outline
            padding="10px"
            color="white"
            icon="mdi-whatsapp"
            class=""
            unelevated
          />
        </a>
      </div>
      <!--    xxxxx   -->
      <!--    Menu   -->
      <div class="b-menu text-center">
        <q-btn
          icon="menu"
          outline
          padding="10px"
          class=""
          color="white"
          @click="$emit('openMenu')"
        />
      </div>
      <gis-cart-icon :flat="false"/>
      <gis-customization-icon />
      <!--      xxxxx   -->
<!--      Cart   -->


    </div>
  </section>
</template>

<script>
import GisCartIcon from "components/utils/gisCartIcon";
import GisCustomizationIcon from "components/utils/gisCustomizationIcon";
export default {
  name: "gisMobileBottomBar",
  components: {GisCustomizationIcon, GisCartIcon},
  data() {
    return {
      fabFirst: false
    }
  },
  computed: {
    contacts() {
      return this.$store.getters.getContacts
    }
  },
  methods: {
    callBack() {
      this.$root.$emit('callBack')
    }
  }
}
</script>

<style lang="sass">
.rounded-white
  border-radius: 10px
  border: 1px solid #fff
.mobile-bottom-bar
  position: fixed
  bottom: 0
  left: 0
  right: 0
  height: 55px
  background: $primary
  z-index: 33
  display: grid
  grid-template-columns: repeat(5, 1fr)
  align-items: center
</style>
