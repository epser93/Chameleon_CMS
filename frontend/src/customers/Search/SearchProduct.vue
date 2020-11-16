<template>
  <div class="container my-4">
    <h3>' {{ this.$route.params.text }} ' 관련 상품 {{ result }}건</h3>
    <hr>
    <h3 class="title my-4">Product</h3>
    <hr>
    <div class="row my-4">
      <div v-for="(item, index) in search.items" :key="index" class="col-sm-12 col-md-6 col-lg-4 item" @click="onProductDetail(item.id)">
<<<<<<< HEAD
        <img class="product-img" :src="item.images[0].item_image" alt="" style="width: 100%">
=======
        <img class="product-img justify-content-center" :src="getImg(item.images)" alt="">
>>>>>>> fb4df6a8ac9e15dfb391bba5a8fdc5dd88360600
        <h4 class="product-name mt-2">{{ item.name }}</h4>
        <hr>
        <h5 class="product-price">{{ addComma(item.price) }}원</h5>
        <p v-for="(spec, index) in item.descriptions" :key="index" class="product-des">{{ spec.category_description.name }} : {{ spec.content}}</p>
      </div>
    </div>
    <div class="row justify-content-center">
      <button type="button" class="my-4 btn btn-outline-secondary btn-md" @click="$router.go(-1)">
        뒤로가기
      </button>
    </div>
  </div>
</template>

<script>
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
    getImg(src) {
      for (let i=0; i<src.length; i++) {
        if (src[i].is_thumbnail) {
          return src[i].item_image
        }
      }
      return '@/assets/250.png'
    }
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
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
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