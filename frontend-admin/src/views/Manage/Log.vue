<template>
  <div>
    <div class="table-container mt-0">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">No</th>
            <th scope="col">카테고리</th>
            <th scope="col">분류</th>
            <th scope="col">서버 IP</th>
            <th scope="col">생성일</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Product</td>
            <td>계정로그인</td>
            <td>192.168.000.00</td>
            <td>2020-10-29 14:20:19</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Product</td>
            <td>게시글삭제</td>
            <td>192.168.000.00</td>
            <td>2020-10-29 14:20:19</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Product</td>
            <td>계정로그인</td>
            <td>192.168.000.00</td>
            <td>2020-10-29 14:20:19</td>
          </tr>
          <tr>
            <th scope="row">4</th>
            <td>Product</td>
            <td>계정로그인</td>
            <td>192.168.000.00</td>
            <td>2020-10-29 14:20:19</td>
          </tr>
        </tbody>
      </table>
      <div class="page-navi">
        <nav aria-label="Page navigation example justify-content-center">
          <ul class="pagination">
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li class="page-item active"><a class="page-link" href="#">1</a></li>
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.table-container {
  width: 100%;
  margin-top: 10vh; 
  text-align: center;
}

.page-navi {
  position: absolute;
  bottom: 0;
  left: 50%;
}
</style>