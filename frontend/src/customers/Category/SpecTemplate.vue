<template>
  <div class="container">
    <h3 class="mt-4">{{ datas.name }}</h3>
    <hr>
    <div class="row mt-4 mb-4 ml-4 item" v-for="(item, index) in datas.items" :key="index" @click="onRoute('CustomerProduct', item.id)">
      <div v-if="item.images.length == 0" class="col-12 col-md-5">
        <img src="@/assets/dummy-250.png" class="product-img" alt="">
      </div>
      <div v-else class="col-12 col-md-5">
        <img :src="getImg(item.images)" class="product-img" alt="">
      </div>
      <div class="row spec col-12 col-md-7 align-items-center justify-content-start">
        <div class="product-spec m-0">
          <h4 class="product-name">{{ item.name }}</h4>
          <h5 class="price">{{ addComma(item.price) }}원</h5>
          <p v-for="(spec, index) in item.descriptions" :key="index">{{spec.category_description.name}} : {{ spec.content}}</p>
        </div>
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
    },
    addComma(num) {
      const regexp = /\B(?=(\d{3})+(?!\d))/g;
      return num.toString().replace(regexp, ',');
    }
  },
}
</script>

<style scoped>
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

.spec {
  justify-content: center;
}
/* @media screen and (max-width: 960px) {
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
} */
@media screen and (max-width: 768px) {
  .product-img {
    width: 100%;
    height: auto;
  }

  .spec {
    margin-left: 20px;
  }
}
</style>