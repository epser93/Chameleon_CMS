<template>
  <div class="container" v-if="event">
    <!-- event detail head -->
    <div class="event-detail d-flex flexbox_wrapping justify-content-between mt-4">
      <h3 class="event-title">{{ event.title }}</h3>
      <p class="event-date mt-2 mb-0">이벤트 기간: {{ event.start_date.slice(0,10) }} ~ {{ event.end_date.slice(0,10) }}</p>
    </div>
    <hr>
    <!-- event image -->
    <div class="column justify-content-center mt-4">
      <div class="d-flex mb-4">
        <img :src="event.thumbnail_image" class="w-100" alt="">
      </div>
      <!-- event detail image -->
      <div class="d-flex event-detail-img" v-for="(image, index) in event.images" :key="index">
        <img :src="image.image" class="w-100" alt="">
      </div>
    </div>

    <div class="d-flex flexbox_wrapping justify-content-center mt-4 mb-4" v-if="event.url">
      <button type="button" class="btn btn-dark" @click="onClickWindows(image.image)">관련 상품 보러가기</button>
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
      window.open('https://chameleon.gq'+url) 
    },
  },
  created() {
    this.getEvent(this.$route.params.eid)
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
}
</script>

<style>
@media screen and (max-width: 576px) {  
  .event-detail {
    display: flex;
    flex-direction: column;
  }
}
</style>