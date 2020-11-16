<template>
<div class="container">
  <h1>대표 이미지</h1>
  <div v-if="!files.length" class="file-upload-container">
    <div class="file-upload-example">
      <div class="notice-item">
        <div class="image-box">
          <label for="file">이미지 등록</label>
          <input type="file" id="file" ref="files" @change="imageUpload" multiple />
        </div>
      </div>
      <div class="notice-item">
        이미지는 최소 4장 및 (100x100)사이즈를 권장합니다.
      </div>
      <div class="notice-item">
        부족할 경우, 기본이미지(상품준비중)가 제공됩니다.
      </div>
    </div>
  </div>
  <div v-else class="file-preview-content-container">
    <div class="file-preview-container">
      <div v-for="(file, index) in files" :key="index" class="file-preview-wrapper">
        <div class="file-close-button" @click="fileDeleteButton" :name="file.number">
          x
        </div>
        <img :src="file.preview" />
      </div>
      <div class="file-preview-wrapper-upload">
        <div class="image-box" id="image-box-preview">
          <label for="file">추가 사진 등록</label>
          <input type="file" id="file" ref="files" @change="imageAddUpload" multiple />
        </div>
      </div>
    </div>
  </div>
    

</div>
</template>

<script>          
export default {
  data() {
    return {
      files: [], //업로드용 파일
      filesPreview: [],
      uploadImageIndex: 0 // 이미지 업로드를 위한 변수
    }
  },
  methods: {
    imageUpload() {
      // console.log(this.$refs.files.files);

      // this.files = [...this.files, this.$refs.files.files];
      //하나의 배열로 넣기
      let num = -1;
      for (let i = 0; i < this.$refs.files.files.length; i++) {
        this.files = [
          ...this.files,
            //이미지 업로드
            {
                //실제 파일
                file: this.$refs.files.files[i],
                //이미지 프리뷰
                preview: URL.createObjectURL(this.$refs.files.files[i]),
                //삭제및 관리를 위한 number
                number: i
            }
        ];
        num = i;
              //이미지 업로드용 프리뷰
              // this.filesPreview = [
              //   ...this.filesPreview,
              //   { file: URL.createObjectURL(this.$refs.files.files[i]), number: i }
              // ];
      }
      this.uploadImageIndex = num + 1; //이미지 index의 마지막 값 + 1 저장
      // console.log(this.files);
      // console.log(this.filesPreview);
      },

    imageAddUpload() {
      // console.log(this.$refs.files.files);

      // this.files = [...this.files, this.$refs.files.files];
      //하나의 배열로 넣기c
      let num = -1;
      for (let i = 0; i < this.$refs.files.files.length; i++) {
        // console.log(this.uploadImageIndex);
        this.files = [
          ...this.files,
          //이미지 업로드
          {
            //실제 파일
            file: this.$refs.files.files[i],
            //이미지 프리뷰
            preview: URL.createObjectURL(this.$refs.files.files[i]),
            //삭제및 관리를 위한 number
            number: i + this.uploadImageIndex
          }
        ];
        num = i;
      }
      this.uploadImageIndex = this.uploadImageIndex + num + 1;

      // console.log(this.files);
      // console.log(this.filesPreview);
    },
    fileDeleteButton(e) {
      const name = e.target.getAttribute('name');
      this.files = this.files.filter(data => data.number !== Number(name));
      // console.log(this.files);
    },
  }
}
</script>

<style scoped>
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
      /* text-align: center; */
  }

.image-box {
    /* margin-top: 30px; */
    padding-bottom: 20px;
    /* text-align: center; */
}

.image-box input[type='file'] {
    position: absolute;
    width: 0;
    height: 0;
    padding: 0;
    overflow: hidden;
    border: 0;
}

.image-box label {
    display: inline-block;
    padding: 10px 20px;
    background-color: #232d4a;
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
    background-color: #666666;
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
    background-color: #888888;
    width: 190px;
    height: 130px;
}
</style>