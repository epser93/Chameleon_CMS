<template>
  <div class="container">
    <div class="event row">
      <div class="col-8">
        <div class="event-content">
          <h4>이벤트 제목</h4>
          <input v-model="title" type="text">
        </div>
        
        <div class="event-content">
          <h4>이벤트 기간</h4>
          <table class="template-table">
            <tr>
              <td>
                <h2>시작 날짜</h2>
              </td>
              <td>
                <h2>종료 날짜</h2>
              </td>
            </tr>
            <tr>
              <td>
                <datepicker v-model="date.start" :value="date.start" />
              </td>
              <td>          
                <datepicker v-model="date.end" :value="date.end" />
              </td>
            </tr>
          </table>
        </div>

        <div class="event-content">
          <h4>이벤트 내용</h4>
          <textarea class="form-control" rows="5" cols="40" v-model="content"></textarea>
        </div>

        <div class="event-content">
          <h4>이벤트 썸네일</h4>
              <input ref="thumbImageInput" type="file" hidden @change="onChangeThumbImages">
              <button type="button" class="btn btn-success btn-sm" @click="onClickImageUpload">업로드</button>
          <div class="preview-img">
            <img id="inner-img" v-if="imageUrl.thumbnail" :src="imageUrl.thumbnail">
          </div>
        </div>

        <div class="row justify-content-end" id="content-btn">
          <div >
            <button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows">미리보기</button>
          </div>
          <div >
            <button type="button" class="btn btn-secondary btn-sm">임시저장</button>
          </div>
        </div>  

      </div>
    </div>
  </div>
</template>

<script>
import Datepicker from "vuejs-datepicker";

import { mapState, mapMutations, mapActions } from 'vuex'

export default {
  data() {
    return {
      title: '',
      content: '',
      date: {
        start: '',
        end: ''
      },
      history: [],
      imageUrl: {
        thumbnail :'',
        detail: '',
      },
      eventData : {
        title: '',
        start_date: '',
        end_date: '',
        thumbnail_image: '',
        detail: []
      }
    }
  },
  computed: {
    ...mapState('event', ['event'])
  },
  components: {
    Datepicker,
  },
  methods: {
    ...mapActions('event', ['getEvent']),
    ...mapMutations('event', ['SET_EVENT']),
    onClickRegister(){
      console.log('dfdfdf')
    },
    onClickWindows(){
      var url="test.html";
      window.open(url,"",);
    },

    onClickImageUpload() {
        this.$refs.imageInput.click();
    },
    onChangeThumbImages(e) {
        console.log(e.target.files)
        const file = e.target.files[0];
        this.imageUrl.thumbnail = URL.createObjectURL(file);
    },
  },
  created() {
    if (this.$route.params.method == 'update') {
      console.log(this.$store.state.event.event)
    }
  },
  destroyed() {
    this.SET_EVENT('')
  }
}
</script>

<style>
textarea {
  resize: none;
}

.form-control {
  width: auto;
}

.template-table {
  text-align: center;
  width: 250px;
}

.event-content {
  margin-top: 30px;
}

.preview-img {
  width: 350px;
  height: 150px;
  background-color: ghostwhite;
}

#inner-img {
  width : 300px;
  height: 125px;
  margin-left: auto;
  margin-right: auto;
}
</style>