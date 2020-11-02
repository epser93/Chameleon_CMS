<template>
  <div>
    <!-- 대표 이미지 Carousel -->
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="@/assets/dummy-img.png" class="d-block w-100" alt="main image1">
        </div>
        <div class="carousel-item">
          <img src="@/assets/dummy-img.png" class="d-block w-100" alt="main image2">
        </div>
        <div class="carousel-item">
          <img src="@/assets/dummy-img.png" class="d-block w-100" alt="main image3">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    <!-- 추천 제품 리스트 -->
    <div class="container">
      <div class="row mt-4 mb-3">
        <h2 class="mr-auto ml-auto">추천 제품</h2>
      </div>
      <div class="row justify-content-around mb-2">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image1">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image2">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image3">
        <img src="@/assets/250.png" class="col-6 col-lg-3 mb-4" alt="recommand product image4">
      </div>
    </div>
    <!-- 이벤트 Carousel --> 
    <div class="container mb-5">
      <div class="row mb-4">
        <h2 class="mr-auto ml-auto">이벤트</h2>
      </div>
      <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="@/assets/dummy-1200.png" class="d-block w-100" alt="main image1">
          </div>
          <div class="carousel-item">
            <img src="@/assets/dummy-1200.png" class="d-block w-100" alt="main image2">
          </div>
          <div class="carousel-item">
            <img src="@/assets/dummy-1200.png" class="d-block w-100" alt="main image3">
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Home',
  created() {
    if (!this.$cookies.get("DontOpenNotice")) {
      window.open("http://localhost:8080/notice", "", "width=305,height=332,left=200,top=200")
    }
  }
}
</script>

<style>
@media screen and (max-width: 500px) {
  h2 {
   font-size: 20px;
  }
}
</style>
