<template>
  <div class="fullscreen bg-primary text-white text-center q-pa-md flex flex-center">
    <div>
      <div style="font-size: 20vh">
        404
      </div>

      <div class="text-h6" style="opacity:.9">
        Извините, но запрашиваемая вами страница не найдена
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
</template>

<script>
export default {
  name: 'Error404'
}
</script>
