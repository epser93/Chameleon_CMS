<template>
  <div class="box container-fluid">
    <!-- 반응형 추가해야 함 -->
    <div class="row">
      <div class="col-2">
        <ol class="carousel-indicators mb-0" data-interval="false">
          <div class="column mt-5">
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
      <div class="col-5 mt-5">
        <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel" data-interval="false">
          <div class="carousel-inner">
            <!-- Image1 -->
            <div class="carousel-item active">
              <img src="@/assets/250.png" class="d-block" alt="...">
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
            <!-- Image2 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
            <!-- Image3 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
            <!-- Image4 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
            <!-- Image5 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
            <!-- Image6 -->
            <div class="carousel-item">
              <img src="@/assets/250.png" class="d-block" alt="...">
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Item Info -->
      <div class="itm-info col-5">
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
          <!-- <div> -->
          <!-- </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CarouselTemplate',
}
</script>

<style>
.box {
  background-color: #e8f0f7;
}

.carousel-indicators{
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

.itm-info {
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

/* 반응형 추가해야 함 */
/* @media screen and (max-width: 768px) {

} */
</style>