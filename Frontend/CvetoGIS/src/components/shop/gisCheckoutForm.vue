<template>
  <div class="q-mt-xl">
    <div class="row q-mt-md">
      <!--      Форма заказа   -->
      <div class="col-12 col-lg-6" style="padding: 5px">
        <q-card bordered class="shadow-0 q-pa-sm rounded">
          <h3 class="q-py-lg text-center text-h6 text-weight-bold">Форма заказа</h3>
          <div class="row">
            <!--            Имя заказчика   -->
            <div class="col-12 col-md-6 q-pa-sm">
              <q-input rounded class="shadow-lt rounded-35 q-pl-md" borderless v-model="bayerName" label="Ваше имя*"/>
            </div>
            <!--            ===============   -->
            <!--            Номер телефона заказчика   -->
            <div class="col-12 col-md-6 q-pa-sm">
              <q-input type="number" rounded class="shadow-lt rounded-35 q-pl-md" borderless v-model="bayerPhone"
                       label="Ваш номер телефона*"/>
            </div>
            <!--             ==========================   -->
            <!--            Чекбоксы   -->
            <div class="col-12 col-md-6 q-pa-sm">
              <q-checkbox v-model="customerIsTheRecipient" label="Я сам получу цветы"/>
            </div>
            <div class="col-12 col-md-6 q-pa-sm">
              <q-checkbox v-model="findOutTheAddress" label="Узнать адрес у получателя" @click="findAddress"/>
            </div>
            <!--            ======================   -->
            <!--            Адрес доставки   -->
            <q-slide-transition>
              <div class="col-12 q-px-sm" v-if="!findOutTheAddress">
                <q-input rounded class="shadow-lt rounded-35 q-pl-md" borderless v-model="address"
                         label="Адрес доставки*"/>
              </div>
            </q-slide-transition>
            <!--            ==========================   -->
            <q-separator class="q-mt-lg"/>
            <!--            Данные получателя   -->
            <q-slide-transition>
              <div v-if="!customerIsTheRecipient" class="col-12 q-mt-lg">
                <div class="row">
                  <!--            Имя получателя   -->
                  <div class="col-12 col-md-6 q-pa-sm">
                    <q-input rounded class="shadow-lt rounded-35 q-pl-md" borderless v-model="receiverName"
                             label="Имя получателя*"/>
                  </div>
                  <!--                  ======================   -->
                  <!--                  Телефон получателя   -->
                  <div class="col-12 col-md-6 q-pa-sm">
                    <q-input type="number" rounded class="shadow-lt rounded-35 q-pl-md" borderless
                             v-model="receiverPhone" label="Телефон получателя*"/>
                  </div>
                  <!--                  ============================= -->
                </div>
              </div>
            </q-slide-transition>

            <!--            Дата и время доставки   -->
            <div class="col-12 q-pa-sm">
              <p class="text-center text-grey-8 q-pt-md">Дата и время доставки*</p>
              <q-input class="shadow-lt rounded-35 q-px-md q-mt-sm" borderless v-model="date" rounded>
                <template v-slot:prepend>
                  <q-icon name="event" class="cursor-pointer">
                    <q-popup-proxy transition-show="scale" transition-hide="scale">
                      <q-date v-model="date" mask="DD-MM-YYYY время HH:mm" navigation-min-year-month="2020/01" today-btn
                              title="Дата доставки" :locale="myLocale">
                        <div class="row items-center justify-end">
                          <q-btn v-close-popup label="Ок" color="primary" flat/>
                        </div>
                      </q-date>
                    </q-popup-proxy>
                  </q-icon>
                </template>

                <template v-slot:append>
                  <q-icon name="access_time" class="cursor-pointer">
                    <q-popup-proxy transition-show="scale" transition-hide="scale">
                      <q-time v-model="date" mask="DD-MM-YYYY время HH:mm" format24h>
                        <div class="row items-center justify-end">
                          <q-btn v-close-popup label="Ok" color="primary" flat/>
                        </div>
                      </q-time>
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
              <p class="small text-center text-secondary q-pt-md">Доставка возможна не ранее, чем через час после
                оформления заказа</p>

            </div>
            <!--            =========================   -->
            <!--            Открытка   -->
            <div class="col-12 q-pa-sm">
              <q-checkbox v-model="postCard" label="Добавить открытку"/>
            </div>
            <q-slide-transition>
              <div class="col-12 q-pa-sm" v-if="postCard">
                <q-input type="textarea" rounded class="shadow-lt rounded-35 q-pl-md" borderless v-model="postCardText"
                         label="Текст на открытке"/>
              </div>
            </q-slide-transition>
            <!--            ====================   -->
          </div>
        </q-card>
      </div>
      <!--      =====================   -->
      <!--      Детали заказа   -->
      <div class="col-12 col-lg-6" style="padding: 5px">
        <q-card bordered class="shadow-0 q-pa-sm rounded">
          <q-stepper
            v-model="step"
            ref="stepper"
            color="primary"
            animated
          >
            <q-step
              :name="1"
              title="Детали заказа"
              icon="receipt_long"
              :done="step > 1"
            >
              <div class="steep-1">
                <h4 class="text-subtitle1 text-weight-bold">Общая сумма заказа: {{ getSum() }} тенге</h4>
                <!--          Доставка   -->
                <q-toolbar class="text-dark q-mt-md">
                  <q-toolbar-title class="text-h6 text-center">
                    Доставка
                  </q-toolbar-title>
                </q-toolbar>
                <h4 class="text-subtitle1 q-mt-sm">Адрес доставки: {{ city }},
                  {{ findOutTheAddress ? `позвонить и уточнить у получателя` : address }}</h4>
                <q-option-group
                  :options="deliveries"
                  label="Notifications"
                  type="radio"
                  v-model="deliveryType"
                />
                <q-separator class="q-my-sm"/>
                <h4 class="text-subtitle1">Имя получателя: {{ customerIsTheRecipient ? bayerName : receiverName }}</h4>
                <q-separator class="q-my-sm"/>
                <h4 class="text-subtitle1">Телефон получателя: {{
                    customerIsTheRecipient ? bayerPhone : receiverPhone
                  }}</h4>
                <q-separator class="q-my-sm"/>
                <h4 class="text-subtitle1">Дата и время доставки: {{ date }}</h4>
                <!--          ===================   -->
              </div>
            </q-step>

            <q-step
              :name="2"
              title="Оплата"
              icon="payments"
              :done="step > 2"
            >
              <div class="steep-2">
            <!--          Оплата   -->
            <h4 class="text-subtitle1 q-mt-lg">Выберите удобный для Вас способ оплаты</h4>
            <h4 class="text-subtitle1 text-weight-bold">Общая сумма к оплате: {{ getSum() }} тенге</h4>
            <div class="pay-methods q-mt-xl">
              <q-card
                v-for="payment in payments"
                :key="payment.id"
                class="q-pa-sm shadow-lt text-center rounded-35 q-mt-lg"
              >
                <h4 class="text-subtitle1 q-pa-sm" style="line-height: 1">{{ payment.text }}</h4>
                <q-img :src="payment.image" contain
                       style="height: 50px; object-fit: contain">
                </q-img>
                <q-btn
                  label="Выбрать"
                  color="primary"
                  rounded
                  class="q-mt-sm text-weight-bold q-px-md"
                  unelevated
                  @click="addNewOrder(payment.id)"
                  :loading="loadingNewOrder"
                />
              </q-card>
            </div>
            <!--          ===================   -->
              </div>
            </q-step>
            <template
              v-if="accessToPay"
              v-slot:navigation
              class="q-mt-lg"
            >
              <q-stepper-navigation class="text-center q-mt-sm">
                <q-btn v-if="step < 2" icon-right="forward" rounded class="q-px-md q-py-sm text-weight-bold shadow-lt" @click="$refs.stepper.next()" color="primary" :label="step === 2 ? '' : 'Перейти к оплате'" />
                <q-btn v-if="step > 1" flat color="primary" class="q-px-md q-py-sm text-weight-bold" @click="$refs.stepper.previous()" label="Назад" />
              </q-stepper-navigation>
            </template>
          </q-stepper>
        </q-card>
      </div>
      <!--      ======================    -->
    </div>
  </div>
