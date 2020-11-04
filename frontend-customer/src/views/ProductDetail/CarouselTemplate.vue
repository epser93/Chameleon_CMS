<template>
  <div class="box container-fluid">
    <div class="row">
      <!-- col-md 이상일 때 나오는 왼쪽 세로 캐로우셀 -->
      <div class="d-none d-sm-none d-md-block col-2 px-0">
        <ol class="carousel-indicators-img mb-0" data-interval="false">
          <div class="direction column mt-5">
            <img src="@/assets/250.png" data-target="#carouselExampleCaptions" data-slide-to="0" class="active preview-img" alt="">
            <img src="@/assets/250.png" data-target="#carouselExampleCaptions" data-slide-to="1" class="preview-img" alt="">
            <img src="@/assets/250.png" data-target="#carouselExampleCaptions" data-slide-to="2" class="preview-img" alt="">
            <img src="@/assets/250.png" data-target="#carouselExampleCaptions" data-slide-to="3" class="preview-img" alt="">
            <img src="@/assets/250.png" data-target="#carouselExampleCaptions" data-slide-to="4" class="preview-img" alt="">
            <img src="@/assets/250.png" data-target="#carouselExampleCaptions" data-slide-to="5" class="preview-img" alt="">
          </div>
        </ol>
      </div>
      <!-- Carousel Image -->
      <div class="col-sm-12 col-md-5 mt-5 mr-auto ml-auto pl-0 pr-4">
        <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel" data-interval="false">
          <div class="carousel-inner">
            <!-- Image1 -->
            <div class="carousel-item active">
              <img src="@/assets/250.png" class="d-block" alt="...">
            </div>
            <!-- Image2 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
            </div>
            <!-- Image3 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
            </div>
            <!-- Image4 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
            </div>
            <!-- Image5 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
            </div>
            <!-- Image6 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
            </div>
          </div>
        </div>
      </div>
      <!-- col-sm일 때 나오는 하단 캐로우셀 -->
      <div class="d-block d-sm-block d-md-none col-12 mb-4">
        <ol class="carousel-indicators">
          <li data-target="#carouselExampleCaptions" data-slide-to="0" class="preview-btn"></li>
          <li data-target="#carouselExampleCaptions" data-slide-to="1" class="preview-btn"></li>
          <li data-target="#carouselExampleCaptions" data-slide-to="2" class="preview-btn"></li>
          <li data-target="#carouselExampleCaptions" data-slide-to="3" class="preview-btn"></li>
          <li data-target="#carouselExampleCaptions" data-slide-to="4" class="preview-btn"></li>
          <li data-target="#carouselExampleCaptions" data-slide-to="5" class="preview-btn"></li>
        </ol>
      </div>
      <!-- col-md 이상일 때 Item Info -->
      <div class="itm-info-md d-none d-sm-none d-md-block col-5">
        <div class="d-flex mt-2">
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
    <!-- col-sm일 때 Item Info -->
    <div class="item-info-sm d-block d-sm-block d-md-none col-12">
      <div class="item-info-sm-detail mx-1 row justify-content-between">
        <h4>판매가</h4>
        <h4>000,000원</h4>
      </div>
    </div>
    <div class="d-block d-sm-block d-md-none col-12 column mx-2">
      <p>Item Detail Information 1</p>
      <p>Item Detail Information 2</p>
      <p>Item Detail Information 3</p>
      <p>Item Detail Information 4</p>
      <p>Item Detail Information 5</p>
      <p>Item Detail Information 6</p>   
    </div>
    <!-- Item deatil image ara -->
    <div class="bottom mb-4">
      <h1>Item detail image Area</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CarouselTemplate',
}
</script>

<style scoped>
.box {
  background-color: #e8f0f7;
}

.carousel-indicators-img{
  width: 50px;
}

.preview-img {
  width: 50px;
  border: 1px solid transparent;
  border-radius: 10px;
  margin-bottom: 10px;
}

ol {
  height: 100%;
}

.itm-info-md {
  width: 320px;
  height: 500px;
  background-color: white;
  position: relative;
}

.carousel-item {
  min-height: 250px; 
}

.carousel-inner {
  margin-top: 55px;
  margin-right: -50px;
  /* min-width: 250px; */
}

.itm-info-detail {
  width: 300px;
  height: 300px;
  border: 4px solid #f8f9fa;
  border-radius: 10px;
  padding: 10px;
  position: absolute;
}

.itm-info-box {
  justify-content: center;
  flex-direction: column;
}

.bottom {
  width:100%;
  height:900px;
  background:#8698b9;
}

.preview-btn {
  background-color: #4c4949;
}

img {
  margin-left: auto;
  margin-right: auto;
}
  
@media screen and (max-width: 768px) {
  .itm-info {
    width: 100%;
    height: 500px;
    background-color: white;
    position: relative;
  }
  .item-info-sm {
    background-color: white;
  }
  .container-fluid {
    padding: 0;
  }
  .carousel-inner {
    margin-top: 0;
    margin-bottom: 40px;
  }
}
</style>