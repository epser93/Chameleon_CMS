<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="row logo-section">
      <a class="navbar-brand" @click="onRoute('Main')">
        <img src="@/assets/logo.png" width="200" height="100%" class="d-inline-block align-top" alt="" loading="lazy">
      </a>
      <div class="row align-items-center mt-4">
        <p class="user-info">{{ userInfo.username }}님 환영합니다.</p>
        <button type="button" class="btn btn-secondary btn-sm ml-2" @click="logout()">로그아웃</button>
      </div>
    </div>
    <div class="nav-tabs-container">
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li v-if="userInfo.is_superuser || userInfo.is_logger" class="nav-item" role="presentation">
          <a class="nav-link Manage" id="manage-tab" data-toggle="tab" @click="onRoute('Manage')" role="tab" aria-controls="manage" aria-selected="true">Manage</a>
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link Data" id="data-tab" data-toggle="tab" @click="onRoute('Data')" role="tab" aria-controls="data" aria-selected="false">Data</a>
        </li>
        <li class="nav-item" role="presentation">
          <a class="nav-link Contents" id="contents-tab" data-toggle="tab" @click="onRoute('Contents')" role="tab" aria-controls="contents" aria-selected="false">Contents</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'Header',
  data() {
    return {

    }
  },
  computed: {
    ...mapState('account', ['userInfo'])
  },
  methods: {
    ...mapActions('account', ['getUserInfo', 'logout']),
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
    fixTabs() {
      document.querySelector('.' + this.$route.matched[2].name).classList.add('active')
    },
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
  font-size: 26px;
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
  margin-bottom: 0;
}
</style>
