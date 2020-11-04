<template>
  <div class="modal fade" tabindex="-1" id="unauthorizedUser">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">가입승인</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">부서</th>
                <th scope="col">이름</th>
                <th scope="col">아이디</th>
                <th scope="col">승인여부</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>인사</td>
                <td>송은석</td>
                <td>songsong123</td>
                <td>
                  <button type="button" class="btn btn-outline-primary approve-btn">승인</button>
                  <button type="button" class="btn btn-outline-danger">거부</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">닫기</button>
          <button type="button" class="btn btn-primary">완료</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.approve-btn {
  margin-right: 1vw;
}
</style>