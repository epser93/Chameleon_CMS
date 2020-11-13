<template>
  <div v-if="events" class="container pl-0">
    <div v-if="events" class="table-container">
      <div class="btn-background">
        <div class="event-btn row align-items-center mt-3 mb-3">
          <h5 class="mb-0 ml-3">이벤트</h5>
          <button type="button" class="btn btn-info btn-sm" @click="onCreate()">추가</button>
        </div>
      </div>
      <table class="table">
        <thead class="">
          <tr>
            <th scope="col">제목</th>
            <th scope="col">상태</th>
            <th scope="col">기간</th>
            <th scope="col">상세보기</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(event, index) in eventsForList" :key="index">
            <td>{{ event.title }}</td>
            <!-- 스위치 -->
            <td v-if="event.is_active" class="row justify-content-center">
              <span class="badge badge-success" @click="changeActive(event)">활성화</span>
            </td>
            <td v-else class="row justify-content-center">
              <span class="badge badge-danger" @click="changeActive(event)">비활성화</span>
            </td>
            <!-- 스위치 -->
            <td>{{ eventDate[index].start }} ~ {{ eventDate[index].end }}</td>
            <td><button type="button" class="btn btn-secondary btn-sm" @click="onUpdate(event.id)">보기</button></td>
          </tr>
        </tbody>
      </table>
      <div class="page-navi">
        <nav aria-label="Page navigation example">
          <ul v-if="pages == 0" class="pagination">
            <li class="page-item">
              <img src="@/assets/icons/caret-left.svg" width="26" height="26" title="caret-left" @click="prevPage()">
            </li>
            <p> {{ nowPage + 1 }}  / {{ pages + 1}} </p>
            <li class="page-item">
              <img src="@/assets/icons/caret-right.svg" width="26" height="26" title="caret-right" @click="nextPage()">
            </li>
          </ul>
          <ul v-else class="pagination">
            <li class="page-item">
              <img v-if="nowPage == 0" src="@/assets/icons/caret-left.svg" width="26" height="26" title="caret-left" @click="prevPage()">
              <img v-else src="@/assets/icons/caret-left-fill.svg" width="26" height="26" title="caret-left-fill" @click="prevPage()">
            </li>
            <p> {{ nowPage + 1 }}  / {{ pages }} </p>
            <li class="page-item">
              <img v-if="nowPage == (pages-1)" src="@/assets/icons/caret-right.svg" width="26" height="26" title="caret-right" @click="nextPage()">
              <img v-else src="@/assets/icons/caret-right-fill.svg" width="26" height="26" title="caret-right-fill" @click="nextPage()">
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
    },
    rows() {
      return this.events.length
    },
    pages() {
      return Math.ceil(this.events.length/this.perPage)
    },
    eventsForList() {
      return this.events.slice(
        (this.nowPage) * this.perPage,
        (this.nowPage + 1) * this.perPage
      )
    },
  },
  data() {
    return {
      checked: [],
      perPage: 7,
      nowPage: 0,
    }
  },
  methods: {
    ...mapActions('event', ['getEvents', 'delEvent', 'actEvent']),
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
    },
    changeActive(event){
      if (confirm("상태를 변경하시겠습니까?") == true){    //확인
          if (event.is_active) {
            this.delEvent(event.id)
          }
          else {
            this.actEvent(event.id)
          }
      } else {   //취소
        this.getEvents()
      }
    },
    prevPage() {
      if (this.nowPage > 0) {
        this.nowPage -= 1
      }
    },
    nextPage() {
      if (this.nowPage < this.pages-1) {
        this.nowPage += 1
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

.custom-control-label {
  cursor: pointer;
}

span {
  cursor: pointer;
  margin-top: 4px;
}

.page-item {
  cursor: pointer;
}
</style>