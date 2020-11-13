<template>
  <div class="container">
    <div class="event">
      <div class="col-8">
        <div class="form-title mt-5">
          <h3 v-if="update">Edit Event</h3>
          <h3 v-else>Add Event</h3>
          <hr>
        </div>
        <!-- 이벤트 제목 -->
        <div class="event-content">
          <h4>이벤트 제목</h4>
          <input v-model="title" class="form-control" type="text" placeholder=" 제목을 입력해 주세요.">
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
          <h4>관련 URL</h4>
          <input type="text" class="form-control" placeholder="상품 페이지" v-model="linkUrl">
        </div>

        <div class="event-content">
          <div class="row">
            <h4 class="ml-3">이벤트 썸네일</h4>
            <input ref="thumbnailImage" type="file" hidden @change="onChangeThumbnail">
            <button type="button" class="btn btn-success btn-sm ml-3" @click="onUploadThumbnail">이미지 등록</button>
          </div>
          <div class="preview-img mt-2">
            <img id="inner-img" class="d-flex mx-auto" v-if="imageUrl.thumbnail" :src="imageUrl.thumbnail" alt="">
          </div>
        </div>

        <div class="content-part">
          <div class="row align-items-center">
            <h4 class="mb-0 ml-3">상세 이미지</h4>
          </div>
          <div v-if="!images.detail.length" class="file-upload-container">
            <div class="file-upload-example">
              <div class="notice-item">
                <div class="image-box">
                  <label for="file" class="mt-2">이미지 등록</label>
                  <input type="file" id="file" ref="detailImages" @change="imageUpload" multiple />
                </div>
              </div>
            </div>
          </div>
          <div v-else class="file-preview-content-container">
            <div class="file-preview-container">
              <div v-for="(file, index) in images.detail" :key="index" class="file-preview-wrapper">
                <div class="file-close-button" @click="fileDeleteButton">
                  <img src="@/assets/icons/x.svg" alt="delete button" width="20" height="20" title="x" :name="file.number">
                </div>
                <img :src="file.preview" />
              </div>
              <div class="file-preview-wrapper-upload">
                <div class="image-box" id="image-box-preview">
                  <label for="file">추가 사진 등록</label>
                  <input type="file" id="file" ref="detailImages" @change="imageAddUpload" multiple />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 뒤로가기, 미리보기, 임시저장 -->
        <div class="row justify-content-end mt-5 mb-5" id="content-btn">
          <div>
            <button type="button" class="btn btn-dark btn-sm mr-2" @click="$router.go(-1)">뒤로가기</button>
          </div>
          <div>
            <button type="button" class="btn btn-secondary btn-sm mr-2" @click="onClickWindows">미리보기</button>
          </div>
          <div>
            <button type="button" class="btn btn-primary btn-sm" @click="onRegister">등록하기</button>
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
      },
      images: {
        thumbnail: '',
        detail: [],
      },
      linkUrl: '',
      uploadImageIndex: 0,
      update: false
    }
  },
  computed: {
    ...mapState('event', ['event']),
  },
  watch: {
    event(val) {
      this.imageUrl.thumbnail = 'http://k3c205.p.ssafy.io' + val.thumbnail_image.slice(56)
      this.title = val.title,
      this.content = val.content,
      this.date.start = val.start_date,
      this.date.end = val.end_date
      this.linkUrl = val.url
      for (let i = 0; i < val.images.length; i++) {
        const imageData = {
          file: val.images[i].id,
          number: i,
          preview: 'http://k3c205.p.ssafy.io' + val.images[i].image.slice(56)
        }
        this.images.detail.push(imageData)
      }
      this.uploadImageIndex = val.images.length
      console.log(val.detail)
      console.log(this.images.detail)

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
    imageUpload() {
      const num = this.$refs.detailImages.files.length
      for (let i = 0; i < this.$refs.detailImages.files.length; i++) {
        const image = {
          //실제 파일
          file: this.$refs.detailImages.files[i],
          //이미지 프리뷰
          preview: URL.createObjectURL(this.$refs.detailImages.files[i]),
          //삭제및 관리를 위한 number
          number: i
        }
        this.images.detail.push(image)
      }
      this.uploadImageIndex = num; //이미지 index의 마지막 값 + 1 저장
      },

    imageAddUpload() {
      const num = this.$refs.detailImages.files.length
      for (let i = 0; i < num; i++) {
        const image = {
          //실제 파일
          file: this.$refs.detailImages.files[i],
          //이미지 프리뷰
          preview: URL.createObjectURL(this.$refs.detailImages.files[i]),
          //삭제및 관리를 위한 number
          number: this.uploadImageIndex + i
        }
        this.images.detail.push(image)
      }
      this.uploadImageIndex = this.uploadImageIndex + num;
    },
    fileDeleteButton(e) {
      const name = e.target.getAttribute('name');
      console.log(name)
      this.images.detail = this.images.detail.filter(data => data.number !== Number(name));
    },
    onRegister() {
      const imgArray = [...this.images.detail]
      const eventData = new FormData()
      eventData.append('thumbnail', this.images.thumbnail)
      eventData.append('title', this.title)
      eventData.append('content', this.content)
      const SD = new Date(this.date.start)
      const startDate = SD.getFullYear() + "-" + (SD.getMonth() + 1) + "-" + SD.getDate()
      const ED = new Date(this.date.end)
      const endDate = ED.getFullYear() + "-" + (ED.getMonth() + 1) + "-" + ED.getDate()
      eventData.append('start_date', startDate.slice(0,10) + " 00:00:00")
      eventData.append('end_date', endDate.slice(0,10)+" 23:59:59")
      eventData.append('number', imgArray.length)
      for (let i = 0; i < imgArray.length; i++) {
        eventData.append('image'+i, imgArray[i].file)
      }
      eventData.append('url', 'test')
      this.postEvent(eventData)
    },

  },
  created() {
    if (this.$route.params.method == 'update') {
      this.getEvent(this.$route.params.eid)
      this.update = true
    }
  }
}
</script>

