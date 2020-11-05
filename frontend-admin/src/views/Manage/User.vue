<template>
  <div class="container-fluid">
    <div class="table-container">
      <div class="unauthorized">
        <button type="button" class="btn btn-info" data-toggle="modal" data-target="#unauthorizedUser">
          미승인 회원 <span class="badge badge-light">4</span>
        </button>
      </div>
      <UnauthorizedUser></UnauthorizedUser>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">부서</th>
            <th scope="col">이름</th>
            <th scope="col">아이디</th>
            <th scope="col">권한</th>
          </tr>
        </thead>
        <tbody>
          <tr class="user-infos" @click="giveAuthority(userinfo)" v-for="(userinfo, idx) in userinfos" :key="idx">
            <th scope="row">{{ idx+1 }} </th>
            <td>{{ userinfo.department.name }}</td>
            <td>{{ userinfo.first_name }}</td>
            <td>{{ userinfo.username }}</td>
            <td>{{ getAuthority(userinfo) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <AuthorityModal :modalinfos="modalinfos"></AuthorityModal>
  </div>
</template>

<script>
import AuthorityModal from '@/components/AuthorityModal'
import UnauthorizedUser from'@/components/UnauthorizedUser'
import $ from 'jquery'
import axios from 'axios'
import SERVER from '@/api/drf'
export default {
  components: {
    AuthorityModal,
    UnauthorizedUser
  },
  data() {
    return {
      modalinfos : [],
      userinfos: []
    }
  },
  methods: {
    giveAuthority(userinfo) {
      console.log(userinfo)
      this.modalinfos = userinfo
      $('#authorityModal').modal('show')
    },

    sliceAuthorities(authorities) {
      let authoritiyList = ""
      for (let i=0; i<authorities.length; i++) {
        if (i === authorities.length - 1) {
          authoritiyList += authorities[i]
        } else {
          authoritiyList += authorities[i] + ', '
        }
      }
      return authoritiyList
    },

    getAccessUserInfo() {
      const config = {
        headers: {
          'Authorization' : 'Token ' + this.$cookies.get('auth-token')
        }
      }
      axios.get(SERVER.URL + SERVER.ROUTER.usersearch + '?type=all', config)
        .then(res => {
          this.userinfos = res.data
          console.log(this.userinfos)
        })
        .catch(error => console.log(error))
    },
    getAuthority(userinfo) {
      let authority = ""
      if (userinfo.is_logger) {
        authority += "Log "
      }
      if (userinfo.is_eventer) {
        authority += "Event "
      }
      if (userinfo.is_producter) {
        authority += "Product "
      }
      if (userinfo.is_marketer) {
        authority += "Main + Notice "
      }
      return authority
    }
  },
  computed : {

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

.user-infos {
  cursor: pointer;
}

.user-infos:hover {
  background-color: #e9e9e9;
}

.unauthorized {
  display: flex;
}
</style>