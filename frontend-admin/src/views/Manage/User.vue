<template>
  <div class="container-fluid p-0">
    <div class="table-container mt-0">
      <div class="unauthorized">
        <button type="button" class="btn ml-3 mt-3 mb-3" data-toggle="modal" data-target="#unauthorizedUser">
          미승인 회원 <span class="badge badge-light ml-1">{{unAuthorizedUserCount}}</span>
        </button>
      </div>
      <UnauthorizedUser></UnauthorizedUser>
      <table class="table">
        <thead>
          <tr class="top-tr">
            <th scope="col">#</th>
            <th scope="col">부서</th>
            <th scope="col">이름</th>
            <th scope="col">아이디</th>
            <th scope="col">권한</th>
          </tr>
        </thead>
        <tbody>
          <tr class="user-infos" @click="authorityModalUser(userinfo)" v-for="(userinfo, idx) in accessUserInfos" :key="idx">
            <th scope="row">{{ idx+1 }} </th>
            <td>{{ userinfo.department.name }}</td>
            <td>{{ userinfo.first_name }}</td>
            <td>{{ userinfo.username }}</td>
            <td>
              <span v-if="userinfo.is_eventer" class="badge badge-primary">Event</span>
              <span v-if="userinfo.is_logger" class="badge badge-secondary">Log</span>
              <span v-if="userinfo.is_producter" class="badge badge-success">Product</span>
              <span v-if="userinfo.is_marketer" class="badge badge-dark">Main + Notice</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <AuthorityModal/>
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
</template>

<script>
import AuthorityModal from '@/components/AuthorityModal'
import UnauthorizedUser from'@/components/UnauthorizedUser'
import { mapActions, mapState, mapMutations, mapGetters } from 'vuex'
import $ from 'jquery'

export default {
  components: {
    AuthorityModal,
    UnauthorizedUser
  },
  data() {
    return {

    }
  },
  methods: {
    ...mapActions('account', ['getAccessUserInfo']),
    ...mapMutations('account', ['SET_USER']),
    authorityModalUser(userdata) {
      const copydata = JSON.parse(JSON.stringify(userdata))
      this.SET_USER(copydata)
      $('#authorityModal').modal('show')
    }
  },
  computed : {
    ...mapState('account', ['accessUserInfos']),
    ...mapGetters('account', ['unAuthorizedUserCount'])
  },
  created() {
    this.getAccessUserInfo()
  }

}
</script>

<style scoped>
.table-container {
  width: 100%;
  margin-top: 10vh; 
  text-align: center;
}

.unauthorized {
  background-color: #e2e4e6;
}

.user-infos {
  cursor: pointer;
}

.user-infos:hover {
  background-color: #e9e9e9;
}

.unauthorized {
  display: flex;
}

td span {
  margin-right: 1vw;
}

.btn {
  background-color: #4ea1b5;
  color: white;
}

.page-navi {
  position: absolute;
  bottom: 0;
  left: 50%;
}
</style>