<template>
  <div v-if="logs">
    <div class="table-container mt-0">
      <table class="table">        
        <thead>
          <tr>
            <th scope="col">No</th>
            <th scope="col">분류</th>
            <th scope="col">유저ID</th>
            <th scope="col">이름</th>
            <th scope="col">서버 IP</th>
            <th scope="col">생성일</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(log, index) in logsForList" :key="index">
            <th scope="row">{{ (nowPage * perPage) + (index + 1) }}</th>
            <td>{{ log.type }}</td>
            <td>{{ log.cms_user.username }}</td>
            <td>{{ log.cms_user.first_name }}</td>
            <td>{{ log.register_ip }}</td>
            <td>{{ calculateDate(log.create_date) }}</td>
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
// import $ from 'jquery'

export default {
  name: "Logs",
  data() {
    return {
      perPage: 10,
      nowPage: 0,
    }
  },
  computed: {
    ...mapState('account', ['logs']),
    rows() {
      return this.logs.length
    },
    pages() {
      return Math.ceil(this.logs.length/this.perPage)
    },
    logsForList() {
      return this.logs.slice(
        (this.nowPage) * this.perPage,
        (this.nowPage + 1) * this.perPage
      )
    },
  },
  methods: {
    ...mapActions('account', ['getLogs']),
    onPage(page) {
      this.nowPage = page
    },
    calculateDate(time) {
      const tz = new Date(time)
      const arrDay = ['일','월','화','수','목','금','토']
      return tz.toLocaleDateString() + '(' + arrDay[tz.getDay()] + ') ' + tz.getHours() + '시 ' + tz.getMinutes() + '분 ' + tz.getSeconds() + '초 '
    },
    test() {
      // console.log(this.paginationLength)
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
    this.getLogs()
  },
}
</script>

<style scoped>
.table-container {
  width: 100%;
  margin-top: 10vh; 
  text-align: center;
}

.page-navi {
  position: absolute;
  bottom: 0;
  margin-bottom: 10px;
  left: 50%;
}

img {
  cursor: pointer;
}
</style>