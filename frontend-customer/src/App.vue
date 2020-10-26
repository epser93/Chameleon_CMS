<template>
  <div>
    <top-nav/>
    <router-view/>
    <Footer/>
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
</style>