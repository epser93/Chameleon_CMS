<template>
  <div class="container">
    <div class="event row">
      <div class="col-8">
        <div class="event-content">
          <h4>카테고리</h4>
          <select name="category" id="category" v-model="category.part">
            <option disabled value="">Please select one</option>
            <option v-for="(category, index) in category.list" :key="index" :value="category.list">{{ category }}</option>
          </select>
        </div>

        <div class="event-content">
          <h4>이벤트 제목</h4>
          <input v-model="title" type="text">
        </div>
        
        <div class="event-content">
          <h4>이벤트 기간</h4>
          <table class="template-table">
            <tr>
              <td>
                <h2>시작 날짜</h2>
              </td>
              <td>
                <h2>종료 날짜</h2>
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

        <div class="event-content">
          <h4>이벤트 내용</h4>
          <textarea class="form-control" rows="5" cols="40" v-model="content"></textarea>
        </div>

        <div class="event-content">
          <h4>이벤트 썸네일</h4>
              <input ref="thumbImageInput" type="file" hidden @change="onChangeImages">
              <button type="button" class="btn btn-success btn-sm" @click="onClickImageUpload">업로드</button>
          <div class="preview-img">
            <img id="inner-img" v-if="imageUrl.thumbnail" :src="imageUrl.thumbnail">
          </div>
        </div>

        <div class="event-content">
          <h4>이벤트 상세</h4>
              <input ref="detailImageInput" type="file" hidden @change="onChangeImages">
              <button type="button" class="btn btn-success btn-sm" @click="onClickImageUpload">업로드</button>
          <div class="preview-img">
            <img id="inner-img" v-if="imageUrl.detail" :src="imageUrl.detail">
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
import Datepicker from "vuejs-datepicker";

export default {
  data() {
    return {
      title: '',
      content: '',
      category: {
        list: ['노트북', '냉장고'],
        part: ''
      },
      date: {
        start: '',
        end: ''
      },
      history: [],
      imageUrl: {
        thumbnail :'',
        detail: '',
      }
    }
  },
  components: {
    Datepicker,
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
    onChangeThumbImages(e) {
        console.log(e.target.files)
        const file = e.target.files[0];
        this.imageUrl.thumbnail = URL.createObjectURL(file);
    },
    onChangeDetailImages(e) {
        console.log(e.target.files)
        const file = e.target.files[0];
        this.imageUrl.detail = URL.createObjectURL(file);
    },

  }
}
</script>

<style>
textarea {
  resize: none;
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