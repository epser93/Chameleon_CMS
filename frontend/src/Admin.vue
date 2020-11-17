<template>
  <div>
    <router-view/>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$ga.disable()
  }
}
</script>
