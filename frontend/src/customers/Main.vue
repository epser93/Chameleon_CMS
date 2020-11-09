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
  margin-top: 68px;
}

</style>