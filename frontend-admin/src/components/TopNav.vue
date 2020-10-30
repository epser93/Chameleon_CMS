<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" @click="onRoute('Main')">
      <img src="@/assets/logo.png" width="200" height="100%" class="d-inline-block align-top" alt="" loading="lazy">
    </a>
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
export default {
  name: 'Header',
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
  },
  mounted() {
    this.fixTabs()
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

</style>
