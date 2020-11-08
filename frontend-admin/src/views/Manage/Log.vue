<template>
  <div v-if="logs">
    <div class="table-container mt-0">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">No</th>
            <th scope="col">분류</th>
            <th scope="col">유저</th>
            <th scope="col">서버 IP</th>
            <th scope="col">생성일</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(log, index) in logsForList" :key="index">
            <th scope="row">{{ (nowPage * perPage) + (index + 1) }}</th>
            <td>{{ log.type }}</td>
            <td>{{ log.cms_user.first_name }}</td>
            <td>{{ log.register_ip }}</td>
            <td>{{ log.create_date }}</td>
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
  left: 40%;
}
</style>