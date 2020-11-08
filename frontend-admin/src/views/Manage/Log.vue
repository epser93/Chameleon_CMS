<template>
  <div>
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
          <tr v-for="(log, index) in logs" :key="index">
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ log.type }}</td>
            <td>{{ log.cms_user.username }}</td>
            <td>{{ log.cms_user.first_name }}</td>
            <td>{{ log.register_ip }}</td>
            <td>{{ calculateDate(log.create_date) }}</td>
          </tr>
        </tbody>
      </table>
      <div class="page-navi">
        <nav aria-label="Page navigation example justify-content-center">
          <ul class="pagination">
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li class="page-item active"><a class="page-link" href="#">1</a></li>
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
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
  name: "Logs",
  data() {
    return {

    }
  },
  computed: {
    ...mapState('account', ['logs'])
  },
  methods: {
    ...mapActions('account', ['getLogs']),
    calculateDate(time) {
      const tz = new Date(time)
      const arrDay = ['일','월','화','수','목','금','토']
      return tz.toLocaleDateString() + '(' + arrDay[tz.getDay()] + ') ' + tz.getHours() + '시 ' + tz.getMinutes() + '분 ' + tz.getSeconds() + '초 '
    }
  },
  created() {
    this.getLogs()
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
  left: 50%;
}
</style>