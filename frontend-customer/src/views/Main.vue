<template>
  <div>
    <top-nav/>
    <div class="body">
      <router-view/>
      <Footer/>
    </div>
  </div>
</template>

<script>
import TopNav from '@/components/TopNav'
import Footer from '@/components/Footer'

export default {
  components: {
    TopNav,
    Footer,
  },
}
</script>

<style>
.body {
  margin-top: 68px;
}

</style>