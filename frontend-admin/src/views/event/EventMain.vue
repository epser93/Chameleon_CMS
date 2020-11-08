<template>
  <div v-if="events" class="container-fluid pl-0">
    <div v-if="events" class="table-container">
      <div class="btn-background">
        <div class="event-btn ml-3 mt-3 mb-3">
          <!-- <button type="button" class="btn btn-danger">삭제</button> -->
          <button type="button" class="btn btn-info ml-3" @click="onCreate()">생성</button>
        </div>
      </div>
      <table class="table">
        <thead class="">
          <tr>
            <th scope="col">제목</th>
            <th scope="col">기간</th>
            <th scope="col">상세보기</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(event, index) in events" :key="index">
            <td>{{ event.title }}</td>
            <td>{{ eventDate[index].start }} ~ {{ eventDate[index].end }}</td>
            <td><button type="button" class="btn btn-secondary btn-sm" @click="onUpdate(event.id)">보기</button></td>
          </tr>
        </tbody>
      </table>
      <div class="page-navi">
        <nav aria-label="Page navigation example justify-content-center">
          <ul class="pagination">
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li class="page-item active"><a class="page-link" href="#">1</a></li>
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
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
  width: 100%;
  text-align: center;
}

.event-btn {
  display: flex;
}

td {
  padding-top: 16px;
  padding-bottom: 10px;
}

.page-navi {
  position: absolute;
  bottom: 0;
  left: 50%;
}
</style>