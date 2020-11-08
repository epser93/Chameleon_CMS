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
              <input ref="thumbnailImage" type="file" hidden @change="onChangeThumbnail">
              <button type="button" class="btn btn-success btn-sm" @click="onUploadThumbnail">업로드</button>
          <div class="preview-img">
            <img id="inner-img" v-if="imageUrl.thumbnail" :src="imageUrl.thumbnail" alt="">
          </div>
          <h4>이벤트 썸네일</h4>
              <input ref="thumbnailImage2" type="file" hidden @change="onChangeThumbnail2">
              <button type="button" class="btn btn-success btn-sm" @click="onUploadThumbnail2">업로드</button>
          <div class="preview-img">
            <img id="inner-img" v-if="imageUrl.thumbnail2" :src="imageUrl.thumbnail2" alt="">
          </div>
        </div>

        <div class="row justify-content-end" id="content-btn">
          <div >
            <button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows">미리보기</button>
          </div>
          <div >
            <button type="button" class="btn btn-secondary btn-sm" @click="onRegister">임시저장</button>
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
  components: {
    Datepicker,
  },
  data() {
    return {
      title: '',
      content: '',
      date: {
        start: '',
        end: ''
      },
      imageUrl: {
        thumbnail: '',
        thumbnail2: '',
        detail: [],
      },
      images: {
        thumbnail: '',
        thumbnail2: '',
        detail: [],
      },
      linkUrl: ''
    }
  },
  computed: {
    ...mapState('event', ['event']),
  },
  watch: {
    event(val) {
      this.imageUrl.thumbnail = val.thumbnail_image
      this.title = val.title,
      this.content = val.content,
      this.date.start = val.start_date,
      this.date.end = val.end_date
      // this.eventData.images = []
    }
  },
  methods: {
    ...mapActions('event', ['getEvent', 'postEvent']),
    ...mapMutations('event', ['SET_EVENT']),
    onClickRegister(){
      console.log('dfdfdf')
    },
    onClickWindows(){
      var url="test.html";
      window.open(url,"",)
    },
    onUploadThumbnail() {
      this.$refs.thumbnailImage.click()
    },
    onChangeThumbnail(e) {
      const file = e.target.files[0]
      this.images.thumbnail = file
      this.imageUrl.thumbnail = URL.createObjectURL(file)
    },
    onUploadThumbnail2() {
      this.$refs.thumbnailImage2.click()
    },
    onChangeThumbnail2(e) {
      const file = e.target.files[0]
      this.images.thumbnail2 = file
      this.imageUrl.thumbnail2 = URL.createObjectURL(file)
    },
    onRegister() {
      const imgArray = new Array()
      imgArray.push(this.images.thumbnail)
      imgArray.push(this.images.thumbnail2)
      console.log(imgArray)
      // imgArray.from(input_file.files).forEach((f) => {
      //   data.append('image[]', f)
      // })
      const eventData = new FormData()
      eventData.append('thumbnail', this.images.thumbnail)
      eventData.append('title', this.title)
      eventData.append('content', this.content)
      eventData.append('start_date', this.date.start.slice(0,10) + " 00:00:00")
      eventData.append('end_date', this.date.end.slice(0,10)+" 23:59:59")
      // json으로 해보기
      eventData.append('images', imgArray[0])
      eventData.append('images', imgArray[1])
      eventData.append('url', 'test')
      this.postEvent(eventData)
    }
  },
  created() {
    if (this.$route.params.method == 'update') {
      this.getEvent(this.$route.params.eid)
    }
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