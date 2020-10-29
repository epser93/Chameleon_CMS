<template>
  <div class="row">
    <div class="col-3">
        <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            <a class="nav-link active" id="v-pills-main-tab" data-toggle="pill" href="#v-pills-main" role="tab" aria-controls="v-pills-main" aria-selected="false">Main</a>
            <a class="nav-link" id="v-pills-product-tab" data-toggle="pill" href="#v-pills-product" role="tab" aria-controls="v-pills-product" aria-selected="true">Product</a>
            <a class="nav-link" id="v-pills-event-tab" data-toggle="pill" href="#v-pills-event" role="tab" aria-controls="v-pills-event" aria-selected="false">Event</a>
            <a class="nav-link" id="v-pills-notice-tab" data-toggle="pill" href="#v-pills-notice" role="tab" aria-controls="v-pills-notice" aria-selected="false">Notice</a>
        </div>
    </div>
    <div class="col-9">
        <div class="tab-content" id="v-pills-tabContent">
            <div class="tab-pane fade show active" id="v-pills-main" role="tabpanel" aria-labelledby="v-pills-main-tab">
                <Main/>
            </div>
            <div class="tab-pane fade" id="v-pills-product" role="tabpanel" aria-labelledby="v-pills-log-product">
                <Product/>
            </div>
            <div class="tab-pane fade" id="v-pills-event" role="tabpanel" aria-labelledby="v-pills-event-tab">
                <Event/>
            </div>
            <div class="tab-pane fade" id="v-pills-notice" role="tabpanel" aria-labelledby="v-pills-notice-tab">
                <Notice/>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import Event from '../homeContent/Event.vue'
import Main from '../homeContent/Main.vue'
import Notice from '../homeContent/Notice.vue'
import Product from '../homeContent/Product.vue'

export default {
    components: {
        Event,
        Main,
        Notice,
        Product
  }
}
</script>

<style>

</style>