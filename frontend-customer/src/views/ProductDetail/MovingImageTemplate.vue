<template>
  <div class="container-fluid mt-4">
    <section class="one clearfix">
      <div class="left">
        <div v-for="image in images" :key="image.name" class="product-img">
          <img :src="image.src" class="product-image mb-3" alt="">
        </div>
        <!-- <div></div>
        <div></div>
        <div></div>
        <div></div> -->
      </div>
      <div class="right">
        <div class="right-child">
          <div class="itm-info-box">
            <h3>제품 이름</h3>
            <p>제품 No.</p>
              <h5>000,000원</h5>
              <div class="itm-info-detail">
                <p>Item Detail Information 1</p>
                <p>Item Detail Information 2</p>
                <p>Item Detail Information 3</p>
                <p>Item Detail Information 4</p>
                <p>Item Detail Information 5</p>
                <p>Item Detail Information 6</p>
              </div>
          </div>
        </div>
      </div>
    </section>
    <div class="bottom mb-4">
      <h1>Image Area</h1>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  created () {
    window.addEventListener('scroll', this.reOrder);
  },
  destroyed () {
    window.removeEventListener('scroll', this.reOrder);
  },
  data() {
    return {
      images: [
        {name: 'vertical1', src: require("@/assets/vertical1.jpg")},
        {name: 'vertical2', src: require("@/assets/vertical2.jpg")},
        {name: 'vertical2', src: require("@/assets/vertical3.jpg")},
        {name: 'vertical2', src: require("@/assets/vertical4.jpg")},
      ]
    }
  },
  methods: {
    reOrder() {
      let mq = window.matchMedia("(min-width: 992px)");
      if (mq.matches) {
        $('.right-child').addClass('customm');
        let scroll = $(window).scrollTop(),
          topContent = $('.one').position().top - 25,
          sectionHeight = $('.left').height(),
          rightHeight = $('.right-child').height(),
          bottomContent = topContent + sectionHeight - rightHeight - 45;

        if (scroll > topContent && scroll < bottomContent) {
          $('.customm').removeClass('posAbs').addClass('posFix');
        } else if (scroll > bottomContent) {
          $('.customm').removeClass('posFix').addClass('posAbs');
        } else if (scroll < topContent) {
          $('.customm').removeClass('posFix');
        }
      } else {
        $('.right-child').removeClass('customm posAbs posFix');
      }
    }
  },
}
</script>

<style>
.container {
  height:100%;
  width:992px;
  margin:0 auto;
  padding:25px;
}

.one {
  position:relative;
}

.left {
  width:calc(50% - 12px);
  float:left;
  margin-right:25px;
}

.product-img {
  width: 100%;
}

/* .left > div{
  width:100%;
  height:200px;
  background:#ccd9f1;
  margin-bottom:25px;
  border-radius:4px;
} */

.right {
  width:calc(50% - 13px);
  float:right;
}

.right-child {
  display:block;
  width:458px;
  height: 85vh;
  padding:10px;
  text-align:center;
  color:black;
  border: 4px solid #f8f9fa;
  border-radius: 10px;
}

.right-child > h2{
  font-size:38px;
}

.posFix {
  position:fixed;
  top:25px;
  margin-right: auto;
  margin-left: auto;
}

.posAbs {
  position:absolute;
  bottom:25px;
}

.bottom {
  width:100%;
  height:900px;
  background:#8698b9;
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