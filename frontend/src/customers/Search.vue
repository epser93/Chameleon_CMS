<template>
  <div>
    <search-bar/>
    <router-view/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'

export default {
  name: 'Search',
  components: {
    SearchBar,
  }
}
</script>
<style scoped>
</style>
