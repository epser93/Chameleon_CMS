<template>
  <div v-if="categories" class="container pl-0">
    <div class="table-container">
      <div class="ml-3 mt-3 mb-3">
          <button type="button" class="btn btn-info ml-3 mb-3" @click="onRoute('ProductCG')">
            생성
          </button>
      <!-- 제품별 리스트 - 검색 조건 걸어줘야함 혹은 전체 보기로 기존의 것들을 출력할 수 있어야함 -->
        <table class="table">
          <thead>
            <tr>
              <th scope="col"></th>
              <th scope="col">카테고리</th>
              <th scope="col">상태</th>
              <th scope="col">수정날짜</th>
              <th scope="col">상세보기</th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(category, index) in categories" :key="index">
              <th scope="row align-items-center"></th>
              <!-- {{ category }} -->
              <td>{{ category.name }}</td>
              <!-- 스위치 -->
              <td v-if="category.is_active">
                <span class="badge badge-success" @click="changeActive(category)">활성화</span>
              </td>
              <td v-else>
                <span class="badge badge-danger" @click="changeActive(category)">비활성화</span>
              </td>
              <!-- 스위치 -->
              <td>{{ category.update_date.slice(0,10) }}</td>
              <td><button type="button" class="btn btn-info" @click="onDetail(category.id)">보기</button></td>
              <td><button type="button" class="btn btn-secondary" @click="onUpdate(category.id)">수정</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  props:[''],

  data() {
    return {
    }
  },

  computed: {
    ...mapState('category', ['categories'])
  },

  methods: {
    ...mapActions('category', ['delCategory', 'postCategory']),
    // ...mapMutations('category', ['SET_CATEGORY']),
    onUpdate(cid) {
      this.$router.push({name:'ProductCGupdate', params:{cid: cid, update: 'update'}})
    },
    onRoute(name) {
      console.log("눌림")
			this.$router.push({name:name}, () => {})
    },
    onDetail(cid) {
      this.$router.push({name:'ProductItemMain', params:{cid: cid}})
    },
    
    changeActive(category){
      if (confirm("상태를 변경하시겠습니까?") == true){    //확인
        if (category.is_active) {
          this.delCategory(category.id)
        }
        else {
          this.postCategory(category.id)
        }
      }
    }
    
  },

  created(){
    // this.getCategoryList()
    // this.checked = this.categories.is_active
  }
}
</script>

<style scoped>
.btn {
  margin-left: 10px
}

.category-list {
  margin-top: 20px;
}

td {
  padding-top: 16px;
  padding-bottom: 10px;
}

#btn-add {
  margin-top: 50px;
  text-align: end;
}

span {
  cursor: pointer;
  margin-top: 4px;
}
</style>