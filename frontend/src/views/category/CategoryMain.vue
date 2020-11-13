<template>
  <div v-if="categories" class="container pl-0">
    <div class="table-container">
      <div class="mt-3 mb-3">
        <div class="row align-items-center mt-1 mb-3">
          <h5 class="mb-0 ml-3">카테고리</h5>
          <button type="button" class="btn btn-info btn-sm" @click="onRoute('ProductCG')">추가</button>
        </div>
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
            <tr v-for="(category, index) in categoriesForList" :key="index">
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
              <td><button type="button" class="btn btn-outline-secondary btn-sm" @click="onDetail(category.id)">보기</button></td>
              <td><button type="button" class="btn btn-warning btn-sm" @click="onUpdate(category.id)">수정</button></td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="page-navi justify-content-center">
        <nav aria-label="Page navigation example">
          <ul v-if="pages == 0" class="pagination">
            <li class="page-item">
              <img src="@/assets/icons/caret-left.svg" width="26" height="26" title="caret-left" @click="prevPage()">
            </li>
            <p> {{ nowPage + 1 }}  / {{ pages + 1}} </p>
            <li class="page-item">
              <img src="@/assets/icons/caret-right.svg" width="26" height="26" title="caret-right" @click="nextPage()">
            </li>
          </ul>
          <ul v-else class="pagination">
            <li class="page-item">
              <img v-if="nowPage == 0" src="@/assets/icons/caret-left.svg" width="26" height="26" title="caret-left" @click="prevPage()">
              <img v-else src="@/assets/icons/caret-left-fill.svg" width="26" height="26" title="caret-left-fill" @click="prevPage()">
            </li>
            <p> {{ nowPage + 1 }}  / {{ pages }} </p>
            <li class="page-item">
              <img v-if="nowPage == (pages-1)" src="@/assets/icons/caret-right.svg" width="26" height="26" title="caret-right" @click="nextPage()">
              <img v-else src="@/assets/icons/caret-right-fill.svg" width="26" height="26" title="caret-right-fill" @click="nextPage()">
            </li>
          </ul>
        </nav>
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
      perPage: 7,
      nowPage: 0,
    }
  },

  computed: {
    ...mapState('category', ['categories']),
    rows() {
      return this.categories.length
    },
    pages() {
      return Math.ceil(this.categories.length/this.perPage)
    },
    categoriesForList() {
      return this.categories.slice(
        (this.nowPage) * this.perPage,
        (this.nowPage + 1) * this.perPage
      )
    },
  },

  methods: {
    ...mapActions('category', ['delCategory', 'postCategory']),
    // ...mapMutations('category', ['SET_CATEGORY']),
    onUpdate(cid) {
      this.$router.push({name:'ProductCGupdate', params:{cid: cid, update: 'update'}})
    },
    onRoute(name) {
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
    },
      prevPage() {
      if (this.nowPage > 0) {
        this.nowPage -= 1
      }
    },
    nextPage() {
      if (this.nowPage < this.pages-1) {
        this.nowPage += 1
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

.page-navi {
  position: absolute;
  bottom: 0;
  left: 50%;
}

.page-item {
  cursor: pointer;
}
</style>