<style>
textarea {
  resize: none;
}

input {
  border: 1px solid #cbcbcb;
  border-radius: 5px;
}

.form-control {
  width: auto;
}

.form-title {
  display: inline-block;
}

hr {
  border: 3px solid grey;
  border-radius: 3px;
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

.image-box label {
    display: inline-block;
    padding: 10px 20px;
    background-color: #28A743;
    color: #fff;
    vertical-align: middle;
    font-size: 15px;
    cursor: pointer;
    border-radius: 5px;
}

.file-preview-wrapper {
    padding: 10px;
    position: relative;
}

.file-preview-wrapper>img {
    position: relative;
    width: 190px;
    height: 130px;
    z-index: 10;
}

.file-close-button {
    position: absolute;
    /* align-items: center; */
    line-height: 18px;
    z-index: 99;
    font-size: 18px;
    right: 5px;
    top: 10px;
    color: #fff;
    font-weight: bold;
    background-color: #cbcbcb;
    width: 20px;
    height: 20px;
    text-align: center;
    cursor: pointer;
}

.file-preview-container {
    height: 100%;
    display: flex;
    flex-wrap: wrap;
}

.file-preview-wrapper-upload {
    margin: 10px;
    padding-top: 20px;
    /* background-color: #888888; */
    width: 190px;
    height: 130px;
}
.content-part{
  margin-top: 30px;
}

.file-upload-example {
    height: 100%;
}

.file-preview-content-container {
    height: 100%;
}
#image-box-preview{
    margin-top: 30px;
    padding-bottom: 20px;
    text-align: center;
}
.notice-item {
  margin-top: 5px;
  color: grey;
}

.image-box {
    padding-bottom: 10px;
}

.image-box input[type='file'] {
    position: absolute;
    width: 0;
    height: 0;
    padding: 0;
    overflow: hidden;
    border: 0;
}

.warning-text {
  align-items: center;
  color: grey;
}

.warning-text-detail {
  margin-bottom: 0;
  font-size: 12px;
}
</style>