<template>
  <div class="container my-4">
    <h3 class="title my-4">EVENT</h3>
    <hr>

    <div class="row my-4 ml-4">
      <div class="col-8">
        <img src="https://picsum.photos/600/250" class="event-img" alt="">
      </div>
      <div class="col-4">
        <h4 class="event-name">이벤트 B</h4>
        <div class="event-spec m-0">
          <p>이벤트 설명</p>
        </div>
        <p class="date">기간: 2020-00-00 ~ 2020-00-00</p>
      </div>
    </div>
    <hr>
    <div class="row my-4 ml-4">
      <div class="col-8">
        <img src="https://picsum.photos/600/250" class="event-img" alt="">
      </div>
      <div class="col-4">
        <h4 class="event-name">이벤트 A</h4>
        <div class="event-spec m-0">
          <p>이벤트 설명</p>
        </div>
        <p class="date">기간: 2020-00-00 ~ 2020-00-00</p>
      </div>
    </div>

    <div class="button">
      <button type="button" class="my-4 btn btn-outline-secondary btn-lg" @click="$router.go(-1)">
        뒤로가기
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchEvent',
}
</script>

<style>

</style>