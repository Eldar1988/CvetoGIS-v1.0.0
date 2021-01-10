<template>
  <q-page>
    <gis-page-title :title="contacts.title"/>
    <div
      class="q-mt-xl text-center text-weight-bold"
      v-html="contacts.description"
      style="font-size: 16px"
    ></div>

<!--    phone   -->
    <div class="text-center q-mt-xl">
      <a
        :href="`tel:${contacts.phone}`"
        class="text-weight-bold contacts-item"
      >
        <q-icon name="call" size="24px" />
        {{ contacts.phone }}
      </a>
    </div>

<!--    whatsapp   -->
    <div class="text-center q-mt-xl">
      <a
        :href="`https://wa.me/${contacts.whatsapp}`"
        class="text-weight-bold contacts-item"
      >
        <q-icon name="mdi-whatsapp" size="24px" />
        {{ contacts.whatsapp }}
      </a>
    </div>

    <!--    email   -->
    <div class="text-center q-mt-xl">
      <a
        :href="`mailto:${contacts.email}`"
        class="text-weight-bold contacts-item"
      >
        <q-icon name="mail" size="24px" />
        {{ contacts.email }}
      </a>
    </div>

    <!--    address   -->
    <div v-if="contacts.address" class="text-center q-mt-xl">
      <p class="text-weight-bold contacts-item" style="max-width: 500px; margin: auto !important;">
        <q-icon name="place" size="24px" /><br>
        {{ contacts.address }}
      </p>
    </div>
  </q-page>
</template>

<script>
import GisPageTitle from "components/headers/gisPageTitle";

export default {
  name: "Contacts",
  components: {GisPageTitle},
  computed: {
    contacts() {
      return this.$store.getters.getContacts
    }
  }
}
</script>

<style lang="sass">
.contacts-item
  font-size: 16px
  border: 1px solid $dark
  padding: 10px 35px
  border-radius: 10px

</style>
