<template>
  <q-card
    class="q-pa-sm rounded shadow-lt"
    style="min-height: 100%; display: flex; justify-items: center; min-width: 100%"
  >
    <div class="row relative-position" style="align-items: center; width: 100%">
      <div class="col-4">
        <q-img :src="product.image" class="rounded" style="height: 125px; object-fit: cover"></q-img>
      </div>
      <div class="col-8 q-pa-sm">
        <p class="text-weight-bold ellipsis">{{ product.title }}</p>
        <q-separator style="margin: 5px 0"/>
        <p
          class="text-weight-bold"
          style="font-size: 18px"
        >
          {{ getPrice(product.price) }}
          <q-icon :name="priceIcon"/>
          <span v-if="product.old_price" style="font-size: 14px; margin-left: 10px; text-decoration: line-through">{{
              getPrice(product.old_price)
            }}
          </span>
        </p>
        <!--        Кнопки   -->
        <div class="quntity q-mt-sm">
          <q-btn
            outlined round
            color="primary"
            @click="quantityMinus(product.id)"
            size="sm"
            class="q-mr-sm"
          >-
          </q-btn>
          {{ product.quantity }}
          <q-btn
            outlined round
            color="primary"
            @click="quantityPlus(product.id)"
            size="sm"
            class="q-ml-sm"
          >+
          </q-btn>
          <q-btn
            color="dark"
            round
            size="sm"
            class="q-ml-lg"
            @click="delCartItem(product.id)"
            title="Удалить?"
            icon="mdi-trash-can-outline"
            style="position: absolute; bottom: 0; right: 0"
          />
        </div>
        <!--        ==============   -->
      </div>
    </div>
  </q-card>
</template>

<script>
export default {
  name: "gisCartItem",
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
    }
  },
  computed: {
    // Иконка валюты
    priceIcon() {
      return this.$store.getters.getCurrentCurrency.icon
    }
  },
  methods: {
    reverseData() {
      this.newData.reverse()
    },
    // Меняем количество товара в корзине
    quantityPlus(id) {
      let items = JSON.parse(localStorage.cart)
      items.forEach((item) => {
        if (item.id === id) {
          item.quantity++
        }
      })
      localStorage.setItem('cart', JSON.stringify(items))
      this.$root.$emit('updateCart')
    },
    quantityMinus(id) {
      let items = JSON.parse(localStorage.cart)
      items.forEach((item) => {
        if (item.id === id) {
          if (item.quantity > 1) {
            item.quantity--
          }
        }
      })
      localStorage.setItem('cart', JSON.stringify(items))
      this.$root.$emit('updateCart')
    },

    // Удаляем товар из корзины
    delCartItem(id) {
      let items = JSON.parse(localStorage.cart)
      items.forEach((item) => {
        if (item.id === id) {
          let itemIndex = items.indexOf(item)
          console.log(itemIndex)
          items.splice(itemIndex, 1)
        }
      })
      localStorage.setItem('cart', JSON.stringify(items))
      this.$root.$emit('updateCart')
    },

    // Получаем цену (форматированная и в валюте)
    getPrice(price) {
      let course = this.$store.getters.getCurrentCurrency.value
      let newPrice = price / parseInt(course)
      newPrice = Math.ceil(newPrice)
      newPrice = newPrice.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
      return newPrice
    },
  },
}
</script>

<style scoped>

</style>
