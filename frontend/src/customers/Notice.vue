<template>
  <div class="notice-main">
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li v-for="(notice, index) in notices" :key="index" data-target="#carouselExampleIndicators" :data-slide-to="index" :class="(index === 0) ? 'active' : ''"></li>
      </ol>
      <div class="carousel-inner">
        <div v-for="(notice, index) in notices" :key="index" :class="(index === 0) ? 'carousel-item active' : 'carousel-item'">
          <img :src="getImage(notice.image)" class="d-block w-100" alt="main image1">
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
    <div class="row mx-0">
      <button class="btn btn-info btn-sm col-6" type="button" @click="winClose(); winNonOpen();">하루 동안 보지 않기</button>
      <button class="btn btn-secondary btn-sm col-6" type="button" @click="winClose();">닫기</button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import SERVER from '@/api/drf'
export default {
  name: 'Notice',
  data() {
    return {
    }
  },
  computed: {
    ...mapState('notice', ['notices'])
  },
  methods: {
    ...mapActions('notice', ['getNotices']),
    winClose() {
      window.close()
    },
    winNonOpen() {
      this.$cookies.set('DontOpenNotice','idontwanttoseethat')
    },
    getImage(src) {
      return SERVER.domain + src.slice(56, src.length)
    }
  },
  created() {
    this.getNotices()
  }
}
</script>

<style scoped>
.notice-img {
  width: 100%;
}

</style>