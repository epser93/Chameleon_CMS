<template>
  <div id="searchMain">
    <div class="input-group pt-2 pb-4 mx-auto" id="searchContent">
      <input v-model="search" type="text" class="form-control" placeholder="Search Content" aria-label="Recipient's username" aria-describedby="basic-addon2" @keydown.enter="onSearch()">
      <div class="input-group-append">
        <button class="btn btn-outline-light" type="button" @click="onSearch()">Search</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      search: ''
    }
  },
  methods: {
    onSearch() {
      this.$router.push({name:'CustomerSearch', params:{text: this.search}}, () => {})
		},
  },
  created() {
    this.search = this.$route.params.text
  }
}
</script>

<style>
#searchMain {
  padding-top: 18px;
  background-color: #26272b;
}

#searchContent {
  width: 60%;
  padding-top: 18px;
}
</style>