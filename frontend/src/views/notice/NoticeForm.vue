<template>
  <div class="container form-root">
    <div class="title-division">
      <div class="col-8">
        <div class="form-title mt-5">
          <h3 v-if="id">Edit Notice</h3>
          <h3 v-else>Add Notice</h3>
          <hr>
        </div>
        <!-- Notice 제목 -->
        <div class="notice-content">
          <h4>공지사항 제목</h4>
          <input v-model="title" class="form-control" type="text" placeholder=" 제목을 입력해 주세요.">
        </div>
        <!-- Notice 내용 -->
        <div class="notice-content">
          <h4>공지사항 내용</h4>
          <textarea class="form-control contents-input" name="contents" id="noticeContents" rows="5" cols="40" v-model="contents"></textarea>
        </div>        
        <!-- Notice 이미지 -->
        <div class="notice-content">
          <div class="row">
            <h4 class="ml-3">공지사항 이미지 업로드</h4>
            <input ref="imageInput" type="file" hidden @change="onChangeImages">
            <button type="button" class="btn btn-success btn-sm ml-3" @click="onClickImageUpload">이미지 등록</button>
          </div>
          <div class="preview-img mt-2">
            <img id="inner-img" class="d-flex mx-auto" v-if="imageUrl" :src="imageUrl" alt="">
          </div>
        </div>
        <div class="row btn-division justify-content-end mt-5 mb-5">
          <div>
            <button type="button" class="btn btn-dark btn-sm mr-2" @click="onRoute('Notice')">뒤로가기</button>
          </div>
          <div v-if="!noticeInfo || noticeInfo.is_temp">
            <button type="button" class="btn btn-warning btn-sm mr-2" @click="onClickTemp">임시저장</button>
          </div>
          <div>
            <button type="button" class="btn btn-primary btn-sm" @click="onActivate">등록하기</button>
          </div>
        </div> 
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SERVER from '@/api/drf'
import { mapGetters } from 'vuex'
export default {
  data() {
    return {
      imageUrl: null,
      title : null,
      contents: null,
      imageFile : null,
      noticeInfo : null,
      id: false,
    }
  },
  computed : {
    ...mapGetters('account', ['config', 'formconfig'])
  },
  methods: {
    onClickImageUpload() {
      this.$refs.imageInput.click();
    },
    onChangeImages(e) {
      const file = e.target.files[0]
      this.imageFile = file
      this.imageUrl = URL.createObjectURL(file)
    },
    onActivate(){
      let formdata = new FormData()
      if (this.imageFile) {
        formdata.append("image", this.imageFile)
      }
      formdata.append("title", this.title)
      formdata.append("content", this.contents)
      if (!this.$route.params.id) { // 바로 등록의 경우 
        formdata.append("is_temp", 'False')  
        axios.post(SERVER.URL + SERVER.ROUTER.notice, formdata, this.formconfig)
          .then(res => {
            console.log(res)
            this.$router.push({ name : 'Notice'})
          })
          .catch(error => console.log(error.response))
      } else { // 임시저장후 등록의 경우 수정 + 활성이 한번에 이루어짐
        axios.put(SERVER.URL + SERVER.ROUTER.notice + this.$route.params.id, formdata, this.formconfig)
          .then(() =>{
            axios.post(SERVER.URL + SERVER.ROUTER.notice + this.$route.params.id + '/', null, this.config)
              .then(res => {
                console.log('활성', res)
                this.$router.push({ name : 'Notice' })
              })
              .catch(error => console.log(error.response))
          })
      }
    },
    onClickTemp(){
      let formdata = new FormData()
      if (this.imageFile) {
        formdata.append("image", this.imageFile)
      } 
      formdata.append("title", this.title)
      formdata.append("content", this.contents)
      if (!this.$route.params.id) { // 첫글 바로 임시등록할 때
        axios.post(SERVER.URL + SERVER.ROUTER.notice, formdata, this.formconfig)
          .then(() => {
            this.$router.push({ name : 'Notice' })
          })
          .catch(error => console.log(error.response))
      } else { // 임시 등록 후 다시 임시등록을 할 때
        axios.put(SERVER.URL + SERVER.ROUTER.notice + this.$route.params.id, formdata, this.formconfig)
          .then(res => {
            console.log(res)
            this.$router.push({ name : 'Notice' })
          })
          .catch(error => console.log(error.response))
      }
    },
    init() {
      if (this.$route.params.id) {
        axios.get(SERVER.URL + SERVER.ROUTER.notice + this.$route.params.id, this.config)
          .then(res => {
            this.id = true
            this.noticeInfo = res.data
            this.title = res.data.title
            this.contents = res.data.content
            this.imageUrl = SERVER.domain + res.data.image.slice(56, res.data.image.length)
          })
          .catch(error => console.log(error.response))
      }
    },
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
  },
  created() {
    this.init()
  }
}

</script>

<style scoped>
.form-title {
  display: inline-block;
}

hr {
  border: 3px solid grey;
  border-radius: 3px;
}

.notice-content {
  margin-top: 30px;
}

.contents-input {
  width: auto;
  border: 1px solid #ced4da;
  border-radius: 10px;
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