<template>
  <div>
    <img src="@/assets/aboutus/ALCC176.jpg" alt="">
    <div class="year">
      <img src="@/assets/aboutus/20201114_173123_1.png" alt="">
      <img src="@/assets/aboutus/20201114_173123_2.png" alt="">
      <img src="@/assets/aboutus/20201114_173123_3.png" alt="">
      <img src="@/assets/aboutus/20201114_173123_4.png" alt="">
      <img src="@/assets/aboutus/20201114_173123_5.png" alt="">
      <img src="@/assets/aboutus/20201114_173123_6.png" alt="">
      <img src="@/assets/aboutus/20201114_173123_7.png" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: 'About',
  created() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
}
</script>

<style scoped>

img {
  width: 100%;
}

.year {
  width: 80%;
  margin: auto;
}

</style>