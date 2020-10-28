<template>
  <div class="container">

    <h3 class="mt-4">EVENT</h3>
    <hr>

    <div class="row mt-4 mb-4 ml-4" @click="onDetail('B')">
      <div class="col-8">
        <img src="https://picsum.photos/600/250" class="event-img" alt="">
      </div>
      <div class="col-4">
        <h4 class="event-name">이벤트 B</h4>
        <div class="event-spec m-0">
          <p>이벤트 설명</p>
        </div>
        <p class="date">기간: 2020-00-00 ~ 2020-00-00</p>
      </div>
    </div>
    <hr>
    <div class="row mt-4 mb-4 ml-4" @click="onDetail('A')">
      <div class="col-8">
        <img src="https://picsum.photos/600/250" class="event-img" alt="">
      </div>
      <div class="col-4">
        <h4 class="event-name">이벤트 A</h4>
        <div class="event-spec m-0">
          <p>이벤트 설명</p>
        </div>
        <p class="date">기간: 2020-00-00 ~ 2020-00-00</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EventMain',
  methods: {
    onDetail(eid) {
      this.$router.push({name:'EventDetail', params:{eid: eid}})
		},
  }
}
</script>

<style>
p {
  margin: 0;
}

.date {
  position: absolute;
  bottom: 0px;
}

@media screen and (max-width: 960px) {
  .event-img {
   width: 80%;
   height: auto;
  }
  .event-name {
   font-size: 1rem; 
   margin-bottom: 10px;
  }
  .event-spec {
    font-size: 1rem;
  }
  .date {
    position: relative;
    font-size: 1rem;
  }
}

@media screen and (max-width: 576px) {
  .event-spec {
    font-size: 0.5rem;
  }
  .event-name {
    margin-bottom: 5px;
  }
  .date {
    position: relative;
    font-size: 0.5rem;
  }
}
</style>