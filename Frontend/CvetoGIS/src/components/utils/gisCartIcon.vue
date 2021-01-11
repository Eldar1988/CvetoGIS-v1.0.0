<template>
<div class="text-center">
  <q-btn
    round outline
    :color="color"
    :padding="padding"
    icon="shopping_cart"
    class="shadow-1"
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
