<template>
  <div class="container">
    <!-- This is Design Template of Product category -->
    <h3 class="mt-4">선택 제품군 이름</h3>
    <hr>
    {{ datas }}
    <!-- 상품 리스트 (연동후 for문으로 돌리기) -->
    <div class="row col-12 mt-4">
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

  </div>
</template>

<script>
export default {
    name: 'DesignTemplate.vue',
    props: ['datas']
}
</script>

<style>
.product-img {
  border: 1px solid transparent;
  border-radius: 10px;
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