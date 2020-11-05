<template>
  <div>
    <div class="table-container">
      <div class="btn">
        <button type="button" class="btn btn-outline-danger">삭제</button>
        <button type="button" class="btn btn-outline-success" @click="onRoute('EventForm')">생성</button>
      </div>
      <table class="table">
        <thead>
          <tr>
            <th scope="col"><input type="checkbox" @click="checkAll(events)"></th>
            <th scope="col">카테고리</th>
            <th scope="col">제목</th>
            <th scope="col">기간</th>
            <th scope="col">기타</th>
            <th scope="col">상태</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(event, index) in events" :key="index">
            <th scope="row"><input type="checkbox" v-model="checked" :value="event"></th>
            <td>{{ event.category }}</td>
            <td>{{ event.title }}</td>
            <td>{{ event.startDate }} ~ {{ event.endDate }}</td>
            <td>{{ event.etc }}</td>
            <td>게시중</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      checked: [],
      events: [
        { 
          category : "Laptop",
          title : "가을맞이 노트북 장만!",
          startDate : "2020-10-01",
          endDate : "2020-11-31",
          etc : ""
        },
        {
          category : "Product",
          title : "크리스마스 특집 가전",
          startDate : "2020-11-07",
          endDate : "2020-11-30",
          etc : ""
        },
        {
          category : "Air Conditioner",
          title : "더위를 날려 버리자",
          startDate : "2020-08-01",
          endDate : "2020-08-31",
          etc : ""
        }
      ]
    }
  },
  methods: {
    onRoute(name) {
			this.$router.push({name:name}, () => {})
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
  computed: {

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