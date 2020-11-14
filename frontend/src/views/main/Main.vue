<template>
  <div>
    <div class="container">
      <div class="row mt-4 mb-3">
        <h2 class="mr-auto ml-auto">대표 이미지</h2>
      </div>
    </div>

    {{ allProducts }}

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
        <img :src="'http://k3c205.p.ssafy.io/'+product.item.thumbnail" class="col-6 col-lg-3 mb-4" :alt="'recommand product image' + index" v-for="(product, index) in products" :key="index" @click="onModal(product)">
      </div>
    </div>
    <!-- 추천 제품 모달 -->
    <div class="modal" tabindex="-1" id="recommendModal">
      <div class="modal-dialog" v-if="product">
        <div class="modal-content">
          <div class="modal-header" >
            <h5 class="modal-title">추천 상품 변경</h5>
          </div>
          <div class="modal-body">
            <div class="container">
              <h4 class="product-name">현재 상품 : {{ product.item.name }}</h4>
              <div class="row mt-4 mb-4 ml-4">
                <!-- <div class="input-group mb-3 justify-content-center">
                  <select name="" id="" v-model="selectedDepartment">
                    <option value="all">All</option>
                    <option v-for="(department, index) in departments" :key="index" :value="department.name">{{department.name}}</option>
                  </select>
                  <input type="text" class="form-control" placeholder="회원 검색" v-model="searchedName" @keypress.enter="changeSearchToggle()">
                  <div class="input-group-append">
                    <button class="btn btn-secondary ml-0" type="button" id="button-addon2" @click="changeSearchToggle()">검색</button>
                  </div>
                </div> -->
              </div>
            </div>
          </div>
          <div class="modal-footer justify-content-center">
            <button type="button" class="btn btn-primary">변경</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">취소</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import $ from 'jquery'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Main',
  data() {
    return {
      product: ''
    }
  },
  computed: {
    ...mapState('customer', ['carousels']),
    ...mapState('main', ['products', 'allProducts'])
  },
  methods: {
    ...mapActions('customer', ['getCarousels']),
    ...mapActions('main', ['getProducts','getAllProducts']),
    onModal(product) {
      this.product = product
      $('#recommendModal').modal('show')
    },
  },
  created() {
    this.getCarousels()
    this.getProducts()
    // this.getAllProducts()
  }
}
</script>

<style>
.carousel {
  width: 90%;
  margin: auto;
}
</style>