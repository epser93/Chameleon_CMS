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
            <img :src="carousel.image" class="d-block w-100" :alt="'main-image-'+index">
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
    <div class="container recommand-products" v-if="products">
      <div class="row mt-4 mb-3">
        <h2 class="mr-auto ml-auto">추천 제품</h2>
      </div>
      <div class="row justify-content-around mb-2 product">
        <img :src="product.item.thumbnail" class="col-6 col-lg-3 mb-4" :alt="'recommand product image' + index" v-for="(product, index) in products" :key="index" @click="onModal(product)">
      </div>
    </div>
    <!-- 추천 제품 모달 -->
    <div class="modal" tabindex="-1" id="recommendModal">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable" v-if="modalProduct">
        <div class="modal-content">
          <div class="modal-header" >
            <h5 class="modal-title">추천 상품 변경</h5>
          </div>
          <div class="modal-body">
            <div class="container">
              <h4 class="product-name">현재 상품 : {{ modalProduct.item.name }}</h4>
              <hr>
              <div class="input-group mb-3 justify-content-center">
                <select name="" id="" v-model="selectedCategory">
                  <option value="all">All</option>
                  <option v-for="(category, index) in categories" :key="index" :value="category.name">{{category.name}}</option>
                </select>
                <input type="text" class="form-control" placeholder="제품 검색" v-model="searchedProduct" @keypress.enter="changeSearchToggle()">
                <div class="input-group-append">
                  <button class="btn btn-secondary ml-0" type="button" id="button-addon2" @click="changeSearchToggle()">검색</button>
                </div>
              </div>
              <table class="table">
                <thead>
                  <tr class="top-tr">
                    <th scope="col">카테고리</th>
                    <th scope="col">상품명</th>
                    <th scope="col">변경</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="user-infos" v-for="(product, index) in allProducts" :key="index">
                    <td>{{ product.category.name }}</td>
                    <td>{{ product.name }}</td>
                    <td v-if="nowProducts.includes(product.id)"><button type="button" class="btn btn-danger btn-sm m-0" disabled>추천 상품</button></td>
                    <td v-else><button type="button" class="btn btn-warning btn-sm m-0" @click="onUpdate(product.id)">수정</button></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="modal-footer justify-content-right">
            <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="SET_ALL_PRODUCTS('')">취소</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import $ from 'jquery'
import { mapState, mapActions, mapMutations } from 'vuex'

export default {
  name: 'Main',
  data() {
    return {
      modalProduct: '',
      selectedCategory: 'all',
      searchedProduct: '',
      searchToggle : false,
    }
  },
  computed: {
    ...mapState('customer', ['carousels']),
    ...mapState('main', ['products', 'allProducts']),
    ...mapState('category', ['categories']),
    nowProducts() {
      const ids = []
      for(let i=0; i<this.products.length; i++) {
        ids.push(this.products[i].item.id)
      }
      return ids
    }
  },
  watch: {
    categories(val) {
      const tmpCategory = []
      for(let i=0; i<val.length; i++) {
        if(val[i].is_active) {
          tmpCategory.push(val[i])
        }
      }
     this.productCategories = tmpCategory
    },
    selectedDepartment: function() {
      this.getAllProducts({ category : this.selectedCategory, product : ''})
    },
    searchToggle: function() {
      this.getAllProducts({ category : this.selectedCategory, product: this.searchedProduct })
      this.searchedProduct = ''
    }
  },
  methods: {
    ...mapActions('customer', ['getCarousels']),
    ...mapActions('main', ['getProducts', 'putProduct', 'getAllProducts']),
    ...mapMutations('main', ['SET_ALL_PRODUCTS']),
    onModal(product) {
      this.modalProduct = product
      $('#recommendModal').modal('show')
    },
    onUpdate(pid) {
      if (confirm("추천 상품을 변경하시겠습니까?") == true){
        const putData = {
          priority: this.modalProduct.priority,
          is_active: "True",
          id: pid
        }
        this.putProduct({ pid: this.modalProduct.id, putData: putData })
        $('#recommendModal').modal('hide')
      }
    },
    changeSearchToggle() {
      this.searchToggle = !this.searchToggle
    },
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

.recommand-products {
  cursor: pointer;
}
</style>