<template>
<div class="container">
  <h1>Product</h1>
  <div class="row justify-content-between">
    <div class="col-3">
      <button type="button" class="btn btn-info" @click="onRoute('Item')">
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
          <th scope="col">기타</th>
          <th scope="col">상태</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row"><input type="checkbox"></th>
          <td>노트북</td>
          <td>LG전자 2020 그램15</td>
          <td>15ZD90N-VX50K</td>
          <td>임시저장</td>
        </tr>
        <tr>
          <th scope="row"><input type="checkbox"></th>
          <td>노트북</td>
          <td>LG전자 2020 그램15</td>
          <td>15ZD90N-VX50K</td>
          <td>임시저장</td>
        </tr>
        <tr>
          <th scope="row"><input type="checkbox"></th>
          <td>노트북</td>
          <td>LG전자 2020 그램15</td>
          <td>15ZD90N-VX50K</td>
          <td>임시저장</td>
        </tr>
        <tr>
          <th scope="row"><input type="checkbox"></th>
          <td>노트북</td>
          <td>LG전자 2020 그램15</td>
          <td>15ZD90N-VX50K</td>
          <td>임시저장</td>
        </tr>
        <tr>
          <th scope="row"><input type="checkbox"></th>
          <td>노트북</td>
          <td>LG전자 2020 그램15</td>
          <td>15ZD90N-VX50K</td>
          <td>임시저장</td>
        </tr>

      </tbody>
    </table>

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

<style>
.btn {
  margin-left: 10px
}
</style>