<template>
  <div class="modal fade" tabindex="-1" id="unauthorizedUser">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">가입승인</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">부서</th>
                <th scope="col">이름</th>
                <th scope="col">아이디</th>
                <th scope="col">승인여부</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(user, index) in unAccessedUserInfos" :key="index">
                <th scope="row">{{ index+1 }}</th>
                <td>{{ user.department.name }}</td>
                <td>{{ user.first_name }}</td>
                <td>{{ user.username}}</td>
                <td>
                  <button type="button" class="btn btn-outline-primary approve-btn" @click="approve(user.id)">승인</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">닫기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  data() {
    return {

    }
  },
  methods: {
    ...mapActions('account', ['getUnAccessUserInfo', 'approveAccess', 'getAccessUserInfo']),
    approve(userPk) {
      this.approveAccess(userPk)
    },
  },
  computed: {
    ...mapState('account', ['unAccessedUserInfos'])
  },
  created() {
    this.getUnAccessUserInfo()
  }
}
</script>

<style scoped>
.approve-btn {
  margin-right: 1vw;
}
</style>