<template>
  <div class="container my-4">
    <h3>' {{result}} ' 검색결과 {{100}}건</h3>
    <hr>

    <h3 class="title my-4">Product</h3>
    <hr>
    <div class="row col-12 my-4">
      <div class="column col-12 col-sm-6 col-md-4 mb-4">
        <img class="product-img" src="@/assets/250.png" alt="">
        <h4 class="product-name mt-2">제품명</h4>
        <hr>
        <h5 class="product-price">제품가격</h5>
        <p class="product-des">간단한 설명</p>
      </div>
      <div class="column col-12 col-sm-6 col-md-4 mb-4">
        <img class="product-img" src="@/assets/250.png" alt="">
        <h4 class="product-name mt-2">제품명</h4>
        <hr>
        <h5 class="product-price">제품가격</h5>
        <p class="product-des">간단한 설명</p>
      </div>
      <div class="column col-12 col-sm-6 col-md-4 mb-4">
        <img class="product-img" src="@/assets/250.png" alt="">
        <h4 class="product-name mt-2">제품명</h4>
        <hr>
        <h5 class="product-price">제품가격</h5>
        <p class="product-des">간단한 설명</p>
      </div>
    </div>

    <div class="button">
      <button type="button" class="my-4 btn btn-outline-secondary btn-lg" @click="onRoute('SearchProduct')">
        관련 상품 더 보기
      </button>
    </div>

    <h3 class="title my-4">EVENT</h3>
    <hr>

    <div class="row my-4 justify-content-around">
      <div class="col-sm-12 col-md-8">
        <img src="https://picsum.photos/600/250" class="event-img" alt="">
      </div>
      <div class="col-sm-12 col-md-4">
        <h4 class="event-name">이벤트 B</h4>
        <div class="column">
          <p class="event-des">이벤트 설명</p>
          <p class="date">기간: 2020-00-00 ~ 2020-00-00</p>
        </div>
      </div>
    </div>
    <hr>
    <div class="row my-4 justify-content-around">
      <div class="col-sm-12 col-md-8">
        <img src="https://picsum.photos/600/250" class="event-img" alt="">
      </div>
      <div class="col-sm-12 col-md-4">
        <h4 class="event-name">이벤트 B</h4>
        <div class="column">
          <p class="event-des">이벤트 설명</p>
          <p class="date">기간: 2020-00-00 ~ 2020-00-00</p>
        </div>
      </div>
    </div>

    <div class="button">
      <button type="button" class="my-4 btn btn-outline-secondary btn-lg" @click="onRoute('SearchEvent')">
        관련 이벤트 더 보기
      </button>
    </div>

  </div>
</template>

<script>
export default {
  name: 'SearchResult',
  data() {
    return {
      result: '',
    }
  },
  methods: {
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
  },
  created() {
    this.result = this.$route.params.text
  }
}
</script>

<style>
.title {
  text-align: center;
}

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

  .event-img {
   width: 100%;
   height: auto;
  }
  .event-name {
   font-size: 1rem; 
   margin-bottom: 10px;
  }
  .date {
    font-size: 1rem;
  }
  .event-des {
    font-size: 1rem;
    margin-bottom: 20px;
  }
}

@media screen and (max-width: 576px) {
  .product-img {
    width: 100%;
  }
  .event-name {
    margin-bottom: 5px;
  }
  .date {
    font-size: 0.5rem;
  }
  .event-des {
    font-size: 0.8rem;
    margin-bottom: 14px;
  }
}

p {
  margin: 0;
}

.button {
  text-align: center;
}

.date {
  position: absolute;
  bottom: 0px;
}

</style>