<template>
  <div>
    <datepicker v-model="date.start" :value="date.start" />
    <datepicker v-model="date.end" :value="date.end" />
  </div>
</template>

<script>
import Datepicker from "vuejs-datepicker";

export default {
  data() {
    return {
      date: {
        start: '',
        end: ''
      }
    }
  },
  components: {
    Datepicker,
  },
};
</script>

<style>
</style>