<template>
  <div class="container">
    <div class="event row">
      <div class="col-8">
        <!-- 이벤트 제목 -->
        <div class="event-content">
          <h4>이벤트 제목</h4>
          <input v-model="title" type="text" placeholder=" 제목을 입력해 주세요.">
        </div>
        <!-- 이벤트 기간 -->
        <div class="event-content">
          <h4>이벤트 기간</h4>
          <table class="template-table">
            <tr>
              <td>
                <p class="mb-0">시작 날짜</p>
              </td>
              <td>
                <p class="mb-0">종료 날짜</p>
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
        <!-- 이벤트 내용 -->
        <div class="event-content">
          <h4>이벤트 내용</h4>
          <textarea class="form-control" rows="5" cols="40" v-model="content"></textarea>
        </div>
        <!-- 이벤트 썸네일 -->
        <div class="event-content">
          <div class="row">
            <h4 class="ml-3">이벤트 썸네일</h4>
            <input ref="thumbnailImage" type="file" hidden @change="onChangeThumbnail">
            <button type="button" class="btn btn-success btn-sm ml-3" @click="onUploadThumbnail">업로드</button>
          </div>
          <div class="preview-img mt-2">
            <img id="inner-img" class="d-flex mx-auto" v-if="imageUrl.thumbnail" :src="imageUrl.thumbnail" alt="">
          </div>
        </div>
        <div class="event-content">
          <div class="row">
            <h4 class="ml-3">이벤트 썸네일</h4>
            <input ref="thumbnailImage" type="file" hidden @change="onChangeThumbnail">
            <button type="button" class="btn btn-success btn-sm ml-3" @click="onUploadThumbnail">업로드</button>
          </div>
          <div class="preview-img mt-2">
            <img id="inner-img" class="d-flex mx-auto" v-if="imageUrl.thumbnail" :src="imageUrl.thumbnail" alt="">
          </div>
        </div>
        <!-- 뒤로가기, 미리보기, 임시저장 -->
        <div class="row justify-content-end mt-5 mb-5" id="content-btn">
          <div>
            <button type="button" class="btn btn-dark btn-sm mr-2" @click="onRoute('Event')">뒤로가기</button>
          </div>
          <div>
            <button type="button" class="btn btn-secondary btn-sm mr-2" @click="onClickWindows">미리보기</button>
          </div>
          <div>
            <button type="button" class="btn btn-primary btn-sm" @click="onRegister">임시저장</button>
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
    },
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },

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

input {
  border: 1px solid grey;
  border-radius: 10px;
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
  width: 360px;
  height: 150px;
  background-color: ghostwhite;
  border: 1px solid #ced4da;
  border-radius: 10px;
}

#inner-img {
  width : 300px;
  height: 125px;
  right: 50%;
  top: 50%;
}

</style>