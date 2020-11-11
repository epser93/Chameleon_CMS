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
            <p class="mb-2">부서</p>
            <select name="department" id="department" v-model="part">
              <option disabled value="">부서를 선택해 주세요.</option>
              <option v-for="(department, index) in departments" :key="index" :value="department">{{ department.name }}</option>
            </select>
          </div>
          <div>
            <p>이름</p>
            <input v-model="name" type="text">
          </div>
          <div>
            <p>사번</p>
            <input v-model="employeeNumber" type="text">
          </div>
          <div>
            <p>이메일</p>
            <input v-model="email" type="email">
          </div>
          <div>
            <div>
              아이디
              <span class="validate-fail" v-if="idValidate == 1">아이디는 영문,숫자 6~12자이내입니다.</span>
              <span class="validate-temp" v-if="idValidate == 2">중복체크를 해주세요.</span> 
              <span class="validate-success" v-if="idValidate == 3">사용가능한 아이디입니다.</span>
              <span class="validate-fail" v-if="idValidate == 4">중복된 아이디입니다.</span>
            </div>
            <input v-model="id" type="text">
            <button type="button" class="btn btn-outline-primary" @click="isDuplicate(id)">중복확인</button>
          </div>
          <div>
            <div>
              비밀번호
              <span class="validate-fail" v-if="pwValidate1 == 1">비밀번호는 문자+숫자+특수문자 8~16자입니다.</span>
              <span class="validate-success" v-if="pwValidate1 == 2">사용가능한 비밀번호입니다.</span>
            </div>
            <input v-model="pw1" type="password" autocomplete="off">
          </div>
          <div>
            <div>
              비밀번호 확인
              <span class="validate-fail" v-if="pwValidate2 == 1">비밀번호가 일치하지 않습니다.</span>
              <span class="validate-success" v-if="pwValidate2 == 2">비밀번호가 일치합니다.</span>
            </div>
            <input v-model="pw2" type="password" autocomplete="off">
          </div>
      </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" @click="signup()">회원가입</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import SERVER from '@/api/drf'
import axios from 'axios'
import $ from "jquery";
const idchk = /^[a-z0-9]{6,12}$/;
const pwchk = /^.*(?=^.{8,16}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$/;
export default {
  name : 'SignupModal',
  data() {
    return {
      employeeNumber : '',
      email : '',
      part: '',
      name: '',
      pw1: '',
      pw2: '',
      id: '',
      pwValidate1: 0, // 0 : nothing / 1 : 사용불가 비밀번호 / 2 : 사용가능 비밀번호
      pwValidate2: 0, // 0 : nothing / 1 : 비밀번호 일치x / 2 : 비밀번호 일치 
      idValidate: 0, // 0: nothing / 1: id검증 실패 / 2: id검증 성공 / 3: id 중복 pass / 4 : id 중복 fail
      isDuplicateId: null
    }
  },
  methods: {
    ...mapActions('account', ['getDepartments']),
    initializeParameter() {
      this.part = ''
      this.name = ''
      this.id = ''
      this.pw1 = ''
      this.pw2 = ''
      this.employeeNumber = ''
      this.email = ''
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
    signup() {
      const signUpData = {
        username : this.id,
        password1 : this.pw1,
        password2 : this.pw2,
        department : this.part.name,
        email : this.email,
        first_name: this.name,
        employee_number : this.employeeNumber
      }
      console.log(signUpData)
      axios.post(SERVER.URL + SERVER.ROUTER.signup, signUpData)
        .then(() => {
          this.onRoute("Login")
          alert('회원가입이 완료되었습니다. 관리자 승인후 로그인해주세요')
        })
        .catch(error => {
          console.log(error.response)
          alert(error.response.data.message)
        })
    },
    isDuplicate(account) {
      axios.get(SERVER.URL + SERVER.ROUTER.accountvalidation + `?type=id&content=${account}`)
        .then(res => {
          alert(res.data.message)
          this.isDuplicateId = false
        })
        .catch(error => {
          alert(error.response.data.message)
          if (error.response.data.message === '존재하는 아이디 입니다.') {
            this.isDuplicateId = true
          }
        })
    }
  },
  watch: {
    isDuplicateId: function() {
      if (this.isDuplicateId === false) {
        this.idValidate = 3
      } else if (this.isDuplicateId === true) {
        this.idValidate = 4
      }
    },
    idValidate: function() {
      if (this.idValidate !== (3 || 4)) {
        this.isDuplicateId = null
      }
    },
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
  computed: {
    ...mapState('account', ['departments'])
  },
  created() {
    this.getDepartments()
  }
}
</script>

<style scoped>
p {
  margin: 0;
}
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

.validate-temp {
  color: orange;
}

.modal-footer {
  margin-left: auto;
  margin-right: auto;
  border-top: none;
  padding: 0;
  margin-bottom: 30px;
}

.btn {
  background-color: #56b596;
  border: none;
}
</style>