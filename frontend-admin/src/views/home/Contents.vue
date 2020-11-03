<template>
  <div class="row">
    <div class="col-3">
      <SideBar :categories="categories"></SideBar>
    </div>
    <div class="col-9">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'

export default {
  data() {
    return {
      categories: ['Main', 'Product', 'Event', 'Notice']
    }
  },
  components: {
    SideBar
  }
}
</script>

<style scoped>
.row {
	height: calc(100vh - 135px);
}

.nav-container {
	border-right: 1px gray solid;
	margin-bottom: 0;
}
</style>