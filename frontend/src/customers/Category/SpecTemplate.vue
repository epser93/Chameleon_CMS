<template>
  <div class="container">
    <!-- This is Spec Template of Product category -->
    <h3 class="mt-4">{{ datas.name }}</h3>
    <hr>
    <!-- 상품 리스트 (연동후 for문으로 돌리기) -->
    <div class="row mt-4 mb-4 ml-4 item" v-for="(item, index) in datas.items" :key="index" @click="onRoute('CustomerProduct', item.id)">
      <div v-if="item.images.length == 0" class="col-5">
        <img src="@/assets/dummy-250.png" class="product-img" alt="">
      </div>
      <div v-else class="col-5">
        <img :src="getImg(item.images)" class="product-img" alt="">
      </div>
      <div class="col-7">
        <h4 class="product-name">{{ item.name }}</h4>
        <div class="product-spec m-0">
          <p v-for="(spec, index) in item.descriptions" :key="index">{{spec.category_description.name}} : {{ spec.content}}</p>
        </div>
        <p class="price">{{ item.price }}원</p>
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf'
export default {
  name: 'SpecTemplate',
  props: ['datas'],
  methods: {
    getImg(src) {
      for (let i=0; i<src.length; i++) {
        if (src[i].is_thumbnail === true) {
          return SERVER.domain + src[i].item_image.slice(56, src[i].item_image.length)
        } 
      }
      return '@/assets/250.png'
    },
    onRoute(name, id) {
      this.$router.push({name: name, params: {cid: id}}, () => {})
    }
  },
}
</script>

<style>
p {
  margin: 0;
}

.date {
  position: absolute;
  bottom: 0px;
}

.item {
  cursor: pointer;
}

@media screen and (max-width: 960px) {
  .product-img {
   width: 80%;
   height: auto;
  }
  .product-name {
   font-size: 1rem; 
   margin-bottom: 10px;
  }
  .product-spec {
    font-size: 1rem;
  }
  .price {
    position: relative;
    font-size: 1rem;
  }
}

@media screen and (max-width: 576px) {
  .product-spec {
    font-size: 0.5rem;
  }
  .product-name {
    margin-bottom: 5px;
  }
  .price {
    position: relative;
    font-size: 0.5rem;
  }
}
</style>