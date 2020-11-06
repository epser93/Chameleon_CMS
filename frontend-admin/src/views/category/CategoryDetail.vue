<template>
  <div class="container">
    <div class="category row">
      <div class="col-8">
        <div class="category-content">
          <h4>제품군</h4>
          <input type="text" class="form-control" placeholder="명칭을 입력해주세요" v-model="categoryName">
        </div>
        
        <div class="category-content">
          <h4>템플릿 선택</h4>
          <table class="template-table">
            <tr>
              <td>
                <img src="@/assets/product/template1.jpg" alt="template1">
              </td>
              <td>
                <img src="@/assets/product/template2.jpg" alt="template2">
              </td>
            </tr>
            <tr>
              <td>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="1" v-model="picked">
                  <label class="form-check-label" for="inlineRadio1">사양 위주</label>
                </div>
              </td>
              <td>       
                   
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="2" v-model="picked">
                <label class="form-check-label" for="inlineRadio2">디자인 위주</label>
              </td>
            </tr>
          </table>
        </div>

        <div class="category-content">
          <h4>제품군 대표 이미지</h4>
              <input ref="imageInput" type="file" hidden @change="onChangeImages">
              <button type="button" class="btn btn-success btn-sm" @click="onClickImageUpload">업로드</button>
          <div class="preview-img">
            <img id="inner-img" v-if="imageUrl" :src="imageUrl">
          </div>
        </div>
        <div class="category-content">
          <h4>제품 사양 카테고리</h4>
          <!-- 태그 -->
          <div class="tag">
            <span v-for="(tag,index) in tags" :key="index" class="badge badge-pill badge-light mr-2 p-2" @click="deleteTag(index)">{{ tag }}<span id="closeTag">  x</span></span>
          </div>
          <input class="form-control" placeholder="사양 입력후 enter키를 눌러주세요" id="category-desc" type="text" v-model="tag" @keydown.enter="postTag">
        </div>

        <div class="row justify-content-end" id="content-btn">
          <div>
            <button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows">미리보기</button>
          </div>
          <div>
            <button type="button" class="btn btn-secondary btn-sm" @click="onClickTemp">임시저장</button>
          </div>
          <div>
            <button type="button" class="btn btn-success btn-sm" @click="onClickRegister">등록</button> 
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
      </div>

    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data() {
    return {
        categoryName: null,
        picked: 1,
        tags: [],
        priority: 1,
        tag: null,
        // aboutText: {
          //   tags:[],
        // },

        imageUrl: null,
        history: [],
    }
  },
  methods: {
    ...mapActions('category', [ 'categoryRegister', '' ]),
    onClickRegister(){
      const categoryData = {
        name: this.categoryName,
        descriptions: this.tags,
        template: this.picked,
        priority: this.priority,
        // images: this.imageUrl
      }
      // console.log('카테고리 등록')
      this.categoryRegister(categoryData)
    },
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
    deleteTag(index) {
      this.tags.splice(index,1)
    },
    postTag() {
      const chkpatterns = /[~!@#$%^&*()_+|<>?:{}]/;
      if (this.tag === null || this.tag.replace(/^\s*|\s*$/g, '').length === 0) {
        alert('빈칸은 태그로 입력 불가능합니다.')
        this.tag = ""
      } else if (chkpatterns.test(this.tag)) {
        alert('특수문자는 입력할 수 없습니다.')
        this.tag = ""
      } else if (!this.tags.includes(this.tag)) {
        this.tags.push(this.tag)
        this.tag = ""
      } else {
        alert('중복된 태그입니다.')
        this.tag= ""
      }
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

.category-content {
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

#closeTag {
  opacity: 0.5;
  cursor: pointer;
}

#category-desc {
  width: 280px;
  margin-top: 20px;

}

#history {
  border: 1px solid gray;
  padding: 10px;
}

</style>