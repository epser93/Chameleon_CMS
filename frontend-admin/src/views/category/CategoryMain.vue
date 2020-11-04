<template>
<div class="container">
  <!-- 제품별 리스트 - 검색 조건 걸어줘야함 혹은 전체 보기로 기존의 것들을 출력할 수 있어야함 -->
  <div class="category-list">
    <table class="table">
      <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col">카테고리</th>
          <th scope="col">상태</th>
          <th scope="col">상세보기</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row"><input type="checkbox"></th>
          <td>노트북</td>
          <td>임시저장</td>
          <td><button type="button" class="btn btn-info" @click="onRoute('Item')">더 보기</button></td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="row justify-content-end">
    <div class="col-4">
        <button type="button" class="btn btn-info" @click="onRoute('Category')">
          추가
        </button>
        <button type="button" class="btn btn-danger">
          삭제
        </button>
    </div>
  </div>


</div>
</template>

<script>
export default {
  methods: {
    onRoute(name) {
			this.$router.push({name:name}, () => {})
		},
  }
}
</script>

<style scoped>
.btn {
  margin-left: 10px
}

.category-list {
  margin-top: 90px;
}
</style>