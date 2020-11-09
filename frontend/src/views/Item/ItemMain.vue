<template>
<div class="container" v-if="items != null && category != null">
  <h1>{{ category.name }}</h1>
  <div class="row justify-content-between">
    <div class="col-3">
      <button type="button" class="btn btn-info" @click="onRoute('ProductItemCreate')">
        추가
      </button>
      <button type="button" class="btn btn-danger">
        삭제
      </button>
    </div>
    <div class="col-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="제품 검색">
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" id="button-addon2">검색</button>
        </div>
      </div>
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
          <th scope="col">수정날짜</th>
          <th scope="col">상태</th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <th scope="row"><input type="checkbox"></th>
          <td>{{ item.category.name }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.update_date.slice(0,10) }}</td>
          <td v-if="item.is_active">
            <span class="badge badge-success" @click="changeActive(item)">활성화</span>
          </td>
          <td v-else>
            <span class="badge badge-danger" @click="changeActive(item)">비활성화</span>
          </td>
          <td><button type="button" class="btn btn-secondary">수정</button></td>
           <!-- @click="onUpdate(item.id)" -->
        </tr>

      </tbody>
    </table>

  </div>
</div>
</template>

<script>
import { mapMutations, mapActions, mapState, mapGetters } from 'vuex'

export default {
  data() {
    return {
      cid: ''
    }
  },
  computed: {
    ...mapState('category', ['items']),
    ...mapGetters('category', ['category'])
  },
  methods: {
    ...mapActions('category', ['getItem', 'delItem', 'postItem']),
    ...mapMutations('category', ['SET_CATEGORY']),

    onRoute(name) {
			this.$router.push({name:name}, () => {})
    },

    onUpdate(pid) {
      this.$router.push({name:'ProductItemMain', params:{pid: pid}})
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
.btn {
  margin-left: 10px
}

span {
  cursor: pointer;
  margin-top: 4px;
}
</style>