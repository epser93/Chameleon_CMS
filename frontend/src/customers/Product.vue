<template>
  <div>
    <CarouselTemplate :itemInfo="itemInfo" v-if="itemInfo.template === 3" />
    <MovingImageTemplate :itemInfo="itemInfo" v-else-if="itemInfo.template === 4" />
  </div>
</template>

<script>
import CarouselTemplate from '@/customers/ProductDetail/CarouselTemplate'
import MovingImageTemplate from '@/customers/ProductDetail/MovingImageTemplate'
import { mapActions, mapState } from 'vuex'
export default {
  name: 'Product',
  components: {
    CarouselTemplate,
    MovingImageTemplate
  },
  computed: {
    ...mapState('customer', ['itemInfo'])
  },
  methods: {
    ...mapActions('customer', ['getItemInfo']),
  },
  watch: {
    '$route' : function() {
      this.getItemInfo(this.$route.params.cid)
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
  },
  created() {
    this.getItemInfo(this.$route.params.cid)
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
}
</script>