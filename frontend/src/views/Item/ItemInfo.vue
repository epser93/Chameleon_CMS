<template>
  <div class="container">
    <div class="item row">
      <div class="col-8">
        <div class="item-content">
          <h4>카테고리 : {{ category.name }}</h4>
        </div>
        <div class="item-content">
          <h4>제품명</h4>
          <input type="text" class="form-control" placeholder="제품명을 입력해주세요" v-model="itemName">
        </div>
        <div class="item-content">
          <h4>가격</h4>
          <input type="number" class="form-control" placeholder="가격을 입력해주세요" v-model="itemPrice" min="0">
        </div>
        
        <div class="item-content">
          <h4>템플릿 선택</h4>
          <table class="template-table">
            <tr>
              <td>
                <img src="@/assets/product/template3.jpg" alt="template1">
              </td>
              <td>
                <img src="@/assets/product/template4.jpg" alt="template2">
              </td>
            </tr>
            <tr>
              <td>
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="3" v-model="picked">
                <label class="form-check-label" for="inlineRadio1">캐로우셀</label>
              </td>
              <td>          
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="4" v-model="picked">
                <label class="form-check-label" for="inlineRadio2">격자</label>
              </td>
            </tr>
          </table>
        </div>
        <!-- carousel에 들어갈 이미지들 -->
        <div class="content-part">
          <div class="row align-items-center">
            <h4 class="mb-0 ml-3">상세 이미지</h4>
          </div>
          <div v-if="!imageOfThumb.length" class="file-upload-container">
            <div class="file-upload-example">
              <div class="notice-item">
                <div class="image-box">
                  <label for="fileDetail">이미지 등록</label>
                  <input type="file" id="fileDetail" ref="detailImages" @change="imageUpload" multiple hidden/>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="file-preview-content-container">
            <div class="file-preview-container">
              <div v-for="(file, index) in imageOfThumb" :key="index" class="file-preview-wrapper">
                <div class="file-close-button" @click="fileDeleteButton" :name="file.number">
                  x
                </div>
                <img :src="file.preview" />
              </div>
              <div class="file-preview-wrapper-upload">
                <div class="image-box" id="image-box-preview">
                  <label for="fileDetail">추가 사진 등록</label>
                  <input type="file" id="fileDetail" ref="detailImages" @change="imageAddUpload" multiple hidden/>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 제품소개 이미지 -->
        <div class="content-part">
          <div class="row align-items-center">
            <h4 class="mb-0 ml-3">소개 이미지</h4>
          </div>
          <div v-if="!imageOfIntro.length" class="file-upload-container">
            <div class="file-upload-example">
              <div class="notice-item">
                <div class="image-box">
                  <label for="fileIntro">이미지 등록</label>
                  <input type="file" id="fileIntro" ref="introImages" @change="introUpload" multiple hidden/>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="file-preview-content-container">
            <div class="file-preview-container">
              <div v-for="(file, index) in imageOfIntro" :key="index" class="file-preview-wrapper">
                <div class="file-close-button" @click="introDeleteButton" :name="file.number">
                  x
                </div>
                <img :src="file.preview" />
              </div>
              <div class="file-preview-wrapper-upload">
                <div class="image-box" id="image-box-preview">
                  <label for="fileIntro">추가 사진 등록</label>
                  <input type="file" id="fileIntro" ref="introImages" @change="introAddUpload" multiple hidden/>
                </div>
              </div>
            </div>
          </div>
        </div>




        <div class="item-content">
          <h4>제품 사양 카테고리</h4>
          <table class="table">
            <tbody>
              <tr v-for="(desc, index) in category.description" :key="index">
                <th scope="row">{{ desc.name }}</th>
                <td><input type="text" class="form-control" v-model="itemDescText[index]"></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="row justify-content-end" id="content-btn">
          <div>
            <button type="button" class="btn btn-dark btn-sm mr-2" @click="$router.go(-1)">뒤로가기</button>
          </div>
          <div >
            <button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows">미리보기</button>
          </div>
          <div >
            <button type="button" class="btn btn-secondary btn-sm" @click="onClickTemp">임시저장</button>
          </div >
        </div>  
      </div>
      <!-- history -->
      <div class="col-4 mt-4">
      <div class="card text-center">
        <div class="card-header">
          <h3><img src="@/assets/icons/card-list.svg" alt="" width="32" height="32" title="card-list" class="mr-2">History</h3>
        </div>
        <div class="card-body">
          <ul v-if="history.length">
            <li v-for="(his,index) in history.slice().reverse()" :key="index">
              <div class="history-btn row justify-content-around" :id="`history-${index}`" @click="onHistory(his), fixHistory(index)">
                <strong>저장 {{ his.idx }}</strong>
                <p>{{ his.date }}</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>

    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'

