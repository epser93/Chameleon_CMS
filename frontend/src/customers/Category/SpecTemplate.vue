<template>
  <div class="container">
    <!-- This is Spec Template of Product category -->
    <h3 class="mt-4">선택 제품군 이름</h3>
    <hr>
    {{ datas }}
    <!-- 상품 리스트 (연동후 for문으로 돌리기) -->
    <div class="row mt-4 mb-4 ml-4">
      <div class="col-5">
        <img src="@/assets/250.png" class="product-img" alt="">
      </div>
      <div class="col-7">
        <h4 class="product-name">제품명</h4>
        <div class="product-spec m-0">
          <p>제품 사양1 - 가나다라마바사</p>
          <p>제품 사양2 - 가나다라마바사</p>
          <p>제품 사양3 - 가나다라마바사</p>
          <p>제품 사양4 - 가나다라마바사</p>
          <p>제품 사양5 - 가나다라마바사</p>
        </div>
        <p class="date">제품 출시일: 2020-00-00</p>
      </div>
    </div>
    <hr>
    <div class="row mt-4 mb-4 ml-4">
      <div class="col-5">
        <img src="@/assets/250.png" class="product-img" alt="">
      </div>
      <div class="col-7">
        <h4 class="product-name">제품명</h4>
        <div class="product-spec m-0">
          <p>제품 사양1 - 가나다라마바사</p>
          <p>제품 사양2 - 가나다라마바사</p>
          <p>제품 사양3 - 가나다라마바사</p>
          <p>제품 사양4 - 가나다라마바사</p>
          <p>제품 사양5 - 가나다라마바사</p>
        </div>
        <p class="date">제품 출시일: 2020-00-00</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SpecTemplate',
  props: ['datas']
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
  .date {
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
  .date {
    position: relative;
    font-size: 0.5rem;
  }
}
</style>