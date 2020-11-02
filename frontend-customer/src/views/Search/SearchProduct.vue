<template>
  <div class="container my-4">
    <h3 class="title my-4">Product</h3>
    <hr>
    <div class="row col-12 my-4">
      <div class="vertical col-12 col-sm-6 col-md-4">
        <img class="product-img" src="@/assets/250.png" alt="">
        <h4 class="product-name mt-2">제품명</h4>
        <hr>
        <h5 class="product-price">제품가격</h5>
        <p class="product-des">간단한 설명</p>
      </div>
      <div class="vertical col-12 col-sm-6 col-md-4">
        <img class="product-img" src="@/assets/250.png" alt="">
        <h4 class="product-name mt-2">제품명</h4>
        <hr>
        <h5 class="product-price">제품가격</h5>
        <p class="product-des">간단한 설명</p>
      </div>
      <div class="vertical col-12 col-sm-6 col-md-4">
        <img class="product-img" src="@/assets/250.png" alt="">
        <h4 class="product-name mt-2">제품명</h4>
        <hr>
        <h5 class="product-price">제품가격</h5>
        <p class="product-des">간단한 설명</p>
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
export default {
  name: 'SearchProduct',

}
</script>

<style>

</style>