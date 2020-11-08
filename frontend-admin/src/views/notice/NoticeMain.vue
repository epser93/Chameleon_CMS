<template>
  <div>
    <div class="table-container">
      <div class="btn">
        <button type="button" class="btn btn-outline-success" @click="makeNotice()">생성</button>
      </div>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">제목</th>
            <th scope="col">공지기간</th>
            <th scope="col">상태</th>
          </tr>
        </thead>
        <tbody>
          <tr class="notice" v-for="(notice, index) in notices" :key="index" @click="goDetail(notice)">
            <td>{{ index + 1 }}</td>
            <td>{{ notice.title }}</td>
            <td v-if="notice.start_date">{{ refactoringDate(notice.start_date) }} ~ {{ refactoringDate(notice.end_date) }}</td>
            <td v-else>-</td>
            <td v-if="!notice.is_temp && notice.is_active">게시중</td>
            <td v-else-if="notice.is_temp && notice.is_active">임시저장중</td>
            <td v-else-if="!notice.is_active">종료</td>
          </tr>
        </tbody>
      </table>
    </div> 
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  data() {
    return {

    }
  },
  computed: {
    ...mapState('notice', ['notices'])
  },
  methods: {
    ...mapActions('notice', ['getNotices']),
    makeNotice() {
      this.$router.push({ name : 'NoticeForm' })
    },
    refactoringDate(time) {
      if (time) {
        return time.slice(0,10)
      } else {
        return null
      }
    },
    goDetail(notice) {
      if (notice.is_temp) {
        this.$router.push({name: 'NoticeUpdate', params : { id: notice.id}})
      } else {
        this.$router.push({name : 'NoticeDetail', params : { id : notice.id }})
      }
    }
  },
  created() {
    this.getNotices()
    console.log(this.notices)
  }
  
}

</script>

<style scoped>
.notice {
  cursor: pointer;
}

.notice:hover {
  background: #e9e9e9;
}

.table {
  text-align: center;
}
</style>