<template>
  <div class="modal" tabindex="-1" id="authorityModal">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">접근권한 부여</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div>
            <p class="tag">부서</p>
            <p>{{ modalinfos.department }}</p>
          </div>
          <hr>
          <div>
            <p class="tag">이름</p>
            <p>{{ modalinfos.name }}</p>
          </div>
          <hr>
          <div>
            <p class="tag">아이디</p>
            <p>{{ modalinfos.id }}</p>
          </div>
          <hr>
          <div>
            <p class="tag">권한</p>
            <label class="chkbox-label" v-for="(authority, idx) in authorities" :key="idx">
              <input type="checkbox" :value="authority" v-model="modalinfos.authority">
              {{ authority }}
            </label>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">닫기</button>
          <button type="button" class="btn btn-primary" @click="onRoute('User')">권한 수정</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name : "AuthorityModal",
  props: ["modalinfos"],
  data() {
    return {
      checkedAuthorities : [],
      authorities : ["Product", "Main+Notice", "Event"]
    }
  },
  // computed: {
  //   getCheckedAuthorites() {
  //     this.checkedAuthorities = this.modalinfos.authority
  //     return this.check
  //   }
  // },
  methods: {
    onRoute(name) {
      $('#authorityModal').modal('hide')
      this.$router.push({ name : name }, () => {})
    },
    getInitialData() {
      this.checkedAuthorities = this.modalinfos.authority
    }
  },
  created() {
    // this.getInitialData()
  }
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