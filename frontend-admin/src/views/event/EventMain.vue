<template>
  <div v-if="events">
    <div class="table-container">
      <div class="btn">
        <button type="button" class="btn btn-outline-danger">삭제</button>
        <button type="button" class="btn btn-outline-success" @click="onCreate()">생성</button>
      </div>
      <table class="table">
        <thead>
          <tr>
            <th scope="col"><input type="checkbox" @click="checkAll(events)"></th>
            <th scope="col">제목</th>
            <th scope="col">기간</th>
            <th scope="col">상세보기</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(event, index) in events" :key="index">
            <th scope="row"><input type="checkbox" v-model="checked" :value="event"></th>
            <td>{{ event.title }}</td>
            <td>{{ eventDate[index].start }} ~ {{ eventDate[index].end }}</td>
            <td><button type="button" class="btn btn-info btn-sm" @click="onUpdate(event.id)">보기</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState('event',['events']),
    eventDate() {
      const dateList = new Array()
      for (let i=0; i<this.events.length; i++) {
        const SD = new Date(this.events[i].start_date)
        const ED = new Date(this.events[i].end_date)
        var arrDayStr = ['일','월','화','수','목','금','토']
        const date = { 
          start: SD.toLocaleDateString() + ' (' + arrDayStr[SD.getDay()] + ')', 
          end: ED.toLocaleDateString() + ' (' + arrDayStr[ED.getDay()] + ')'
        }
        dateList.push(date)
      }
      return dateList
    }
  },
  data() {
    return {
      checked: [],
    }
  },
  methods: {
    ...mapActions('event',['getEvents']),
    onCreate() {
			this.$router.push({name: 'EventCreate', params: {method: 'create'}}, () => {})
    },
    onUpdate(eid) {
			this.$router.push({name: 'EventUpdate', params: {method: 'update', eid: eid}}, () => {})
		},
    checkAll(events) {
      if (this.checked.length !== this.events.length){
        for (let i=0; i<this.events.length; i++) {
          this.checked.push(events[i])
        }
      } else {
        this.checked = []
      }
    }
  },
  created() {
    this.getEvents()
  }
}
</script>

<style scoped>
.table-container {
  width: 90%;
  margin-top: 10vh; 
  text-align: center;
}

.btn {
  margin-bottom: 30px;
  display: inline;
}

</style>