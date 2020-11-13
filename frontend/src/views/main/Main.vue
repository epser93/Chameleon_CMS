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
    <div class="container" v-if="products">
      <div class="row mt-4 mb-3">
        <h2 class="mr-auto ml-auto">추천 제품</h2>
      </div>
      <div class="row justify-content-around mb-2 product">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image3"  v-for="(product, index) in products" :key="index">
        <!-- <img :src="'http://k3c205.p.ssafy.io'+product.item.images[0].item_image.slice(56)" class="col-6 col-lg-3 mb-4" :alt="'recommand product image' + index"> -->
        <!-- <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image2">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image3">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image4"> -->
      </div>
    </div>
    <!-- 추천 제품 모달 -->
    <!-- <div class="modal" tabindex="-1" id="authorityModal">
      <div class="modal-dialog" v-if="authorityModalUser">
        <div class="modal-content">
          <div class="modal-header" >
            <h5 class="modal-title">접근권한 부여</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div>
              <p class="tag">부서</p>
              <p>{{ authorityModalUser.department.name }}</p>
            </div>
            <hr>
            <div>
              <p class="tag">이름</p>
              <p>{{ authorityModalUser.first_name }}</p>
            </div>
            <hr>
            <div>
              <p class="tag">아이디</p>
              <p>{{ authorityModalUser.username }}</p>
            </div>
            <hr>
            <div> 
              <p class="tag">권한</p>
              <div class="row justify-content-center ml-1">
                <label class="chkbox-label">
                  <input type="checkbox" :value="authorityModalUser.is_eventer" v-model="authorityModalUser.is_eventer">
                  Event
                </label>
                <label class="chkbox-label">
                  <input type="checkbox" :value="authorityModalUser.is_logger" v-model="authorityModalUser.is_logger">
                  Log
                </label>
                <label class="chkbox-label">
                  <input type="checkbox" :value="authorityModalUser.is_producter" v-model="authorityModalUser.is_producter">
                  Product
                </label>
                <label class="chkbox-label">
                  <input type="checkbox" :value="authorityModalUser.is_marketer" v-model="authorityModalUser.is_marketer">
                  Main + Notice
                </label>
              </div>
            </div>
          </div>
          <div class="modal-footer justify-content-center">
            <button type="button" class="btn btn-primary" @click="onRoute('User'), giveAuthority()">권한 수정</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">취소</button>
          </div>
        </div>
      </div>
    </div> -->

  </div>
</template>

<script>
// import $ from 'jquery'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Main',
  computed: {
    ...mapState('customer', ['carousels', 'products']),
    ...mapState('main', ['products'])
  },
  methods: {
    ...mapActions('customer', ['getCarousels']),
    ...mapActions('main', ['getProducts'])
  },
  created() {
    this.getCarousels()
    this.getProducts()
  }
}
</script>

<style>
.carousel {
  width: 90%;
  margin: auto;
}
</style>