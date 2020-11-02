<template>
  <div>
    <div class="table-container">
      <table class="table">
        <thead>
          <tr>
            <th scope="col"><input type="checkbox"></th>
            <th scope="col">카테고리</th>
            <th scope="col">제목</th>
            <th scope="col">기간</th>
            <th scope="col">기타</th>
            <th scope="col">상태</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(event, index) in events" :key="index">
            <th scope="row"><input type="checkbox"></th>
            <td>{{ event.category }}</td>
            <td>{{ event.title }}</td>
            <td>{{ event.startDate }} ~ {{ event.endDate }}</td>
            <td>{{ event.etc }}</td>
            <td>isPostState</td>
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
  computed: {
    // isPostState(event) {
    //   const today = 
    //   if event.
  }
}
</script>

<style scoped>
.table-container {
  width: 90%;
  margin-top: 10vh; 
  text-align: center;
}
</style>