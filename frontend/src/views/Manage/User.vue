<template>
  <div class="container p-0">
    <div class="table-container mt-0">
      <div class="unauthorized">
        <button type="button" class="btn ml-3 mt-3 mb-3" id="unauthorized-btn" data-toggle="modal" data-target="#unauthorizedUser">
          미승인 회원 <span class="badge badge-light ml-1">{{unAuthorizedUserCount}}</span>
        </button>
      </div>
      <div class="input-group mb-3 justify-content-center">
        <select name="" id="" v-model="selectedDepartment">
          <option value="all">All</option>
          <option v-for="(department, index) in departments" :key="index" :value="department.name">{{department.name}}</option>
        </select>
        <input type="text" class="form-control" placeholder="회원 검색" v-model="searchedName" @keypress.enter="changeSearchToggle()">
        <div class="input-group-append">
          <button class="btn btn-secondary ml-0" type="button" id="button-addon2" @click="changeSearchToggle()">검색</button>
        </div>
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
          <tr class="user-infos" @click="authorityModalUser(userinfo)" v-for="(userinfo, idx) in accessUserInfosForList" :key="idx">
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
      selectedDepartment: 'all',
      searchedName: '',
      searchToggle : false,
      perPage: 7,
      nowPage: 0,
    }
  },
  methods: {
    ...mapActions('account', ['getAccessUserInfo', 'getDepartments', 'filterUser']),
    ...mapMutations('account', ['SET_USER']),
    authorityModalUser(userdata) {
      const copydata = JSON.parse(JSON.stringify(userdata))
      this.SET_USER(copydata)
      $('#authorityModal').modal('show')
    },
    changeSearchToggle() {
      this.searchToggle = !this.searchToggle
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
  computed : {
    ...mapState('account', ['accessUserInfos', 'departments']),
    ...mapGetters('account', ['unAuthorizedUserCount']),
    rows() {
      return this.accessUserInfos.length
    },
    pages() {
      return Math.ceil(this.accessUserInfos.length/this.perPage)
    },
    accessUserInfosForList() {
      return this.accessUserInfos.slice(
        (this.nowPage) * this.perPage,
        (this.nowPage + 1) * this.perPage
      )
    },
  },
  created() {
    this.getAccessUserInfo()
    this.getDepartments()
  },
  watch : {
    selectedDepartment: function() {
      this.filterUser({ department : this.selectedDepartment, name : ''})
    },
    searchToggle: function() {
      this.filterUser({ department : this.selectedDepartment, name: this.searchedName })
      this.searchedName = ''
    }
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
  display: flex;
}

.user-infos {
  cursor: pointer;
}

.user-infos:hover {
  background-color: #e9e9e9;
}

td span {
  margin-right: 1vw;
}

#unauthorized-btn {
  background-color: #4ea1b5;
  color: white;
}

.page-navi {
  position: absolute;
  bottom: 0;
  left: 50%;
}

.input-group {
  width: 97%;
  margin-right: auto;
  margin-left: auto;
}

.page-item {
  cursor: pointer;
}
</style>