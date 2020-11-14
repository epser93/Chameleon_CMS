<template>
  <div class="container my-4" v-if="search">
    <h3>' {{ text }} ' 검색결과 {{ result }}건</h3>
    {{ search }}
    <hr>

    <div v-if="search.items.length > 0">
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
    </div>

    <div v-if="search.events.length > 0">
      <h3 class="title my-4">EVENT</h3>
      <hr>

      <div v-for="(event, index) in search.events" :key="index">
        <div class="row my-4 justify-content-around" v-if="index < 2">
          <div class="col-sm-12 col-md-8">
            <img :src="'http://k3c205.p.ssafy.io'+event.thumbnail_image.slice(56)" class="event-img" alt="" @click="onEventDetail(event.id)">
          </div>
          <div class="col-sm-12 col-md-4">
            <h4 class="event-name" @click="onEventDetail(event.id)">{{ event.title }}</h4>
            <div class="column">
              <p class="event-des">이벤트 설명</p>
              <p class="date">기간: {{ event.start_date.slice(0,10) }} ~ {{ event.end_date.slice(0,10) }}</p>
            </div>
          </div>
        </div>
        <hr>
      </div>

      <div class="button">
        <button type="button" class="my-4 btn btn-outline-secondary btn-lg" @click="onRoute('SearchEvent')">
          관련 이벤트 더 보기
        </button>
      </div>
    </div>

    <div v-if="result === 0">
      <h3> 검색 결과 없음 </h3>
    </div>

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'SearchResult',
  data() {
    return {
      text: '',
    }
  },
  computed: {
    ...mapState('customer', ['search']),
    result() {
      if ( this.search ) {
        return this.search.items.length + this.search.events.length
      }
      else {
        return 0
      }
    }
  },
  watch: {
    $route() {
      this.text = this.$route.params.text
      this.getSearch(this.text)
    }
  },
  methods: {
    ...mapActions('customer', ['getSearch']),
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
    onEventDetail(eid) {
      this.$router.push({name:'CustomerEventDetail', params:{eid: eid}})
		},
  },
  created() {
    this.text = this.$route.params.text
    this.getSearch(this.text)
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