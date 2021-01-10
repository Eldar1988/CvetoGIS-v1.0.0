<template>
<q-page>
  <div class="fullscreen bg-primary text-white text-center q-pa-md flex flex-center">
    <div>
      <div style="font-size: 5vh" class="text-weight-bold">
        Спасибо!
      </div>

      <div class="text-h6" style="opacity:.9">
        Мы свяжемся с Вами в течении 10 минут
      </div>

      <q-btn
        class="q-mt-xl q-px-md q-py-sm text-weight-bold"
        color="white"
        text-color="secondary"
        unelevated
        to="/"
        icon="home"
        label="На главную"
        rounded
      />
    </div>
  </div>
</q-page>
</template>

<script>
export default {
  name: "CallBackThanks"
}
</script>

<style scoped>

</style>
