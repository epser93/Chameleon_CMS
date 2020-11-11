<template>
  <div class="container" v-if="event">
    <!-- event detail head -->
    <div class="d-flex flexbox_wrapping justify-content-between mt-4">
      <h3 class="">{{ event.title }}</h3>
      <p class="mt-2 mb-0">이벤트 기간: {{ event.start_date.slice(0,10) }} ~ {{ event.end_date.slice(0,10) }}</p>
    </div>
    <hr>
    <!-- event image -->
    <div class="row justify-content-center mt-4">
      <div class="mb-4">
        <img :src="'http://k3c205.p.ssafy.io'+event.thumbnail_image" class="event-img w-100" alt="">
      </div>
      <!-- event detail image -->
      <div class="d-flex event-detail-img mb-4" v-for="(image, index) in event.images" :key="index">

        <img :src="'http://k3c205.p.ssafy.io'+image.image" class="event-img w-100" alt="">
      </div>
    </div>

    <div class="d-flex flexbox_wrapping justify-content-between mt-4">
      <button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows(image.image)">관련 상품 보러가기</button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'EventDetail',
  computed: {
    ...mapState('customer', ['event']),
  },
  methods: {
    ...mapActions('customer', ['getEvent']),
    onClickWindows(url) {
      window.open('http://k3c205.p.ssafy.io'+url) 
    },
  },
  created() {
    this.getEvent(this.$route.params.eid)
  }
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