export default {
  data() {
    return {
        itemName: null,
        itemPrice: null,
        is_temp: "False",
        picked: 3,
        categoryNum: null,
        itemDescId: [],
        itemDescText: [],
        // imageUrl: null,
        
        update_date: null,
        
        numOfImg: null,

        history: [],


        imageOfThumb: [],
        imageOfIntro: [],
        is_thumbnails: [],
        // files: [], //업로드용 파일

        uploadImageIndex: 0,
        uploadIntroIndex: 0,
    }
  },

  computed: {
    ...mapState('category', ['item']),
    ...mapGetters('category', ['category']),
  },

  watch: {
    item(val) {
      console.log(val)
      this.itemName = val.name
      this.itemPrice = val.price
      this.is_temp = val.is_temp
      this.picked = val.template.id
      this.update_date = val.update_date

      for(let i=0; i<val.descriptions.length; i++) {
        this.itemDescText.push(val.descriptions[i].content)
      }

      
      for (let i = 0; i < val.images.length; i++) {
        const imageData = {
          file: val.images[i].id,
          number: i,
          preview: 'http://k3c205.p.ssafy.io' + val.images[i].item_image
        }
        this.is_thumbnails.push(val.images[i].is_thumbnail)
        if(val.images[i].is_thumbnail == true) {
          this.imageOfThumb.push(imageData)
        } else {
          this.imageOfIntro.push(imageData)
        }
      }

      this.uploadImageIndex = this.imageOfThumb.length,
      this.uploadIntroIndex = this.imageOfIntro.length


      this.imageUrl = 'http://k3c205.p.ssafy.io' + val.image

    },
  },

  methods: {
    ...mapActions('category', ['itemRegister', 'getItemDetail']),

    fixHistory(idx) {
      for (let i=0; i<this.history.length; i++) {
        let className = '#history-' + i
        console.log(className)
        if (i == idx) {
          document.querySelector(className).classList.add('on')
        } else {
          document.querySelector(className).classList.remove('on')
        }
      }
    },
    onHistory(his){
      console.log(his)
    },
    onClickTemp(){
      const itemData = new FormData()
      itemData.append('name', this.itemName)
      itemData.append('price', this.itemPrice)
      itemData.append('is_temp', this.is_temp)
      itemData.append('category', this.categoryNum)
      itemData.append('template', this.picked)

      for(let i=0; i<this.itemDescId.length; i++) {
        itemData.append('descriptions_id', this.itemDescId[i])
        itemData.append('descriptions_content', this.itemDescText[i])
      }

      this.numOfImg = this.imageOfThumb.length +  this.imageOfIntro.length
      itemData.append('number', this.numOfImg)

      const idxTN = this.imageOfThumb.length

      for(let i=0; i<this.numOfImg; i++) {
        if(i < idxTN) {
          itemData.append('image' + i, this.imageOfThumb[i].file)
          itemData.append('is_thumbnails', "True")
        }
        else {
          itemData.append('image' + i, this.imageOfIntro[i-idxTN].file)
          itemData.append('is_thumbnails', "False")
        }
      }

      this.itemRegister({cid : this.category.id, itemData : itemData })
    },
    


    onClickWindows(){
      var url="test.html";
      window.open(url,"",);
    },

    imageUpload() {
      console.log(this.$refs.detailImages.files);
      let num = -1;
      for (let i = 0; i < this.$refs.detailImages.files.length; i++) {
        this.imageOfThumb = [
          ...this.imageOfThumb,
            //이미지 업로드
            {
                //실제 파일
                file: this.$refs.detailImages.files[i],
                //이미지 프리뷰
                preview: URL.createObjectURL(this.$refs.detailImages.files[i]),
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
      },

    imageAddUpload() {
      console.log(this.$refs.detailImages.files);
      let num = -1;
      for (let i = 0; i < this.$refs.detailImages.files.length; i++) {
        console.log(this.uploadImageIndex);
        this.imageOfThumb = [
          ...this.imageOfThumb,
          //이미지 업로드
          {
            //실제 파일
            file: this.$refs.detailImages.files[i],
            //이미지 프리뷰
            preview: URL.createObjectURL(this.$refs.detailImages.files[i]),
            //삭제및 관리를 위한 number
            number: i + this.uploadImageIndex
          }
        ];
        num = i;
      }
      this.uploadImageIndex = this.uploadImageIndex + num + 1;

      console.log(this.imageOfThumb);
    },
    fileDeleteButton(e) {
      const name = e.target.getAttribute('name');
      this.imageOfThumb = this.imageOfThumb.filter(data => data.number !== Number(name));
    },

    // intro

    introUpload() {
      console.log(this.$refs.introImages.files);
      let num = -1;
      for (let i = 0; i < this.$refs.introImages.files.length; i++) {
        this.imageOfIntro = [
          ...this.imageOfIntro,
            //이미지 업로드
            {
                //실제 파일
                file: this.$refs.introImages.files[i],
                //이미지 프리뷰
                preview: URL.createObjectURL(this.$refs.introImages.files[i]),
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
      this.uploadIntroIndex = num + 1; //이미지 index의 마지막 값 + 1 저장
      },

    introAddUpload() {
      console.log(this.$refs.introImages.files);
      let num = -1;
      for (let i = 0; i < this.$refs.introImages.files.length; i++) {
        console.log(this.uploadIntroIndex);
        this.imageOfIntro = [
          ...this.imageOfIntro,
          //이미지 업로드
          {
            //실제 파일
            file: this.$refs.introImages.files[i],
            //이미지 프리뷰
            preview: URL.createObjectURL(this.$refs.introImages.files[i]),
            //삭제및 관리를 위한 number
            number: i + this.uploadIntroIndex
          }
        ];
        num = i;
      }
      this.uploadIntroIndex = this.uploadIntroIndex + num + 1;

      console.log(this.imageOfIntro);
    },
    introDeleteButton(e) {
      const name = e.target.getAttribute('name');
      this.imageOfIntro = this.imageOfIntro.filter(data => data.number !== Number(name));
    },




  },

  created() {
    this.categoryNum = this.category.id
    for(let i=0; i<this.category.description.length; i++){
      // this.itemDescText.push('')
      this.itemDescId.push(this.category.description[i].id)
    }

    if(this.$route.params.update == 'update') {
      const pid = this.$route.params.pid
      this.getItemDetail(pid)
      this.update = true
    }
  }
}
</script>

<style>
.form-control {
  width: auto;
}

.template-table {
  text-align: center;
  width: 250px;
}

.item-content {
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
#history {
  border: 1px solid gray;
  padding: 10px;
}

</style>