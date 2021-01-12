<template>
<div class="text-center">
  <q-btn
    outline
    :color="color"
    :padding="padding"
    icon="shopping_cart"
    class=""
    :flat="flat"
    to="/cart"
  >
    <q-badge color="secondary" floating>{{ cartLen }}</q-badge>
  </q-btn>
</div>
</template>

<script>
export default {
  name: "gisCartIcon",
  props: {
    color: {
      type: String,
      default: 'white'
    },
    padding: {
      type: String,
      default: '10px'
    },
    flat: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      cartLen: 0
    }
  },
  mounted() {
    if(localStorage.getItem('cart') !== null) {
      this.cartLen = JSON.parse(localStorage.cart).length
    }
    // Обновляем количество товаров
    this.$root.$on('updateCart', () => this.cartLen = JSON.parse(localStorage.cart).length)
  }
}
</script>

<style lang="sass">

</style>
