<template>
  <div class="container">
    <!-- This is Design Template of Product category -->
    <h3 class="mt-4">{{ datas.name }}</h3>
    <hr>
    <div v-for="(item, index) in datas.items" :key="index" class="row mt-4 item" @click="onRoute('CustomerProduct', item.id)">
      <div class="vertical col-12 col-sm-6 col-md-4">
        
        <img v-if="item.images.length == 0" class="product-img" src="@/assets/dummy-250.png" alt="">
        <img v-else class="product-img" :src="getImg(item.images)" alt="">

        <h4 class="product-name mt-2">{{ item.name }}</h4>
        <hr>
        <h5 class="product-price">{{ item.price }}원</h5>
        <span v-for="(spec, index) in item.descriptions" :key="index" class="product-des">{{spec.category_description.name}} : {{ spec.content}}</span>
      </div>
    </div>

  </div>
</template>

<script>
import SERVER from '@/api/drf'
export default {
    name: 'DesignTemplate.vue',
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
.product-img {
  border: 1px solid transparent;
  border-radius: 10px;
}

.product-des {
  background-color: #e9e9e9;
  padding: 5px;
  border-radius: 10px;
  margin-right: 10px;
}

.item {
  cursor: pointer;
}

@media screen and (max-width: 992px) {
  .product-img {
    width: 100%;
  }
  .product-name {
    font-size: 1rem;
  }
  .product-price {
    font-size: 1rem;
  }
  .product-des {
    font-size: 1rem;
  }
}

@media screen and (max-width: 576px) {
  .product-img {
    width: 100%;
  }
}
</style>