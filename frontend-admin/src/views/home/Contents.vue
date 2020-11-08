<template>
  <div class="row">
    <div class="col-3 nav-container">
      <SideBar
      :categories="categoriess"
      :productCategories="findActive"
      ></SideBar>
    </div>
    <div class="col-9">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'
import { mapActions, mapState } from 'vuex'

export default {
  data() {
    return {
      categoriess: ['Main', 'Product', 'Event', 'Notice'],
    }
  },
  components: {
    SideBar
  },
  computed: {
    ...mapState('category', ['categories']),
    
    findActive() {
      const tmpCategory = []
      for(let i=0; i<this.categories.length; i++) {
        if(this.categories[i].is_active) {
          tmpCategory.push(this.categories[i])
        }
      }
      return tmpCategory
    }
    
  },
  methods: {
    ...mapActions('category', ['getCategoryList'])
  },
  created(){
    this.getCategoryList()
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