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
            <th scope="col" @click="test">생성일</th>
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
      console.log(this.paginationLength)
    }
  },
  created() {
    this.getLogs()
  },
  updated() {
    let pagination = document.querySelector('.page-navi')
    let tableContainer = document.querySelector('.table-container')
    let tableConatinerLength = (tableContainer.clientWidth - pagination.clientWidth) / 2
    document.querySelector('.page-navi').style.left = String(tableConatinerLength) + 'px'
  }
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
}
</style>