<template>
  <div>
    <!-- 대표 이미지 Carousel -->
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" v-if="carousels">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" :class="(index === 0) ? 'active' : ''" :data-slide-to="index"  v-for="(carousel, index) in carousels" :key="index"></li>
      </ol>
      <div class="carousel-inner">
          <div :class="(index === 0) ? 'active carousel-item' : 'carousel-item'"  v-for="(carousel, index) in carousels" :key="index">
            <img :src="carousel.image" class="d-block w-100" :alt="'main-image-'+index" @click="onClickWindows(carousel.url)">
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
      <div class="row mb-4 justify-content-around mb-2 mr-4 ml-4 product">
        <div v-for="(product, index) in mainItems" :key="index" @click="onRoute(product.item.id)">
          <img class="recommand-img" :src="product.item.thumbnail" :alt="'recommand product image'+index">
          <div class="text-center">
            <p>{{ product.item.name }}</p>
          </div>
        </div>
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
            <img :src="event.thumbnail_image" class="d-block w-100" :alt="'main-image-'+index" @click="onDetail(event.id)">
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
    ...mapState('customer', ['mainItems', 'carousels', 'events']),
  },
  methods: {
    ...mapActions('customer', ['getMainItems', 'getCarousels', 'getEvents']),
    onClickWindows(url) {
      if (url) {
        window.open(url) 
      }
    },
    onRoute(cid) {
      this.$router.push({name: 'CustomerProduct', params: {cid: cid}})
    },
    onDetail(eid) {
      let routeData = this.$router.resolve({name:'CustomerEventDetail', params:{eid: eid}})
      window.open(routeData.href)
		},
  },
  created() {
    if (!this.$cookies.get("DontOpenNotice")) {
      window.open("https://chameleon.gq/notice", "", "width=305,height=332,left=200,top=200")
    }
    this.getMainItems()
    this.getCarousels()
    this.getEvents()
  }
}
</script>

<style>
.recommand-img {
  width: auto;
  height: 200px;
}

@media screen and (max-width: 500px) {
  h2 {
   font-size: 20px;
  }
}
</style>
