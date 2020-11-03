<template>
  <div class="box">
    <div class="div-A">
      <div class="cms-name">
        <div>CHEIL</div>
        <div>CMS</div>
      </div>
      <div class="id">
        <label for="id">ID</label>
        <input type="text" v-model="id">
      </div>
      <div class="pw">
        <label for="pw">pw</label>
        <input type="password" v-model="pw">
      </div>
      <div class="login-btn" @click="login()">Login</div>
      <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#signupModal">
        회원가입
      </button>
      <SignupModal/>
    </div>
    <div class="div-B">
      <img class="company-image" src="../assets/login1.png" alt="">
    </div>
  </div>
</template>

<script>
import SERVER from '@/api/drf'
import axios from 'axios'
import SignupModal from '@/components/SignupModal'
export default {
  name: 'Login',
  components : {
    SignupModal,
  },
  data() {
    return {
      id: null,
      pw : null,
      is_superuser: false
    }
  },
  methods: {
    login() {
      const loginData = {
        username : this.id,
        password : this.pw
      }
      axios.post(SERVER.URL + SERVER.ROUTER.login, loginData)
        .then(res => {
          this.$cookies.set('auth-token', res.data.key)
          let token = res.data.key
          this.getUserInfo(token)
          console.log(this.is_superuser)
          if (this.is_superuser){
            this.$router.push({ name : 'Manage'})
          } else {
            this.$router.push({ name : 'Data'})
          }
          })
        .catch(error => console.log(error.response))
    },

    getUserInfo(token) {
      const config = {
        headers: {
          'Authorization' : 'Token ' + token
        }
      }
      axios.get(SERVER.URL + SERVER.ROUTER.userinfo, config)
        .then(res => {
          console.log(res)
          this.is_superuser = res.data.is_superuser
        })
        .catch(error => console.log(error.response))
    }
  }
}
</script>

<style scoped>
.box {
  width: 100vw;
  height:100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.div-A {
  display: flex;
  width : 40%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.div-B {
  width: 60%;
}

.cms-name {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 50px;
  margin-bottom: 2vh;
}

.id {
  margin-bottom: 2vh;
}

.pw {
  margin-bottom: 2vh;
}

.login-btn {
  margin-bottom: 2vh;
  cursor: pointer;
}

.company-image {
  border-left: 5px gray solid;
  width: 100%;
  height: 100vh;
}
</style>