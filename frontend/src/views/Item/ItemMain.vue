<template>
<div class="container pl-0" v-if="items != null && category != null">
  <div class="table-container mt-0">
    <div class="d-flex align-items-center justify-content-between">
      <div class="row align-items-center">
        <h5 class="mb-0 ml-3">{{ category.name }}</h5>
        <button type="button" class="btn btn-info btn-sm" @click="onCreate('ProductItemCreate')">추가</button>
      </div>
      <!-- <div class="input-group mb-3 mt-3">
        <input type="text" class="form-control" placeholder="검색할 제품명을 입력하세요.">
        <div class="input-group-append">
          <button class="btn btn-secondary ml-0" type="button" id="button-addon2">검색</button>
        </div>
      </div> -->
    </div>
  </div>
  <!-- 제품별 리스트 - 검색 조건 걸어줘야함 혹은 전체 보기로 기존의 것들을 출력할 수 있어야함 -->
  <div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col">카테고리</th>
          <th scope="col">제품명</th>
          <th scope="col">가격</th>
          <th scope="col">수정날짜</th>
          <th scope="col">상태</th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <th scope="row"></th>
          <td>{{ item.category.name }}</td>
          <td>{{ item.name }}</td>
          <td>{{ addComma(item.price) }}원</td>
          <td>{{ item.update_date.slice(0,10) }}</td>
          <td v-if="item.is_active">
            <span class="badge badge-success" @click="changeActive(item)">활성화</span>
          </td>
          <td v-else>
            <span class="badge badge-danger" @click="changeActive(item)">비활성화</span>
          </td>
          <td><button type="button" class="btn btn-warning btn-sm" @click="onUpdate(category.id, item.id)">수정</button></td>
        </tr>
      </tbody>
    </table>
    <div class="page-navi">
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
import { mapMutations, mapActions, mapState, mapGetters } from 'vuex'

export default {
  data() {
    return {
      cid: '',
      perPage: 10,
      nowPage: 0,
    }
  },
  computed: {
    ...mapState('category', ['items']),
    ...mapGetters('category', ['category']),
    rows() {
      return this.items.length
    },
    pages() {
      return Math.ceil(this.items.length/this.perPage)
    },
    itemsForList() {
      return this.items.slice(
        (this.nowPage) * this.perPage,
        (this.nowPage + 1) * this.perPage
      )
    },
  },
  methods: {
    ...mapActions('category', ['getItem', 'delItem', 'postItem']),
    ...mapMutations('category', ['SET_CATEGORY']),

    onCreate(name) {
      this.$router.push({name:name}, () => {})
    },

    onUpdate(cid, pid) {
      // console.log(cid)
      // console.log(pid)
      this.$router.push({name:'ProducItemUpdate', params:{cid: cid, pid: pid, update: 'update'}})
    },
    
    changeActive(item){
      if (confirm("상태를 변경하시겠습니까?") == true){    //확인
        if (item.is_active) {
          this.delItem({ cid: this.category.id, pid: item.id, })
        }
        else {
          this.postItem({ cid: this.category.id, pid: item.id, })
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
    },
    addComma(num) {
      const regexp = /\B(?=(\d{3})+(?!\d))/g;
      return num.toString().replace(regexp, ',');
    }
  },
  watch :{
    '$route' : function() {
      const cid = this.$route.params.cid
      this.getItem(cid)
      this.SET_CATEGORY(cid)
    }
  },

  created() {
    const cid = this.$route.params.cid
    this.getItem(cid)
    this.SET_CATEGORY(cid)
  },
}
</script>

<style>
.input-group {
  float: right;
  width: 40%;
}

.btn {
  margin-left: 10px
}

span {
  cursor: pointer;
  margin-top: 4px;
}

.page-navi {
  position: absolute;
  bottom: 0;
  margin-bottom: 10px;
  left: 50%;
}

.page-item {
  cursor: pointer;
}
</style>