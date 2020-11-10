<template>
<<<<<<< HEAD
  <div class="row">
    <div class="col-3 nav-container scroll">
      <SideBar v-if="productCategories"
      :categories="categoriess"
      :productCategories="productCategories"
      :mainCategories="mainCategories"
      ></SideBar>
    </div>
    <div class="contents-view col-9">
      <router-view class="scroll"></router-view>
=======
  <div class="container-fluid">
    <div class="row">
      <div class="col-3 nav-container scroll">
        <SideBar
        :categories="categoriess"
        :productCategories="findActive"
        ></SideBar>
      </div>
      <div class="contents-view col-9">
        <router-view class="scroll"></router-view>
      </div>
>>>>>>> 5c7be035428a5744c6e1b241e498bbb848b2f295
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'
import { mapActions, mapState} from 'vuex'

export default {
  data() {
    return {
      categoriess: ['Main', 'Product', 'Event', 'Notice'],
      mainCategories : [{ name: "대표 이미지", pathName : 'MainImage' }, { name: "추천제품", pathName : 'MainProduct' }],
      productCategories : null,
    }
  },
  components: {
    SideBar
  },
  computed: {
    ...mapState('category', ['categories']),
  },
  watch: {
    categories (val) {
      const tmpCategory = []
      for(let i=0; i<val.length; i++) {
        if(val[i].is_active) {
          tmpCategory.push(val[i])
        }
      }
     this.productCategories = tmpCategory
    }
  },
  methods: {
    ...mapActions('category', ['getCategoryList'])
  },
  created(){
    this.getCategoryList()
  },
}
</script>

<style scoped>
.row {
	height: calc(100vh - 135px);
}

.nav-container {
	/* border-right: 1px gray solid; */
	margin-bottom: 0;
  height: calc(100vh - 115px);
}

.scroll {
  overflow: scroll;
  overflow-x: hidden;
  height: calc(100vh - 135px);
}

.scroll::-webkit-scrollbar {
    width: 8px;
}
.scroll::-webkit-scrollbar-track {
    background:#eee;
}
.scroll::-webkit-scrollbar-thumb {
    background:lightgray;
}
.scroll::-webkit-scrollbar-thumb:hover {
    background:gray;
}
</style>