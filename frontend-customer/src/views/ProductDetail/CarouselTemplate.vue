<template>
  <div class="box container-fluid">
    <div class="row">
      <div class="col-6">
        <p>Image</p>
        <!-- <hooper :vertical="true" style="height: 400px" :itemsToShow="1.5" :centerMode="true">
          <slide>
            <img src="@/assets/250.png" style="width: 50px;" alt="">
          </slide>
          <slide>
            <img src="@/assets/250.png" style="width: 50px;" alt="">
          </slide>
          <slide>
            <img src="@/assets/250.png" style="width: 50px;" alt="">
          </slide>
          <slide>
            <img src="@/assets/250.png" style="width: 50px;" alt="">
          </slide>
          <slide>
            <img src="@/assets/250.png" style="width: 50px;" alt="">
          </slide>
          <slide>
            <img src="@/assets/250.png" style="width: 50px;" alt="">
          </slide>
        </hooper> -->
      </div>
      <div class="col-6">
        <p>price</p>
      </div>
    </div>
  </div>
</template>

<script>
// import { Hooper, Slide } from 'hooper';

export default {
  name: 'CarouselTemplate',
  // components: {
  //   Hooper,
  //   Slide
  // }
}
</script>

<style>
.box {
  height: 40vw;
}
</style>