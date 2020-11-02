<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="logo-section">
      <a class="navbar-brand" @click="onRoute('Main')">
        <img src="@/assets/logo.png" width="200" height="100%" class="d-inline-block align-top" alt="" loading="lazy">
      </a>
      <div class="user-info">{{ user }}님 환영합니다.</div>
      <div class="logout-btn" @click="logout()">로그아웃</div>
    </div>
    <div class="nav-tabs-container">
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
          <a ref="Manage" class="nav-link" id="manage-tab" data-toggle="tab" @click="onRoute('Manage')" role="tab" aria-controls="manage" aria-selected="true">Manage</a>
        </li>
        <li class="nav-item" role="presentation">
          <a ref="Data" class="nav-link" id="data-tab" data-toggle="tab" @click="onRoute('Data')" role="tab" aria-controls="data" aria-selected="false">Data</a>
        </li>
        <li class="nav-item" role="presentation">
          <a ref="Contents" class="nav-link" id="contents-tab" data-toggle="tab" @click="onRoute('Contents')" role="tab" aria-controls="contents" aria-selected="false">Contents</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import SERVER from '@/api/drf'
import axios from 'axios'
export default {
  name: 'Header',
  data() {
    return {
      user: null
    }
  },
  methods: {
    onRoute(name) {
      // this.activeTab()
      this.$router.push({name: name}, () => {})
    },
    fixTabs() {
      if (this.$route.matched[1].name === "Manage") {
        this.$refs.Manage.classList.add('active')
      } else if (this.$route.matched[1].name === "Data") {
        this.$refs.Data.classList.add('active')
      } else {
        this.$refs.Contents.classList.add('active')
      }
    },
    getUserInfo() {
      const token = this.$cookies.get('auth-token')
      const config = {
        headers: {
          'Authorization' : 'Token ' + token
        }
      }
      axios.get(SERVER.URL + SERVER.ROUTER.userinfo, config)
        .then(res => {
          this.user = res.data.username
        })
        .catch(error => console.log(error.response))
    },
    logout() {
      const token = this.$cookies.get('auth-token')
      const config = {
        headers: {
          'Authorization' : 'Token ' + token
        }
      }
      axios.post(SERVER.URL + SERVER.ROUTER.logout, null, config)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.$router.push({name : 'Login'})
        })
        .catch(error => console.log(error.response))
    }
  },
  mounted() {
    this.fixTabs()
  },
  created() {
    this.getUserInfo()
  }


}

</script>

<style scoped>
.navbar-brand:hover {
  cursor: pointer;
}

.nav-link:hover {
  cursor: pointer;
}

nav {
  display: flex;
  width: 100%;
  justify-content: space-between;
  padding-bottom: 0;
}

.nav-tabs-container {
  align-self: flex-end;
}

.nav-tabs {
  font-size: 30px;
  color: black;
  height : 80%;
  margin-right: 3vw;
}

.nav-link {
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  padding-left: 60px;
  padding-right: 60px;
  padding-top: 20px;
  padding-bottom: 20px;
  text-decoration: none;
  color: black;
}

.logo-section {
  display: flex;
  align-items: center;
}

.user-info {
  font-size: 25px;
  margin-left: 3vw;
  margin-right: 2vw
}

.logout-btn {
  cursor: pointer;
  /* padding: 15px; */
  /* border: 1px black solid; */
  /* border-radius: 10px; */
}
</style>
