<template>
  <div class="container-fluid">
    <div class="row">
      <div class="login-left col-12 col-lg-5 justify-content-center">
        <div class="cms-name">
          <h1 class="chamaeleon"><span class="upper-c">C</span>hamaeleon</h1>
          <h1 class="cms">CMS</h1>
        </div>
        <div class="mb-4">
          <div class="id">
            <label for="id">ID</label>
            <input type="text" v-model="id"  @keydown.enter="login()">
          </div>
          <div class="pw">
            <label for="pw">PW</label>
            <input type="password" v-model="pw"  @keydown.enter="login()">
          </div>
        </div>
        <div class="login-signup">
          <button type="button" class="btn" @click="login()">
            Login
          </button>
          <p class="signup" data-toggle="modal" data-target="#signupModal">Sign Up</p>
          <SignupModal/>
        </div>
      </div>
      <div class="login-right d-none d-sm-none d-md-none d-lg-block col-7">
        <img class="company-image" src="../assets/login1.png" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import SignupModal from '@/components/SignupModal'

import { mapActions } from 'vuex'

export default {
  name: 'Login',
  components : {
    SignupModal,
  },
  data() {
    return {
      id: null,
      pw : null,
    }
  },
  methods: {
    ...mapActions('account', ['userLogin']),
    login() {
      const loginData = {
        username : this.id,
        password : this.pw
      }
      this.userLogin(loginData)
    },
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

h1 {
  font-size: 60px;
  font-family: 'Raleway', sans-serif;
  color: grey;
}

.chamaeleon {
  color: #4ea2b6;
}

.upper-c {
  color: #4372c4;
}

.cms {
  color: #c78f58;
}

.login-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
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
  border-left: 4px #4fa2b6 solid;
  width: auto;
  height: 100vh;
}

.btn {
  background-color: #56b596;
  color: white;
  margin-bottom: 10px;
  margin-right: auto;
  margin-left: auto;
  display: block;
}

.signup {
  color: #4472c5;
  cursor: pointer;
  text-align: center;
}

input {
  border: 2px solid grey;
  border-radius: 5px;
  width: 100%;
}

@media screen and (max-width: 992px) {
  .login-left {
    display: block;
    margin-top: 160px;
  }
}
</style>