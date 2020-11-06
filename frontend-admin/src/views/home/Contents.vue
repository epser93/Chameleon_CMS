<template>
  <div class="row">
    <div class="col-3 nav-container">
      <SideBar
      :categories="categories"
      :productCategories="productCategories"
      ></SideBar>
    </div>
    <div class="col-9 pl-0">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'

export default {
  data() {
    return {
      categories: ['Main', 'Product', 'Event', 'Notice'],
      productCategories: ['노트북', '스마트폰', '냉장고']
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
  height: calc(100vh - 115px);
}
</style>