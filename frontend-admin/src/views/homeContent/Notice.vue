<template>
  <div>
    <div class="containter">
      <div class="row col-12 mr-auto justify-content-between">
        <h3 class="title-upload">Notice</h3>
        <div class="row">
          <input ref="imageInput" type="file" hidden @change="onChangeImages">
          <button type="button" class="btn btn-success btn-sm" @click="onClickImageUpload">업로드</button>
          <div class="col-4"><img class="question" @click="onClickImageUpload" src="@/assets/icons/question-circle.svg" alt="" width="32" height="32" title="question"></div>
        </div>
      </div>
        
      <p>공지사항 이미지 업로드</p>
      <div class="preview-img">
        <img id="inner-img" v-if="imageUrl" :src="imageUrl">
      </div>
    </div>

    <div class="row justify-content-end">
      <div >
        <button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows">미리보기</button>
      </div>
      <div >
        <button type="button" class="btn btn-secondary btn-sm" @click="onClickTemp">임시저장</button>
      </div>
      <div >
        <button type="button" class="btn btn-success btn-sm" @click="onClickRegister">등록</button> 
      </div>
    </div>

       

    



  </div>
</template>

<script>
import $ from 'jquery'


$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
export default {
  data() {
        return {
            imageUrl: null,
        }
    },
    methods: {
        onClickImageUpload() {
            this.$refs.imageInput.click();
        },
        onChangeImages(e) {
            console.log(e.target.files)
            const file = e.target.files[0];
            this.imageUrl = URL.createObjectURL(file);
        },
        onClickRegister(){
            
        },
        onClickTemp(){
            
        },
        onClickWindows(){
            var url="test.html";
            window.open(url,"",);
        }
    },
}

</script>

<style scoped>
.preview-img{
    background-color:ghostwhite;
    width: 450px;
    height: 250px;
    text-align: center;
    
}
.question{
    cursor: pointer;
}
.btn{
    width: 80px
}

</style>