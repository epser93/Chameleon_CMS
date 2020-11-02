<template>
  <div class="container">
    <!-- event detail head -->
    <div class="d-flex flexbox_wrapping justify-content-between mt-4">
      <h3 class="">이벤트 제목</h3>
      <p class="mt-2 mb-0">이벤트 기간: 2020-00-00 ~ 2020-00-00</p>
    </div>
    <hr>
    <!-- event image -->
    <div class="row justify-content-center mt-4">
      <div class="mb-4">
        <img src="https://picsum.photos/1200/500" class="event-img w-100" alt="">
      </div>
      <!-- event detail image -->
      <div class="d-flex event-detail-img mb-4">
        <h4 class="m-auto">Please add event detail image</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EventDetail',
}
</script>

<style>
.flexbox_wrapping {
  flex-wrap: wrap;
}

.event-detail-img {
  width: 100vw;
  height: 100vh;
  border: 2px solid grey;
}
</style>