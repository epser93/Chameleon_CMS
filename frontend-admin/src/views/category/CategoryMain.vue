<template>
<div class="container" v-if="categories">
  
  <div class="row justify-content-end" id="btn-add">
    <div class="col-4">
      <button type="button" class="btn btn-info" @click="onRoute('Category')">
        추가
      </button>
    </div>
  </div>

  <!-- 제품별 리스트 - 검색 조건 걸어줘야함 혹은 전체 보기로 기존의 것들을 출력할 수 있어야함 -->
  <div class="category-list">
    <table class="table">
      <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col">카테고리</th>
          <th scope="col">상태</th>
          <th scope="col">수정날짜</th>
          <th scope="col">상세보기</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(category, index) in categories" :key="index">
          <th scope="row"></th>
          <td>{{ category.name }}</td>
          <!-- 스위치 -->
          <td v-if="category.is_active">활성화
            <div class="custom-control custom-switch">
              <input type="checkbox" class="custom-control-input" :id="category.id" v-model="category.is_active" value="category.is_active" @click="changeActive(category.id)">
              <label class="custom-control-label" :for="category.id"></label>
            </div>
          </td>
          <td v-else>비활성화
            <div class="custom-control custom-switch">
              <input type="checkbox" class="custom-control-input" :id="category.id"  v-model="category.is_active" value="category.is_active" @click="changeActive(category.id)">
              <label class="custom-control-label" :for="category.id"></label>
            </div>
          </td>
          <!-- 스위치 -->
          <td>{{ category.update_date.slice(0,10) }}</td>
          <td><button type="button" class="btn btn-info" @click="onRoute('ItemMain')">더 보기</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  data() {
    return {
      
    }
  },

  computed: {
    ...mapState('category', ['categories'])
  },

  methods: {
    ...mapActions('category', ['getCategoryList', 'delCategory', 'postCategory']),
 
    onRoute(name) {
			this.$router.push({name:name}, () => {})
    },
    
    changeActive(idx){
      if (confirm("상태를 변경하시겠습니까?") == true){    //확인
          if (this.categories[idx].is_active) {
            this.delCategory(idx)
          }
          else {
            this.postCategory(idx)
          }
      } else {   //취소
          return;
      }
    }
    
  },

  created(){
    this.getCategoryList()
    this.checked = this.categories.is_active
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

#btn-add {
  margin-top: 50px;
  text-align: end;
}
</style>