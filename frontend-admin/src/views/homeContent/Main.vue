<template>
<div class="container">
  <div class="row">
    <div class="col-8">
      <div class="content-part">
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
              <p>url 넣어야하면 여기에서</p>
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
      <div class="content-part">
        <h1>추천 제품 등록</h1>
        <div>
          <!-- Button trigger modal -->
          <div v-if="checkedItemImg">
            <div v-for="(item, index) in checkedItemImg" :key="index">
              {{ item }}
              <img :src="item">
            </div>
          </div>


          <button type="button" class="recommand-btn" data-toggle="modal" data-target="#staticBackdrop">
            추가
          </button>

          <!-- 추천 제품 등록 Modal -->
          <div class="modal fade" id="staticBackdrop" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="staticBackdropLabel">추천 제품 추가</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="제품 검색">
                    <div class="input-group-append">
                      <button class="btn btn-outline-secondary" type="button" id="button-addon2">검색</button>
                    </div>
                  </div>
                  <!-- 제품 검색 리스트 -->
                  <div class="search-product">
                    <div v-if="checkedItem.length > 3">
                      <div v-for="(item, index) in items" :key="index">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" v-model="checkedItem" :id="index" :value="item.name" disabled>
                          <label class="form-check-label" :for="index">
                            {{ item.name }}
                          </label>
                        </div>
                      </div>
                        <!-- {{checkedItem}} -->
                    </div>
                    <div v-else>
                      <div v-for="(item, index) in items" :key="index">
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" v-model="checkedItem" :id="index" :value="item.name">
                          <label class="form-check-label" :for="index">
                            {{ item.name }}
                            <!-- {{ item }} -->
                          </label>
                        </div>
                      </div>
                        <!-- {{checkedItem}} -->
                    </div>
                  </div>
                  <!-- 제품 검색 결과 리스트 -->
                  <hr class="underline">
                  <div class="result-product">
                    <div class="result-product-header"><h5>선택된 제품 {{ checkedItem.length }}/4</h5></div>
                    <div v-for="(item, index) in checkedItem" :key="item">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" v-model="checkedItem" :id="index" :value="item">
                        <label class="form-check-label" :for="index">
                          {{ item }}
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="modal-footer">
                  <input type="submit" class="btn btn-secondary" data-dismiss="modal" value="추가" @click.prevent="addProduct">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row justify-content-end" id="content-btn">
        <div >
          <button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows">미리보기</button>
        </div>
        <div >
          <button type="button" class="btn btn-secondary btn-sm" @click="onClickTemp">임시저장</button>
        </div>
      </div>  
    </div>

    <div class="col-4" id="history">
      <div>
        <div class="temp-part">
          <h1>History</h1>
        </div>
        <div class="temp-part-history">
          <ul v-if="history.length">
            <li v-for="(his,index) in history.slice().reverse()" :key="index">
              <div class="history-view" @click="onHistory(his)">
                저장 {{ his.idx }}
                <p>{{ his.date }}</p>
              </div>
            </li>
          </ul>
        </div>
        <div>
          <button type="button" class="btn btn-success btn-sm" @click="onClickRegister">등록</button> 
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
// import $ from 'jquery'
// $(function(){
//   $('li').click(function(){
//     $('li').removeClass()
//     $(this).addClass('on')

//       })
//     })

export default {
  data() { 
    return {
      files: [], //업로드용 파일
      filesPreview: [],
      uploadImageIndex: 0, // 이미지 업로드를 위한 변수
      items: [
        { name: 'item1', chuchun_images: '@/assets/product/elec.png'},
        { name: 'item2', chuchun_images: '@/assets/product/mixer.png'},
        { name: 'item3', chuchun_images: '@/assets/product/oven.png'},
        { name: 'item4', chuchun_images: '@/assets/product/refre.png'},
        { name: 'item5', chuchun_images: '@/assets/product/washer.png'}
      ],
      checkedItem: [],
      checkedItemImg: [],
      history: [
        { 
          idx: 0,
          date: '2020-10-29',
          daepyo_images: ['@/assets/product/elec.png', '@/assets/product/refre.png'],
          chuchun_images: ['@/assets/product/elec.png']
        },
        { 
          idx: 1,
          date: '2020-10-29',
          daepyo_images: ['@/assets/product/elec.png', '@/assets/product/refre.png', '@/assets/product/washer.png'],
          chuchun_images: ['@/assets/product/elec.png', '@/assets/product/mixer.png']
        },
        { 
          idx: 2,
          date: '2020-10-30',
          daepyo_images: ['@/assets/product/oven.png', '@/assets/product/refre.png', '@/assets/product/washer.png', '@/assets/product/washer.png'],
          chuchun_images: [
             { name: 'item1', chuchun_images: '@/assets/product/elec.png'},
             { name: 'item2', chuchun_images: '@/assets/product/mixer.png'},
             { name: 'item3', chuchun_images: '@/assets/product/oven.png'},
          ]
        },
        { 
          idx: 3,
          date: '2020-10-31',
          daepyo_images: ['@/assets/product/elec.png', '@/assets/product/refre.png', '@/assets/product/washer.png', '@/assets/product/mixer.png'],
          name: 'item3',
          chuchun_images: ['@/assets/product/elec.png', '@/assets/product/mixer.png', '@/assets/product/oven.png']
        }
      ]
    }

  },
  
  methods: {
    onClickTemp(){
      console.log('모든 데이터를 보내면 됌')
    },
    onClickRegister(){
      console.log('dfdfdf')
    },
    onClickWindows(){
      var url="test.html";
      window.open(url,"",);
    },
    onHistory(his){
      console.log(his)
      this.checkedItem = []
      this.checkedItemImg = []
      for ( var i = 0; i < his.chuchun_images.length; i++ ) {
          this.checkedItem.push(his.chuchun_images[i].name) // .name
          this.checkedItemImg.push(his.chuchun_images[i].chuchun_images)
        }
      // console.log(this.checkedItem)
      // console.log(his)
      console.log(this.checkedItemImg)
    },
    imageUpload() {
      console.log(this.$refs.files.files);

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
      console.log(this.files);
      // console.log(this.filesPreview);
      },

    imageAddUpload() {
      console.log(this.$refs.files.files);

      // this.files = [...this.files, this.$refs.files.files];
      //하나의 배열로 넣기c
      let num = -1;
      for (let i = 0; i < this.$refs.files.files.length; i++) {
        console.log(this.uploadImageIndex);
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

      console.log(this.files);
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

.recommand-btn {
  background-color: #232d4a;
  color: white;
  border-radius: 5px;
  height: 40px;
  padding: 0 20px;
}

.form-control {
  border: none;
  border-bottom: solid 1px gray;
}

.modal-body {
  width: 90%;
  align-self: center;
}

.search-product {
  padding-bottom: 30px;
}

.underline {
  border: 1px solid gray;
}

.result-product {
  padding-bottom: 30px;
}

.result-product-header {
  margin-bottom: 20px;
}

.temp-part-history {

}

.history-view{
  cursor: pointer;
}

#content-btn {
  width: inherit;
}

#history {
  border: 1px solid gray;
  padding: 10px;
}

ul,li {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  font-size: 20px;
}

.clear{
  clear: both;
}

li.on{
  color:white;
  background-color:lightgray;
}
</style>