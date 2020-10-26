<template>
<div class="modal fade" id="signupModal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">회원가입</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div>
          part <input v-model="part" type="text">
        </div>
        <div>
          Name <input v-model="name" type="text">
        </div>
        <div>
          ID <input v-model="id" type="text">
        </div>
        <div v-if="idvalidate == 1">아이디는 영문,숫자 6~12자이내입니다.</div>
        <!-- 아이디 중복 체크 추가 필요 -->
        <div v-if="idvalidate == 2">가능한 아이디입니다.</div> 
        <div>
          PW <input v-model="pw1" type="password">
        </div>
        <div v-if="pwvalidate1 == 1">비밀번호는 문자+숫자+특수문자 8~16자입니다.</div>
        <div v-if="pwvalidate1 == 2">사용가능한 비밀번호입니다.</div>
        <div>
          PW Check <input v-model="pw2" type="password">
        </div>
        <div v-if="pwvalidate2 == 1">비밀번호가 일치하지 않습니다.</div>
        <div v-if="pwvalidate2 == 2">비밀번호가 일치합니다.</div>
        admin 
        <select name="product" id="cars">
          <option value="volvo">phone</option>
          <option value="saab">TV</option>
          <option value="mercedes">tablet</option>
          <option value="audi">earphone</option>
        </select>
        <span>  +</span>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary">회원가입</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
const idchk = /^[a-z0-9]{6,12}$/;
const pwchk = /^.*(?=^.{8,16}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$/;
export default {
  name : 'SignupModal',
  data() {
    return {
      part: '',
      name: '',
      pw1: '',
      pw2: '',
      id: '',
      pwvalidate1: 0, // 0 : nothing / 1 : 사용불가 비밀번호 / 2 : 사용가능 비밀번호
      pwvalidate2: 0, // 0 : nothing / 1 : 비밀번호 일치x / 2 : 비밀번호 일치 
      idvalidate: 0 // 0: nothing / 1: id검증 실패 / 2: id검증 성공
    }
  },
  methods: {
    closeModal() {
      this.part = ''
      this.name = ''
      this.id = ''
      this.pw1 = ''
      this.pw2 = ''
      this.pwvalidate1 = 0
      this.pwvalidate2 = 0
      this.idvalidate = 0
    }
  },
  watch: {
    id: function() {
      if (this.id.length === 0) {
        this.idvalidate = 0
      } else if (!idchk.test(this.id)) {
        this.idvalidate = 1
      } else if (idchk.test(this.id)) {
        this.idvalidate = 2
      }
    },
    pw1: function() {
      if (this.pw1.length === 0) {
        this.pwvalidate1 = 0
      } else if (!pwchk.test(this.pw1)) {
        this.pwvalidate1 = 1
      } else if (pwchk.test(this.pw1)) {
        this.pwvalidate1 = 2
      } else if (this.pw2.length === 0) {
        this.pwvalidate2 = 0
      } else if (this.pw1 !== this.pw2) {
        this.pwvalidate2 = 1
      } else if (this.pw1 === this.pw2) {
        this.pwvalidate2 = 2
      }
    },
    pw2: function() {
      if (this.pw2.length === 0) {
        this.pwvalidate2 = 0
      } else if (this.pw1 !== this.pw2) {
        this.pwvalidate2 = 1
      } else if (this.pw1 === this.pw2) {
        this.pwvalidate2 = 2
      }
    },
  },
  destroyed() {
    this.part = ''
    this.name = ''
    this.id = ''
    this.pw1 = ''
    this.pw2 = ''
    this.pwvalidate1 = 0
    this.pwvalidate2 = 0
    this.idvalidate = 0
  }

}
</script>

<style>

</style>