</template>

<script>
export default {
  name: "gisCheckoutForm",
  props: {
    sum: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      bayerName: '',
      bayerPhone: '',
      address: '',
      customerIsTheRecipient: false,  // Заказчик - получатель
      findOutTheAddress: false,   // Узнать адрес у полчателя
      receiverName: '', // Имя получателя
      receiverPhone: '', // Телефон получателя
      date: '', // Дата доставки
      postCard: false,
      postCardText: '',
      city: '',
      deliveries: [],
      deliveryType: {},
      myLocale: {
        daysShort: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
        days: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
        months: ['Янв', 'Веф', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
        monthsShort: ['Янв', 'Веф', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
      },
      step: 1,
      payments: [],
      loadingNewOrder: false
    }
  },
  computed: {
    accessToPay()  {
      return (this.bayerName || this.receiverName) && (this.bayerPhone || this.receiverPhone) && (this.date) && (this.address || this.findOutTheAddress)
    }
  },
  watch: {
    step() {
      this.loadPaymentMethods()
    }
  },
  methods: {
    findAddress() {
      if (this.findOutTheAddress) {
        this.address = 'Позвонить и узнать у получателя'
      }
    },
    getSum() {
      if (typeof (this.deliveryType) !== "object") {
        return this.sum + parseInt(this.deliveryType)
      }
      return this.sum
    },
    async loadPaymentMethods() {
      this.payments = await this.$axios.get(`${this.$store.getters.getServerURL}/orders/payments/`)
      .then(({data}) => {
        return data
      })
    },
    async addNewOrder(paymentID) {
      let order = {}
      let cart = JSON.parse(localStorage.cart)
      let quantities = []
      let products = []
      let sum = 0
      cart.forEach((item) => {
        quantities.push(item.quantity)
        products.push(item.title)
        let itemSum = parseInt(item.price) * item.quantity
        sum += itemSum
      })
      this.loadingNewOrder = true
      order.city = JSON.parse(localStorage.city).id
      order.payment = paymentID
      order.name = this.bayerName
      order.phone = this.bayerPhone
      order.receiver_name = this.receiverName
      order.receiver_phone = this.receiverPhone
      order.address = this.address
      order.bayer_is_receiver = this.customerIsTheRecipient
      order.delivery_date = this.date
      order.quantities = quantities
      order.products = products
      order.order_sum = sum
      order.postcard = this.postCardText

      await fetch(`${this.$store.getters.getServerURL}/`)
    }
  },
  created() {
    this.city = JSON.parse(localStorage.getItem('city')).title
    let deliveries = JSON.parse(localStorage.getItem('city')).deliveries
    deliveries.forEach((item) => {
      let delivery = {}
      let value = item.price > 0 ? `(доставка ${item.price} тенге)` : '(бесплатная доставка)'
      delivery.label = `${item.title} ${value}`
      delivery.value = item.price
      this.deliveries.push(delivery)
    })
    this.getSum()
  },
}
</script>

<style scoped>

</style>
