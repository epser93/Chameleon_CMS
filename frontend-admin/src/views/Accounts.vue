<template>
  <div class="box">
    <div class="div-A">
      <div class="cms-name">
        <div>CHEIL</div>
        <div>CMS</div>
      </div>
      <div class="id">
        <label for="id">ID</label>
        <input type="text">
      </div>
      <div class="pw">
        <label for="pw">pw</label>
        <input type="text">
      </div>
      <div class="login-btn">Login</div>
      <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#signupModal">
        회원가입
      </button>
      <SignupModal/>
    </div>
    <div class="div-B">
      <img class="company-image" src="../assets/cat.jpg" alt="">
    </div>
  </div>
</template>

<script>
import SignupModal from '@/components/SignupModal'
export default {
  name: 'Accounts',
  components : {
    SignupModal
  }
}
</script>

<style>
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
  font-size: 30px;
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
}

.company-image {
  border-left: 1px black solid;
  width: 100%;
  height: 100vh;
}
</style>