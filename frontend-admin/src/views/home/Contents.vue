<template>
  <div class="row">
    <div class="col-3">
        <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            <a class="nav-link active" id="v-pills-about-tab" data-toggle="pill" href="#v-pills-about" role="tab" aria-controls="v-pills-about" aria-selected="true">About</a>
            <a class="nav-link" id="v-pills-main-tab" data-toggle="pill" href="#v-pills-main" role="tab" aria-controls="v-pills-main" aria-selected="false">Main</a>
            <a class="nav-link" id="v-pills-product-tab" data-toggle="pill" href="#v-pills-product" role="tab" aria-controls="v-pills-product" aria-selected="true">Product</a>
            <a class="nav-link" id="v-pills-event-tab" data-toggle="pill" href="#v-pills-event" role="tab" aria-controls="v-pills-event" aria-selected="false">Event</a>
            <a class="nav-link" id="v-pills-contact-tab" data-toggle="pill" href="#v-pills-contact" role="tab" aria-controls="v-pills-contact" aria-selected="true">Contact</a>
            <a class="nav-link" id="v-pills-notice-tab" data-toggle="pill" href="#v-pills-notice" role="tab" aria-controls="v-pills-notice" aria-selected="false">Notice</a>
        </div>
    </div>
    <div class="col-9">
        <div class="tab-content" id="v-pills-tabContent">
            <div class="tab-pane fade show active" id="v-pills-about" role="tabpanel" aria-labelledby="v-pills-about-tab">
                <h1>여기는 about 관리</h1>
            </div>
            <div class="tab-pane fade" id="v-pills-main" role="tabpanel" aria-labelledby="v-pills-main-tab">
                <h1>여기는 main</h1>
            </div>
            <div class="tab-pane fade" id="v-pills-product" role="tabpanel" aria-labelledby="v-pills-log-product">
                <h1>여기는 product 페이지</h1>
            </div>
            <div class="tab-pane fade" id="v-pills-event" role="tabpanel" aria-labelledby="v-pills-event-tab">
                <h1>여기는 event 페이지</h1>
            </div>
            <div class="tab-pane fade" id="v-pills-contact" role="tabpanel" aria-labelledby="v-pills-contact-tab">
                <h1>여기는 contact 페이지</h1>
            </div>
            <div class="tab-pane fade" id="v-pills-notice" role="tabpanel" aria-labelledby="v-pills-notice-tab">
                <h1>여기는 notice 페이지</h1>
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