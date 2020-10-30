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
        <form class="signup-form" autocomplete="on">
          <div>
            <div>Department</div>
            <select name="department" id="department" v-model="part">
              <option disabled value="">Please select one</option>
              <option v-for="(department, index) in departments" :key="index" :value="department">{{ department }}</option>
            </select>
          </div>
          <div>
            <div>Name</div>
            <input v-model="name" type="text">
          </div>
          <div>
            <div>
              ID
              <span class="validate-fail" v-if="idValidate == 1">아이디는 영문,숫자 6~12자이내입니다.</span>
              <span class="validate-success" v-if="idValidate == 2">가능한 아이디입니다.</span> 
            </div>
            <input v-model="id" type="text">
          </div>
          <div>
            <div>
              PW
              <span class="validate-fail" v-if="pwValidate1 == 1">비밀번호는 문자+숫자+특수문자 8~16자입니다.</span>
              <span class="validate-success" v-if="pwValidate1 == 2">사용가능한 비밀번호입니다.</span>
            </div>
            <input v-model="pw1" type="password" autocomplete="off">
          </div>
          <div>
            <div>
              PW Check
              <span class="validate-fail" v-if="pwValidate2 == 1">비밀번호가 일치하지 않습니다.</span>
              <span class="validate-success" v-if="pwValidate2 == 2">비밀번호가 일치합니다.</span>
            </div>
            <input v-model="pw2" type="password" autocomplete="off">
          </div>
          <div>
          <div>Access<span @click="plusAccess" class="plus-access">  +</span><span @click="minusAccess" class="minus-access">  -</span></div> 
            <select v-for="index in selectIdx" :key="index" name="access" id="access" v-model="selected">
              <option disabled value="">Please select one</option>
              <option v-for="(access, index) in accesses" :key="index" :value="access">{{ access }}</option>
            </select>
          </div>
      </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" @click="onRoute('Manage')">회원가입</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import $ from "jquery";
const idchk = /^[a-z0-9]{6,12}$/;
const pwchk = /^.*(?=^.{8,16}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$/;
export default {
  name : 'SignupModal',
  data() {
    return {
      selectIdx: 1,
      departments: ['생산관리', '영업', '재무', '마케팅', '전산', '개발', '홍보'],
      accesses: ['phone', 'TV', 'tablet', 'earphone'],
      part: '',
      name: '',
      pw1: '',
      pw2: '',
      id: '',
      selected: '',
      pwValidate1: 0, // 0 : nothing / 1 : 사용불가 비밀번호 / 2 : 사용가능 비밀번호
      pwValidate2: 0, // 0 : nothing / 1 : 비밀번호 일치x / 2 : 비밀번호 일치 
      idValidate: 0 // 0: nothing / 1: id검증 실패 / 2: id검증 성공
    }
  },
  methods: {
    plusAccess() {
      this.selectIdx += 1
    },
    minusAccess() {
      this.selectIdx -= 1
    },
    initializeParameter() {
      this.part = ''
      this.name = ''
      this.id = ''
      this.pw1 = ''
      this.pw2 = ''
      this.selected = []
      this.pwValidate1 = 0
      this.pwValidate2 = 0
      this.idValidate = 0
    },
    onRoute(name) {
      $('#signupModal').modal('hide')
      this.$router.push({ name : name }, () => {})
      this.initializeParameter()
    },
  },
  watch: {
    id: function() {
      if (this.id.length === 0) {
        this.idValidate = 0
      } else if (!idchk.test(this.id)) {
        this.idValidate = 1
      } else if (idchk.test(this.id)) {
        this.idValidate = 2
      }
    },
    pw1: function() {
      if (this.pw1.length === 0) {
        this.pwValidate1 = 0
      } else if (!pwchk.test(this.pw1)) {
        this.pwValidate1 = 1
      } else if (pwchk.test(this.pw1)) {
        this.pwValidate1 = 2
      } else if (this.pw2.length === 0) {
        this.pwValidate2 = 0
      } else if (this.pw1 !== this.pw2) {
        this.pwValidate2 = 1
      } else if (this.pw1 === this.pw2) {
        this.pwValidate2 = 2
      }
    },
    pw2: function() {
      if (this.pw2.length === 0) {
        this.pwValidate2 = 0
      } else if (this.pw1 !== this.pw2) {
        this.pwValidate2 = 1
      } else if (this.pw1 === this.pw2) {
        this.pwValidate2 = 2
      }
    },
  },
}
</script>

<style scoped>
input {
  margin-bottom : 2vh;
  width: 100%;
  /* border-radius: 5px; */
  /* border: solid 2px grey; */
  border-right-style: none;
  border-left-style: none;
  border-top-style: none;
}
input:focus {
  outline: none;
}

#access {
  width: 100%;
}

#department {
  width: 100%;
  margin-bottom: 2vh;
}

.plus-access {
  cursor: pointer;
}

.signup-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.validate-fail {
  color: red;
}

.validate-success {
  color: green;
}
</style>