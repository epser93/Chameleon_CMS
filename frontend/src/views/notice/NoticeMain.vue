<template>
  <div class="container pl-0">
    <div class="table-container">
      <div class="notice-btn row align-items-center mt-3 mb-3">
        <h5 class="mb-0 ml-3">공지</h5>
        <button type="button" class="btn btn-info btn-sm" @click="makeNotice()">추가</button>
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
      <div class="page-navi">
        <nav aria-label="Page navigation example">
          <ul v-if="pages == 0" class="pagination">
            <li class="page-item">
              <img src="@/assets/icons/caret-left.svg" width="26" height="26" title="caret-left" @click="prevPage()">
            </li>
            <p> {{ nowPage + 1 }}  / {{ pages + 1}} </p>
            <li class="page-item">
              <img src="@/assets/icons/caret-right.svg" width="26" height="26" title="caret-right" @click="nextPage()">
            </li>
          </ul>
          <ul v-else class="pagination">
            <li class="page-item">
              <img v-if="nowPage == 0" src="@/assets/icons/caret-left.svg" width="26" height="26" title="caret-left" @click="prevPage()">
              <img v-else src="@/assets/icons/caret-left-fill.svg" width="26" height="26" title="caret-left-fill" @click="prevPage()">
            </li>
            <p> {{ nowPage + 1 }}  / {{ pages }} </p>
            <li class="page-item">
              <img v-if="nowPage == (pages-1)" src="@/assets/icons/caret-right.svg" width="26" height="26" title="caret-right" @click="nextPage()">
              <img v-else src="@/assets/icons/caret-right-fill.svg" width="26" height="26" title="caret-right-fill" @click="nextPage()">
            </li>
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
      perPage: 7,
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
    },
    prevPage() {
      if (this.nowPage > 0) {
        this.nowPage -= 1
      }
    },
    nextPage() {
      if (this.nowPage < this.pages-1) {
        this.nowPage += 1
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

.page-item {
  cursor: pointer;
}
</style>