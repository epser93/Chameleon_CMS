<template>
  <div class="container pl-0">
    <div class="table-container">
      <div class="btn ml-3 mt-3 mb-3 p-0">
        <button type="button" class="btn btn-info ml-3" @click="makeNotice()">생성</button>
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
          <tr class="notice" v-for="(notice, index) in noticesForList" :key="index" @click="goDetail(notice)">
            <td>{{ (nowPage * perPage) + (index + 1) }}</td>
            <td>{{ notice.title }}</td>
            <td v-if="notice.start_date">{{ refactoringDate(notice.start_date) }} ~ {{ refactoringDate(notice.end_date) }}</td>
            <td v-else>-</td>
            <td v-if="!notice.is_temp && notice.is_active">게시중</td>
            <td v-else-if="notice.is_temp && notice.is_active">임시저장중</td>
            <td v-else-if="!notice.is_active">종료</td>
          </tr>
        </tbody>
      </table>
      <div class="page-navi justify-content-center">
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <div v-for="(page, i) in pages" :key="i">
              <li :class="(i == nowPage) ? 'page-item active':'page-item' ">
                <a @click="onPage(i)" class="page-link" href="#">{{ page }}</a>
              </li>
            </div>
          </ul>
        </nav>
      </div>
    </div> 
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  data() {
    return {
      perPage: 10,
      nowPage: 0,
    }
  },
  computed: {
    ...mapState('notice', ['notices']),
    rows() {
      return this.notices.length
    },
    pages() {
      return Math.ceil(this.notices.length/this.perPage)
    },
    noticesForList() {
      return this.notices.slice(
        (this.nowPage) * this.perPage,
        (this.nowPage + 1) * this.perPage
      )
    },
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

.page-navi {
  position: absolute;
  bottom: 0;
  left: 50%;
}
</style>