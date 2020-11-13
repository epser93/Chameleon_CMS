<template>
  <div class="container">
    <div class="event row">
      <div class="col-8">
        <!-- 대표 이미지 제목 -->
        <div class="event-content">
          <h4>이미지 제목</h4>
          <input v-model="title" type="text" placeholder=" 제목을 입력해 주세요.">
        </div>

        <!-- 대표 이미지 썸네일 -->
        <div class="event-content">
          <h4>관련 URL</h4>
          <input type="text" class="form-control" placeholder="관련 페이지" v-model="linkUrl">
        </div>

        <div class="event-content">
          <div class="row">
            <h4 class="ml-3">대표 이미지</h4>
            <input ref="thumbnailImage" type="file" hidden @change="onChangeThumbnail">
            <button type="button" class="btn btn-success btn-sm ml-3" @click="onUploadThumbnail">이미지 등록</button>
          </div>
          <div class="preview-img mt-2">
            <img id="inner-img" class="d-flex mx-auto" v-if="thumbnail" :src="thumbnail" alt="">
          </div>
        </div>

        <!-- 뒤로가기, 미리보기, 임시저장 -->
        <div class="row justify-content-end mt-5 mb-5" id="content-btn">
          <div>
            <button type="button" class="btn btn-dark btn-sm mr-2" @click="$router.go(-1)">뒤로가기</button>
          </div>
          <div v-if="($route.params.method == 'update')">
            <button type="button" class="btn btn-primary btn-sm" @click="onRegister">수정하기</button>
          </div>
          <div v-else>
            <button type="button" class="btn btn-primary btn-sm" @click="onRegister">등록하기</button>
          </div>
        </div>  

      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data() {
    return {
      title: '',
      thumbnail: '',
      file: '',
      linkUrl: '',
    }
  },
  computed: {
    ...mapState('main', ['image']),
  },
  watch: {
    image(val) {
      this.title = val.title
      this.thumbnail = 'http://k3c205.p.ssafy.io'+val.image
      this.linkUrl = val.url
    }
  },
  methods: {
    ...mapActions('main', ['getImage', 'postImage', 'putImage']),
    onUploadThumbnail() {
      this.$refs.thumbnailImage.click()
    },
    onChangeThumbnail(e) {
      const file = e.target.files[0]
      this.file = file
      this.thumbnail = URL.createObjectURL(file)
    },
    onRegister() {
      const mainImageData = new FormData()
      mainImageData.append('image', this.file)
      mainImageData.append('title', this.title)
      mainImageData.append('url', this.linkUrl)
      mainImageData.append('is_active', "False")
      mainImageData.append('priority', 1)
      if (this.$route.params.method == 'update') {
        this.putImage({ id: this.image.id, mainImageData: mainImageData})
      } else {
        this.postImage(mainImageData)
      }
    },

  },
  created() {
    if (this.$route.params.method == 'update') {
      this.getImage(this.$route.params.id)
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
  width: 490px;
  height: 150px;
  background-color: ghostwhite;
  border: 1px solid #ced4da;
  border-radius: 10px;
}

#inner-img {
  width : auto;
  height: 148px;
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