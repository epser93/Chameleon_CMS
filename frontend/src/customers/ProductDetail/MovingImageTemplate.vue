<template>
  <div class="container-fluid">
    <div class="one">
      <div class="left">
        <div v-for="(thumbnail, index) in thumbnails" :key="index" class="product-img">
          <img :src="getImage(thumbnail.item_image)" class="product-image mb-3" alt="">
        </div>
      </div>
    <div class="right">
      <div class="right-child mt-5">
        <div class="itm-info-box">
          <h3>{{ itemInfo.name }}</h3>
          <h5>{{ addComma(itemInfo.price) }}원</h5>
          <div class="itm-info-detail">
            <p v-for="(spec, index) in itemInfo.descriptions" :key="index">{{ spec.category_description.name }} : {{ spec.content}}</p>
          </div>
        </div>
      </div>
    </div>
    </div>
    <div class="column bottom">
      <div v-for="(detailImage, index) in detailImages" :key="index" class="bottom-product-image">
        <img :src="getImage(detailImage.item_image)" class="mb-3" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import { mapActions, mapState } from 'vuex'
import SERVER from '@/api/drf'
export default {
  props: ['itemInfo'],
  data() {
    return {

    }
  },
  computed: {
    ...mapState('customer', ['thumbnails', 'detailImages'])
  },
  methods: {
    ...mapActions('customer', ['divideImage']),
    reOrder() {
      let mq = window.matchMedia("(min-width: 1140px)");
      if (mq.matches) {
        $('.right').addClass('customm');
        let scroll = $(window).scrollTop(),
          topContent = $('.one').position().top - 25,
          sectionHeight = $('.left').height(),
          rightHeight = $('.right-child').height(),
          bottomContent = topContent + sectionHeight - rightHeight - 45;

        if (scroll > topContent && scroll < bottomContent) {
          $('.customm').removeClass('posAbs').addClass('posFix');
        } else if (scroll > bottomContent) {
          // $('.customm').removeClass('posFix').addClass('posAbs');
        } else if (scroll < topContent) {
          $('.customm').removeClass('posFix');
        }
      } else {
        $('.right-child').removeClass('customm posAbs posFix');
      }
    },
    getImage(src) {
      return SERVER.domain + src.slice(56, src.length)
    },
    addComma(num) {
      const regexp = /\B(?=(\d{3})+(?!\d))/g;
      return num.toString().replace(regexp, ',');
    }
  },
  watch: {
    'itemInfo' : function() {
      this.divideImage(this.itemInfo.images)
    }
  },
  created () {
    window.addEventListener('scroll', this.reOrder);
    this.divideImage(this.itemInfo.images)
  },
  destroyed () {
    window.removeEventListener('scroll', this.reOrder);
  },
}
</script>

<style scoped>
/* .container {
  margin:0 auto;
  padding:25px;
} */

.one {
  position:relative;
  width: auto;
  border-bottom: 10px solid #f8f9fa;
}

.one::after {
  content: "";
  display: block;
  clear: both;
}

.left {
  width:calc(50% - 12px);
  float:left;
  margin-right:25px;
}

.product-img {
  width: 30vw;

}

.right {
  width:calc(30% - 13px);
  margin-right: auto;
  margin-left: auto;
  float:right;
  display: flex;
  margin-bottom: 10px;
}

.content {
  width:100%;
  height:200px;
  background:#ccd9f1;
  margin-bottom:25px;
  border-radius:4px;
}

.right-child {
  width:350px;
  padding:10px;
  text-align:center;
  color:black;
  border: 4px solid #f8f9fa;
  border-radius: 10px;
}

.posFix {
  position: sticky;
  top:25px;
}

.posAbs {
  position:absolute;
  bottom:25px;
}

/* .bottom {
  width:100%;
  margin-top: 30px;
} */

.bottom-product-image {
  width: 100vw;
}
@media (max-width:992px) {
  .left{
    width:100%;
  }

  .container{
    width:100%;
  }

  .right{
    width:100%;
  }

  .right > right-child {
    width:100%;
  }
}
</style>