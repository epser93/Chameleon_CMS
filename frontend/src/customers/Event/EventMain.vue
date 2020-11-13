<template>
  <div class="container">

    <h3 class="mt-4">EVENT</h3>
    <hr>

    <div v-if="events">
      <div v-for="(event, index) in events" :key="index">
        <div class="events row mt-4 mb-4">
          <div class="event-img-box col-sm-12 col-md-8">
            <img :src="'http://k3c205.p.ssafy.io'+event.thumbnail_image.slice(56)" class="event-img" alt=""  @click="onDetail(event.id)">
          </div>
          <div class="event-text-box col-sm-12 col-md-4">
            <h4 class="event-name"  @click="onDetail(event.id)">{{ event.title }}</h4>
            <div class="event-spec m-0">
              <!-- <p>{{ event }}</p> -->
            </div>
            <p class="date">기간: {{ event.start_date.slice(0,10) }} ~ {{ event.end_date.slice(0,10) }}</p>
          </div>
        </div>
        <hr>
      </div>
    </div>
    
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'EventMain',
  computed: {
    ...mapState('customer', ['events']),
  },
  methods: {
    ...mapActions('customer', ['getEvents']),
    onDetail(eid) {
      this.$router.push({name:'CustomerEventDetail', params:{eid: eid}})
		},
  },
  created() {
    this.getEvents()
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

.event-img {
  height: 20vh;
  width: auto;
}

@media screen and (max-width: 960px) {
  .thumbnail-img {
   width: 100%;
   height: auto;
  }
  .event-name {
   font-size: 1rem; 
   margin-bottom: 10px;
  }
  .event-spec {
    font-size: 0.8rem;
  }
  .date {
    font-size: 0.8rem;
  }
}

@media screen and (max-width: 768px) {  
  .events {
    display: flex;
    flex-direction: column;
    align-self: center;
  }

  .event-spec {
    font-size: 0.5rem;
  }
  .event-name {
    margin-top: 10px;
    margin-bottom: 5px;
  }
  .date {
    position: relative;
    font-size: 0.5rem;
  }
}

.events {
  cursor: pointer;
}

.events:hover {
  background-color: #e9e9e9;
}
</style>