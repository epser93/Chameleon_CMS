<template>
  <div class="container-fluid">
    <div class="row">
      <div v-for="image in images" :key="image.name" class="product-img col-7">
        <img :src="image.src" class="product-image" alt="">
      </div>
      <div class="product-detail col-5 d-flex" @scroll="changeSticky">
        <div class="mt-2">
          <div class="column itm-info-box">
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
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovingImageTemplate',
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
    changeSticky() {
      let productDetail = document.getElementById("product-detail");
      let sticky = productDetail.offsetTop;
      if (window.pageYoffset > sticky) {
        productDetail.classList.add("sticky");
      } else {
        productDetail.classList.remove("sticky");
      }
    }
  }
}
</script>

<style>
.product-image {
  width: 100%;
  margin-bottom: 10px;
}

.sticky {
  position: fixed;
  top: 0;
  width: 100%
}

.itm-info-box {
  float: right;
}

.product-detail {
  float: top;
}
</style>