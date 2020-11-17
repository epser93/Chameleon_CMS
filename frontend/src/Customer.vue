<template>
  <div>
    <customer-top-nav/>
    <div class="body">
      <router-view/>
      <Footer/>
    </div>
  </div>
</template>

<script>
//vue-analytics
import Vue from 'vue'
import router from './router'
import VueAnalytics from 'vue-analytics'
Vue.use(VueAnalytics,{
  id: 'G-SYSQQFMZND',
  router
})

import CustomerTopNav from '@/components/CustomerTopNav'
import Footer from '@/components/Footer'

export default {
  components: {
    CustomerTopNav,
    Footer,
  },
}
</script>

<style>
.body {
  margin-top: 85px;
}

</style>