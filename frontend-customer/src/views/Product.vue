<template>
  <div class="box mt-5">
    <div class="row justify-content-around">
      <button type="button" class="btn btn-warning" @click="onRoute('DesignTemplate')">Design</button>
      <button type="button" class="btn btn-info" @click="onRoute('SpecTemplate')">Spec</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Product',
  methods: {
    onRoute(name) {
      this.$router.push({name: name}, () => {})
		},
  }
}
</script>

<style>
.box {
  height: 100px;
}
</style>