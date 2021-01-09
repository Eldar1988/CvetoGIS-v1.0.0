<template>
<section>
  <div class="row">
    <div class="col-12 col-md-12 col-lg-3">

    </div>
  </div>
</section>
</template>

<script>
export default {
  name: "gisReasons",
  computed: {
    reasons() {
      return this.$store.getters.getReasons
    }
  }
}
</script>

<style>

</style>
