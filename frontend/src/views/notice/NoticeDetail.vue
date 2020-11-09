<template>
  <div class="container" v-if="notice && image">
    <div class="mt-4 mb-3">
      <button type="button" class="btn btn-dark btn-sm" @click="$router.go(-1)">뒤로가기</button>
    </div>
    <div class="row division align-items-center pl-3">
      <p class="title">제목</p>
      <p class="notice-title ml-2">{{ notice.title }}</p>
    </div>
    <div class="row division align-items-center pl-3">
      <p class="contents">내용</p>
      <p class="notice-content ml-2">{{ notice.content }}</p>
    </div>
    <div class="division">
      <p class="image">공지 이미지</p>
      <img class="notice-image" :src="image" alt="">
    </div>
    <div>
      <button type="button" class="btn btn-outline-warning" v-if="!notice.end_date" @click="onUpdate()">수정</button>
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
    onUpdate() {
      this.$router.push({ name : 'NoticeUpdate', params: { id : this.$route.params.id }})
    }
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
  font-size: 24px;
  font-weight: bold;
}

.contents {
  font-size: 24px;
  font-weight: bold;
}

.notice-title {
  border-bottom: 2px solid grey;
}

.notice-content {
  border-bottom: 2px solid grey;
}

.image {
  font-size: 24px;
  font-weight: bold;
}

.division {
  margin-bottom : 2vh;
}
</style>