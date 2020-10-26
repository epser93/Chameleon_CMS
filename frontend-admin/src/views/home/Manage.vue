<template>
  <div class="row">
    <div class="col-3">
        <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            <a class="nav-link active" id="v-pills-user-tab" data-toggle="pill" href="#v-pills-user" role="tab" aria-controls="v-pills-user" aria-selected="true">User</a>
            <a class="nav-link" id="v-pills-log-tab" data-toggle="pill" href="#v-pills-log" role="tab" aria-controls="v-pills-log" aria-selected="false">Log</a>
        </div>
    </div>
    <div class="col-9">
        <div class="tab-content" id="v-pills-tabContent">
            <div class="tab-pane fade show active" id="v-pills-user" role="tabpanel" aria-labelledby="v-pills-user-tab">
                <h1>여기는 유저 관리</h1>
            </div>
            <div class="tab-pane fade" id="v-pills-log" role="tabpanel" aria-labelledby="v-pills-log-tab">
                <h1>여기는 log 페이지</h1>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>