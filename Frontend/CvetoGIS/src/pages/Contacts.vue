<template>
  <div>
    <gis-page-title :title="contacts.title"/>
    <section class="page-container">
      <div
        class="q-mt-xl text-weight-bold"
        v-html="contacts.description"
        style="font-size: 16px"
      ></div>

      <!--    phone   -->
      <div class="q-mt-lg">
        <p class="product-card-title text-weight-bold">
          Телефон:
          <span class="text-weight-regular">
          <a :href="`tel:${contacts.phone}`">
            {{ contacts.phone }}
          </a>
            </span>
        </p>
      </div>

      <!--    whatsapp   -->
      <div class="q-mt-sm">
        <p class="product-card-title text-weight-bold">
          Whatsapp:
          <span class="text-weight-regular">
          <a :href="`https://wa.me/${contacts.whatsapp}`">
            {{ contacts.whatsapp }}
          </a>
          </span>
        </p>
      </div>

      <!--    email   -->
      <div class="q-mt-sm">
        <div class="q-mt-sm">
          <p class="product-card-title text-weight-bold">
            E-mail:
            <span class="text-weight-regular">
            <a :href="`mailto:${contacts.email}`">
              {{ contacts.whatsapp }}
            </a>
            </span>
          </p>
        </div>
      </div>

      <!--    address   -->
      <div class="q-mt-sm">
        <div class="q-mt-sm">
          <p class="product-card-title text-weight-bold">
            Адрес:
            <span class="text-weight-regular">
            {{ contacts.address }}
            </span>
          </p>
        </div>
      </div>
    </section>
  </div>
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
