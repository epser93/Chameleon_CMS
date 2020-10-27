<template>
  <div>
    <top-nav/>
    <router-view/>
  </div>
</template>

<script>
import TopNav from '@/components/TopNav'
export default {
  name: 'Home',
  components: {
    TopNav,
  }
}
</script>
