<template>
  <div class="modal" tabindex="-1" id="authorityModal">
    <div class="modal-dialog" v-if="authorityModalUser">
      <div class="modal-content">
        <div class="modal-header" >
          <h5 class="modal-title">접근권한 부여</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div>
            <p class="tag">부서</p>
            <p>{{ authorityModalUser.department.name }}</p>
          </div>
          <hr>
          <div>
            <p class="tag">이름</p>
            <p>{{ authorityModalUser.first_name }}</p>
          </div>
          <hr>
          <div>
            <p class="tag">아이디</p>
            <p>{{ authorityModalUser.username }}</p>
          </div>
          <hr>
          <div> 
            <p class="tag">권한</p>
            <div class="row justify-content-center ml-1">
              <label class="chkbox-label">
                <input type="checkbox" :value="authorityModalUser.is_eventer" v-model="authorityModalUser.is_eventer">
                Event
              </label>
              <label class="chkbox-label">
                <input type="checkbox" :value="authorityModalUser.is_logger" v-model="authorityModalUser.is_logger">
                Log
              </label>
              <label class="chkbox-label">
                <input type="checkbox" :value="authorityModalUser.is_producter" v-model="authorityModalUser.is_producter">
                Product
              </label>
              <label class="chkbox-label">
                <input type="checkbox" :value="authorityModalUser.is_marketer" v-model="authorityModalUser.is_marketer">
                Main + Notice
              </label>
            </div>
          </div>
        </div>
        <div class="modal-footer justify-content-center">
          <button type="button" class="btn btn-primary" @click="onRoute('User'), giveAuthority()">권한 수정</button>
          <button type="button" class="btn btn-secondary" data-dismiss="modal">취소</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import { mapActions, mapState } from 'vuex'

export default {
  name : "AuthorityModal",
  data() {
    return {
  
    }
  },
  methods: {
    ...mapActions('account', ['giveAuthorities']),
    giveAuthority() {
      let authorityInfo = {
        is_producter : this.authorityModalUser.is_producter,
        is_eventer : this.authorityModalUser.is_eventer,
        is_marketer : this.authorityModalUser.is_marketer,
        is_logger : this.authorityModalUser.is_logger
      }
      this.giveAuthorities(authorityInfo)
    },
    onRoute(name) {
      $('#authorityModal').modal('hide')
      this.$router.push({ name : name }, () => {})
    },
  },
  computed: {
    ...mapState('account', ['authorityModalUser']),
  },
  created() {

  },
}
</script>

<style scoped>
.chkbox-label {
  margin-right : 3vw;
}

.tag {
  font-size: 20px;
  font-weight: bold;
}
</style>