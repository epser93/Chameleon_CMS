<template>
  <div class="box container-fluid">
    <div class="row">
      <!-- col-md 이상일 때 나오는 왼쪽 세로 캐로우셀 -->
      <div class="d-none d-sm-none d-md-block col-2 px-0">
        <ol class="carousel-indicators-img mb-0" data-interval="false">
          <div class="direction column mt-5">
            <img v-for="(thumbnail, index) in thumbnails" :key="index" :src="getImage(thumbnail.item_image)" data-target="#carouselExampleCaptions" :data-slide-to="index" :class="(index === 0) ? 'active preview-img' : 'preview-img'" alt="">
          </div>
        </ol>
      </div>
      <!-- Carousel Image -->
      <div class="col-sm-12 col-md-5 mt-5 mr-auto ml-auto pl-0 pr-4">
        <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel" data-interval="false">
          <div class="carousel-inner">
            <!-- Image1 -->
            <div v-for="(thumbnail, index) in thumbnails" :key="index" :src="getImage(thumbnail.item_image)" :class="(index === 0) ? 'carousel-item active' : 'carousel-item'">
              <img :src="getImage(thumbnail.item_image)" class="inner-img d-block" alt="product image">
            </div>
          </div>
        </div>
      </div>
      <!-- col-sm일 때 나오는 하단 캐로우셀 -->
      <div class="d-block d-sm-block d-md-none col-12 mb-4">
        <ol class="carousel-indicators">
          <li v-for="(thumbnail, index) in thumbnails" :key="index" data-target="#carouselExampleCaptions" :data-slide-to="index" class="preview-btn"></li>
        </ol>
      </div>
      <!-- col-md 이상일 때 Item Info -->
      <div class="itm-info-md d-none d-sm-none d-md-block col-5">
        <div class="d-flex mt-5">
          <div class="column itm-info-box mr-auto ml-auto">
            <h3>{{ itemInfo.name }}</h3>
            <h5>{{ itemInfo.price }}원</h5>
            <div class="itm-info-detail">
              <p v-for="(spec, index) in itemInfo.descriptions" :key="index">{{ spec.category_description.name }} : {{ spec.content}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- col-sm일 때 Item Info -->
    <div class="item-info-sm d-block d-sm-block d-md-none col-12">
      <div class="item-info-sm-detail mx-1 row justify-content-between">
        <h4>판매가</h4>
        <h4>{{ itemInfo.price }}원</h4>
      </div>
    </div>
    <div class="d-block d-sm-block d-md-none col-12 column mx-2">
      <p v-for="(spec, index) in itemInfo.descriptions" :key="index">{{ spec.category_description.name }} : {{ spec.content}}</p> 
    </div>
    <!-- Item deatil image ara -->
    <div class="itm-detail mb-3">
      <div v-for="(detailImage, index) in detailImages" :key="index">
        <img :src="getImage(detailImage.item_image)" class="itm-detail-img d-block" alt="...">
      </div>
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf'
import {mapActions, mapState} from 'vuex'
export default {
  name: 'CarouselTemplate',
  props: ['itemInfo'],
  computed: {
    ...mapState('customer', ['thumbnails', 'detailImages'])
  },
  methods: {
    ...mapActions('customer', ['divideImage']),
    getImage(src) {
      return SERVER.domain + src.slice(56, src.length)
    }
  },
  watch: {
    'itemInfo' : function() {
      this.divideImage(this.itemInfo.images)
    }
  },
  created() {
    this.divideImage(this.itemInfo.images)
  }
}
</script>

<style scoped>
.carousel-indicators-img{
  width: 50px;
}

.preview-img {
  width: 50px;
  border: 1px solid transparent;
  border-radius: 10px;
  margin-bottom: 10px;
}

ol {
  height: 100%;
}

.itm-info-md {
  width: 320px;
  height: 500px;
  background-color: white;
  position: relative;
}

.carousel-item {
  min-height: 250px; 
}

.carousel-inner {
  margin-right: -50px;
}

.inner-img {
  max-width: 390px;
}

.itm-info-detail {
  width: 300px;
  height: 300px;
  border: 4px solid #f8f9fa;
  border-radius: 10px;
  padding: 10px;
  position: relative;
}

.itm-info-box {
  justify-content: center;
  flex-direction: column;
}

.bottom {
  width:100%;
  background:#8698b9;
}

.preview-btn {
  background-color: #4c4949;
}

.itm-detail-img {
  width: 100%;
}

@media screen and (max-width: 768px) {
  .itm-info {
    width: 100%;
    height: 500px;
    background-color: white;
    position: relative;
  }
  .item-info-sm {
    background-color: white;
  }
  .container-fluid {
    padding: 0;
  }
  .carousel-inner {
    margin-top: 0;
    margin-bottom: 40px;
  }
  img {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>