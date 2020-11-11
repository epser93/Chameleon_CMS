<template>
  <div>
    <!-- 대표 이미지 Carousel -->
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" v-if="carousels">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" :class="(index === 0) ? 'active' : ''" :data-slide-to="index"  v-for="(carousel, index) in carousels" :key="index"></li>
      </ol>
      <div class="carousel-inner">
          <div :class="(index === 0) ? 'active carousel-item' : 'carousel-item'"  v-for="(carousel, index) in carousels" :key="index">
            <img :src="'http://k3c205.p.ssafy.io'+carousel.image" class="d-block w-100" :alt="'main-image-'+index" @click="onClickWindows(carousel.url)">
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
      <div class="row justify-content-around mb-2">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image1">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image2">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image3">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image4">
      </div>
    </div>
    <!-- 이벤트 Carousel --> 
    <div class="container mb-5" v-if="events">
      <div class="row mb-4">
        <h2 class="mr-auto ml-auto">이벤트</h2>
      </div>
      <div id="eventCarouselIndicators" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#eventCarouselIndicators" :class="(index === 0) ? 'active' : ''" :data-slide-to="index"  v-for="(event, index) in events" :key="index"></li>
        </ol>
        <div class="carousel-inner">
          <div :class="(index === 0) ? 'active carousel-item' : 'carousel-item'"  v-for="(event, index) in events" :key="index">
            <img :src="'http://k3c205.p.ssafy.io'+event.thumbnail_image" class="d-block w-100" :alt="'main-image-'+index" @click="onDetail(event.id)">
          </div>
        </div>
        <a class="carousel-control-prev" href="#eventCarouselIndicators" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#eventCarouselIndicators" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Home',
  computed: {
    ...mapState('customer', ['carousels', 'events']),
  },
  methods: {
    ...mapActions('customer', ['getCarousels', 'getEvents']),
    onClickWindows(url) {
      if (url) {
        window.open(url) 
      }
    },
    onDetail(eid) {
      let routeData = this.$router.resolve({name:'CustomerEventDetail', params:{eid: eid}})
      window.open(routeData.href)
		},
  },
  created() {
    if (!this.$cookies.get("DontOpenNotice")) {
      window.open("http://localhost:8080/notice", "", "width=305,height=332,left=200,top=200")
    }
    this.getCarousels()
    this.getEvents()
  }
}
</script>

<style>
@media screen and (max-width: 500px) {
  h2 {
   font-size: 20px;
  }
}
</style>
