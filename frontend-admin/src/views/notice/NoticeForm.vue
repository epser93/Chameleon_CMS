<template>
  <div class="form-root">
    <div class="title-division">
      <div class="title">
        제목
      </div>
      <div>
        <input class="title-input" type="text" v-model="title">
      </div>
    </div>
    <div class="contents-division">
      <div class="contents">
        내용
      </div>
      <div>
        <textarea class="contents-input" name="contents" id="noticeContents" cols="30" rows="10" v-model="contents"></textarea>
      </div>
    </div>
    <div class="image-division">
      <p class="image">공지사항 이미지 업로드</p>
      <input ref="imageInput" type="file" hidden @change="onChangeImages">
      <button type="button" class="btn btn-success btn-sm" @click="onClickImageUpload">업로드</button>
      <div class="preview-img">
        <img id="inner-img" v-if="imageUrl" :src="imageUrl">
      </div>
    </div>  
    <div class="row justify-content-end btn-division">
      <div >
        <button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows">미리보기</button>
      </div>
      <div v-if="!noticeInfo || noticeInfo.is_temp">
        <button type="button" class="btn btn-secondary btn-sm" @click="onClickTemp">임시저장</button>
      </div>
      <div>
        <button type="button" class="btn btn-success btn-sm" @click="onActivate">등록</button> 
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SERVER from '@/api/drf'
export default {
  data() {
    return {
      imageUrl: null,
      title : null,
      contents: null,
      imageFile : null,
      noticeInfo : null,
    }
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
      const config = {
        headers: {
          'Authorization' : 'Token ' + this.$cookies.get('auth-token'),
          'Content-Type' : 'multipart/form-data',
        }
      }
      let formdata = new FormData()
      if (this.imageFile) {
        formdata.append("image", this.imageFile)
      }
      formdata.append("title", this.title)
      formdata.append("content", this.contents)
      if (!this.$route.params.id) { // 바로 등록의 경우 
        formdata.append("is_temp", 'False')  
        axios.post(SERVER.URL + SERVER.ROUTER.notice, formdata, config)
          .then(res => {
            console.log(res)
            this.$router.push({ name : 'Notice'})
          })
          .catch(error => console.log(error.response))
      } else { // 임시저장후 등록의 경우 수정 + 활성이 한번에 이루어짐
        axios.put(SERVER.URL + SERVER.ROUTER.notice + this.$route.params.id, formdata, config)
          .then(() =>{
            axios.post(SERVER.URL + SERVER.ROUTER.notice + this.$route.params.id + '/')
              .then(res => {
                console.log('활성', res)
                this.$router.push({ name : 'Notice' })
              })
              .catch(error => console.log(error.response))
          })
      }
    },
    onClickTemp(){
      const config = {
        headers: {
          'Authorization' : 'Token ' + this.$cookies.get('auth-token'),
          'Content-Type' : 'multipart/form-data',
        }
      }
      let formdata = new FormData()
      if (this.imageFile) {
        formdata.append("image", this.imageFile)
      } 
      formdata.append("title", this.title)
      formdata.append("content", this.contents)
      if (!this.$route.params.id) { // 첫글 바로 임시등록할 때
        axios.post(SERVER.URL + SERVER.ROUTER.notice, formdata, config)
          .then(() => {
            this.$router.push({ name : 'Notice' })
          })
          .catch(error => console.log(error.response))
      } else { // 임시 등록 후 다시 임시등록을 할 때
        axios.put(SERVER.URL + SERVER.ROUTER.notice + this.$route.params.id, formdata, config)
          .then(res => {
            console.log(res)
            this.$router.push({ name : 'Notice' })
          })
          .catch(error => console.log(error.response))
      }
    },
    onClickWindows(){
      var url="test.html";
      window.open(url,"",);
    },
    init() {
      if (this.$route.params.id) {
        axios.get(SERVER.URL + SERVER.ROUTER.notice + this.$route.params.id)
          .then(res => {
            console.log(res.data)
            this.noticeInfo = res.data
            console.log('인포', this.noticeInfo)
            this.title = res.data.title
            this.contents = res.data.content
            this.imageUrl = SERVER.domain + res.data.image
            console.log(this.imageUrl)
          })
          .catch(error => console.log(error.response))
      }
    }
  },
  created() {
    this.init()
  }
}

</script>

<style scoped>
#inner-img{
  width: 400px;
  text-align: center;
    
}
.question{
  cursor: pointer;
}
.btn{
  width: 80px
}

.form-root {
  display: flex;
  flex-direction: column;
  width: 50%;
}

.title-input {
  width: 100%;
}

.contents-input {
  width: 100%;
}

.title {
  font-size :30px;
  font-weight: bold;
}

.contents {
  font-size: 30px;
  font-weight: bold;
}

.image {
  font-size: 30px;
  font-weight: bold;
}

.title-division {
  margin-bottom: 30px;
}

.contents-division {
  margin-bottom: 30px;
}

.image-division {
  margin-bottom: 30px;
}

.btn-division {
  margin-bottom: 30px;
}
</style>