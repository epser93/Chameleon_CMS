<template>
  <div>
    <div class="container">
      <div class="row mt-4 mb-3">
        <h2 class="mr-auto ml-auto">대표 이미지</h2>
      </div>
    </div>

    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" v-if="carousels">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" :class="(index === 0) ? 'active' : ''" :data-slide-to="index"  v-for="(carousel, index) in carousels" :key="index"></li>
      </ol>
      <div class="carousel-inner">
          <div :class="(index === 0) ? 'active carousel-item' : 'carousel-item'"  v-for="(carousel, index) in carousels" :key="index">
            <img :src="'http://k3c205.p.ssafy.io'+carousel.image.slice(56)" class="d-block w-100" :alt="'main-image-'+index">
          </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    <!-- 추천 제품 리스트 -->
    <div class="container">
      <div class="row mt-4 mb-3">
        <h2 class="mr-auto ml-auto">추천 제품</h2>
      </div>
      <div class="row justify-content-around mb-2 product">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image1">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image2">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image3">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image4">
      </div>
    </div>

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Main',
  computed: {
    ...mapState('customer', ['carousels']),
  },
  methods: {
    ...mapActions('customer', ['getCarousels']),
  },
  created() {
    this.getCarousels()
  }
}
</script>

<style>
.carousel {
  width: 90%;
  margin: auto;
}

.product {
  width: 90%;
  margin: auto;
}

</style>