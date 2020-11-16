<template>
  <div v-if="itemList">
      <SpecTemplate :datas="itemList" v-if="itemList.template == 1"></SpecTemplate>
      <DesignTemplate :datas="itemList" v-else-if="itemList.template == 2"></DesignTemplate>
  </div>
</template>


<script>
import DesignTemplate from '@/customers/Category/DesignTemplate.vue'
import SpecTemplate from '@/customers/Category/SpecTemplate.vue'
import { mapState, mapActions } from 'vuex'

export default {
  components: {
      DesignTemplate,
      SpecTemplate,
  },
  computed: {
    ...mapState('customer', ['itemList'])
  },
  watch: {
    $route() {
      this.getItemList(this.$route.params.cid)
    }
  },
  methods: {
    ...mapActions('customer', ['getItemList'])
  },
  created() {
    this.getItemList(this.$route.params.cid)
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
}
</script>


<style>

</style>