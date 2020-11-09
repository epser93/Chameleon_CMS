<template>
  <div class="container">
    <div class="item row">
      <div class="col-8">
        <div class="item-content">
          <h4>카테고리 : </h4>
        </div>
        <div class="item-content">
          <h4>제품명</h4>
          <input type="text" class="form-control" placeholder="명칭을 입력해주세요" aria-label="Username">
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
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1">
                <label class="form-check-label" for="inlineRadio1">캐로우셀</label>
              </td>
              <td>          
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2">
                <label class="form-check-label" for="inlineRadio2">격자</label>
              </td>
            </tr>
          </table>
        </div>

        <div class="item-content">
          <h4>제품 소개</h4>
              <input ref="imageInput" type="file" hidden @change="onChangeImages">
              <button type="button" class="btn btn-success btn-sm" @click="onClickImageUpload">업로드</button>
          <div class="preview-img">
            <img id="inner-img" v-if="imageUrl" :src="imageUrl">
          </div>
        </div>
        <div class="item-content">
          <h4>제품 사양 카테고리</h4>
          <table>
            <tr>
              <td>
                태그1
              </td>
              <td>
                태그2
              </td>
            </tr>
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
          </div>
        </div>  
      </div>
      <!-- history -->
      <div class="col-4" id="history">
        <div class="temp-part">
          <h1>History</h1>
        </div>
        <div class="temp-part-history">
          <ul v-if="history.length">
            <li v-for="(his,index) in history.slice().reverse()" :key="index">
              <div class="history-btn" :id="`history-${index}`" @click="onHistory(his), fixHistory(index)">
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
</template>

<script>

export default {
  data() {
    return {
        imageUrl: null,
        aboutText: {
          tags:[],
        },
        tag: null,
        history: [],
    }
  },
  methods: {
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
    onClickRegister(){
      console.log('dfdfdf')
    },
    onClickTemp(){
      console.log('모든 데이터를 보내면 됌')
    },
    onClickWindows(){
      var url="test.html";
      window.open(url,"",);
    },

    onClickImageUpload() {
        this.$refs.imageInput.click();
    },
    onChangeImages(e) {
        console.log(e.target.files)
        const file = e.target.files[0];
        this.imageUrl = URL.createObjectURL(file);
    },

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

#history {
  border: 1px solid gray;
  padding: 10px;
}

</style>