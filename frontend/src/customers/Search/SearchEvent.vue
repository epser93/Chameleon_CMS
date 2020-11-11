<template>
  <div class="container my-4">
    <h3>' {{ text }} ' 관련 이벤트 {{ result }}건</h3>
    <hr>
    
    <div v-if="search.events.length > 0">
      <h3 class="title my-4">EVENT</h3>
      <hr>

      <div v-for="(event, index) in search.events" :key="index">
        <div class="row my-4 justify-content-around">
          <div class="col-sm-12 col-md-8">
            <img :src="'http://k3c205.p.ssafy.io'+event.thumbnail_image" class="event-img" alt="" @click="onEventDetail(event.id)">
          </div>
          <div class="col-sm-12 col-md-4">
            <h4 class="event-name" @click="onEventDetail(event.id)">{{ event.title }}</h4>
            <div class="column">
              <p class="event-des">이벤트 설명</p>
              <p class="date">기간: {{ event.start_date.slice(0,10) }} ~ {{ event.end_date.slice(0,10) }}</p>
            </div>
          </div>
        </div>
        <hr>
      </div>
    </div>

    <div v-if="result === 0">
      <h3> 검색 결과 없음 </h3>
    </div>

    <div class="button">
      <button type="button" class="my-4 btn btn-outline-secondary btn-lg" @click="$router.go(-1)">
        뒤로가기
      </button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'SearchEvent',
  data() {
    return {
      text: '',
    }
  },
  computed: {
    ...mapState('customer', ['search']),
    result() {
      if ( this.search ) {
        return this.search.events.length
      }
      else {
        return 0
      }
    }
  },
  methods: {
    ...mapActions('customer', ['getSearch']),
    onEventDetail(eid) {
      this.$router.push({name:'CustomerEventDetail', params:{eid: eid}})
		},
  },
  created() {
    this.text = this.$route.params.text
    this.getSearch(this.text)
  }
}
</script>

<style>

</style>