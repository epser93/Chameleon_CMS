<template>
  <div class="notice-container" v-if="notice && image">
    <div class="division">
      <p class="title">제목</p>
      <div>{{ notice.title }}</div>
    </div>
    <div class="division">
      <p class="contents">내용</p>
      <div>{{ notice.content }}</div>
    </div>
    <div class="division">
      <p class="image">공지 이미지</p>
      <img class="notice-image" :src="image" alt="">
    </div>
    <div>
      <button type="button" class="btn btn-outline-warning" v-if="!notice.end_date">수정</button>
      <button type="button" class="btn btn-outline-secondary" v-if="!notice.end_date" @click="endNotice()">종료</button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: "NoticeDetail",
  data() {
    return {

    }
  },
  computed: {
    ...mapState('notice', ['notice', 'image'])
  },
  methods: {
    ...mapActions('notice', ['getNotice', 'endNotice']),
  },
  created() {
    this.getNotice(this.$route.params.id)
  }
}
</script>

<style scoped>
.notice-image {
  width: 300px;
  height: 300px;
}

.title {
  font-size: 30px;
  font-weight: bold;
}

.contents {
  font-size: 30px;
  font-weight: bold;
}

.image {
  font-size: 30px;
  font-weight: bold;
}

.division {
  margin-bottom : 2vh;
}
</style>