<template>
  <div class="container-fluid">
    <div class="table-container">
      <table class="table">
        <thead>
          <tr>
            <th scope="col"><input type="checkbox"></th>
            <th scope="col">부서</th>
            <th scope="col">이름</th>
            <th scope="col">아이디</th>
            <th scope="col">권한</th>
            <th scope="col">상태</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row"><input type="checkbox"></th>
            <td>생산관리</td>
            <td>송은석</td>
            <td>id1</td>
            <td>권한1</td>
            <td>승인대기</td>
          </tr>
          <tr>
            <th scope="row"><input type="checkbox"></th>
            <td>품질관리</td>
            <td>강현영</td>
            <td>id2</td>
            <td>권한2</td>
            <td>승인완료</td>
          </tr>
          <tr>
            <th scope="row"><input type="checkbox"></th>
            <td>구매</td>
            <td>김유기</td>
            <td>id3</td>
            <td>권한3</td>
            <td>승인대기</td>
          </tr>
          <tr>
            <th scope="row"><input type="checkbox"></th>
            <td>전산</td>
            <td>장주환</td>
            <td>id4</td>
            <td>권한4</td>
            <td>승인대기</td>
          </tr>
          <tr>
            <th scope="row"><input type="checkbox"></th>
            <td>마케팅</td>
            <td>임선빈</td>
            <td>id5</td>
            <td>권한5</td>
            <td>승인대기</td>
          </tr>
          <tr>
            <th scope="row"><input type="checkbox"></th>
            <td>개발</td>
            <td>윤상목</td>
            <td>id6</td>
            <td>권한6</td>
            <td>승인대기</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.table-container {
  width: 100%;
  margin-top: 10vh; 
  text-align: center;
}
</style>