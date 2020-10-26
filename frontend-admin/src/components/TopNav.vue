<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" @click="onRoute('Main')">
      <img src="@/assets/icons/bootstrap.svg" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <a class="nav-link" id="manage-tab" data-toggle="tab" @click="onRoute('Manage')" role="tab" aria-controls="manage" aria-selected="true">Manage</a>
      </li>
      <li class="nav-item" role="presentation">
        <a class="nav-link" id="data-tab" data-toggle="tab" @click="onRoute('Data')" role="tab" aria-controls="data" aria-selected="false">Data</a>
      </li>
      <li class="nav-item" role="presentation">
        <a class="nav-link" id="contents-tab" data-toggle="tab" @click="onRoute('Contents')" role="tab" aria-controls="contents" aria-selected="false">Contents</a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
  },

}

</script>

<style scoped>
.navbar-brand:hover {
  cursor: pointer;
}

.nav-link:hover {
  cursor: pointer;
}

</style>
