<template>
  <div class="container my-4">
    <h3>' {{ this.$route.params.text }} ' 관련 상품 {{ result }}건</h3>
    <hr>
    <h3 class="title my-4">Product</h3>
    <hr>
    <div class="row col-12 my-4" v-for="(item, index) in search.items" :key="index">
      <div class="vertical col-12 col-sm-6 col-md-4 item" @click="onProductDetail(item.id)">
        <img class="product-img" :src="item.images" alt="">
        <h4 class="product-name mt-2">{{ item.name }}</h4>
        <hr>
        <h5 class="product-price">{{ addComma(item.price) }}원</h5>
        <p v-for="(spec, index) in item.descriptions" :key="index" class="product-des">{{ spec.category_description.name }} : {{ spec.content}}</p>
      </div>
    </div>

    <div class="button">
      <button type="button" class="my-4 btn btn-outline-secondary btn-lg" @click="$router.go(-1)">
        뒤로가기
      </button>
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf'
import { mapActions, mapState } from 'vuex'
export default {
  name: 'SearchProduct',
  methods: {
    ...mapActions('customer', ['getSearch']),
    addComma(num) {
      const regexp = /\B(?=(\d{3})+(?!\d))/g;
      return num.toString().replace(regexp, ',');
    },
    onProductDetail(cid) {
      this.$router.push({name: 'CustomerProduct', params: {cid: cid}}, () => {})
    },
  },
  computed: {
    ...mapState('customer', ['search']),
    result() {
      if ( this.search ) {
        return this.search.items.length
      }
      else {
        return 0
      }
    },

  },
  created() {
    this.getSearch(this.$route.params.text)
  }

}
</script>

<style scoped>
.item {
  cursor: pointer;
}

.product-img {
  height : 250px;
  width: auto
}

</style>