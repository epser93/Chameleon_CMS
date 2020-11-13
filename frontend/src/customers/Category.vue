<template>
  <div v-if="itemList">
      <SpecTemplate :datas="itemList.items" v-if="itemList.template == 1"></SpecTemplate>
      <DesignTemplate :datas="itemList.items" v-else-if="itemList.template == 2"></DesignTemplate>
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
  }
}
</script>


<style>

</style>