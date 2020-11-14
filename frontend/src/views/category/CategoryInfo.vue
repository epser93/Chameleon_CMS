<template>
  <div class="container">
    <div class="category">
      <div class="col-8">
        <div class="form-title mt-5">
          <h3 v-if="update">Edit Product Category</h3>
          <h3 v-else>Add Product Category</h3>
          <hr>
        </div>
<!-- 
        <form name="myform">
          <input type="button" value="자식창 열기" @click="onClickWindows()"><br>
          부모창 Sender : <input type="text" name="sender" size="10" v-model="previewData"><br>
        </form> -->

        <div class="category-content">
          <h4>제품군</h4>
          <!-- {{category}} -->
          <input type="text" class="form-control" placeholder="명칭을 입력해주세요." v-model="categoryName">
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
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="2" v-model="picked">
                  <label class="form-check-label" for="inlineRadio2">디자인 위주</label>
                </div>
              </td>
            </tr>
          </table>
        </div>

        <div class="category-content">
          <div class="row">
            <h4 class="ml-3">제품군 대표 이미지</h4>
              <input ref="imageInput" type="file" hidden @change="onChangeImages">
              <button type="button" class="btn btn-success btn-sm ml-3" @click="onClickImageUpload">이미지 등록</button>
          </div>
          <div class="preview-img mt-2">
            <img id="inner-img" v-if="imageUrl" :src="imageUrl">
          </div>
        </div>
        <div class="category-content">
          <h4>제품 사양 카테고리</h4>
          <!-- 태그 -->
          <div class="tag">
            <span v-for="(tag,index) in tags" :key="index" class="badge badge-pill badge-light mr-2 p-2" @click="deleteTag(index)">{{ tag }}<span id="closeTag">  x</span></span>
          </div>
          <input class="form-control" placeholder="사양 입력 후 엔터키를 눌러주세요." id="category-desc" type="text" v-model="tag" @keydown.enter="postTag">
        </div>

        <div class="row justify-content-end mt-5 mb-5" id="content-btn">
          <div>
            <button type="button" class="btn btn-dark btn-sm mr-2" @click="$router.go(-1)">뒤로가기</button>
          </div>
          <div>
            <form name="myform">
              <input type="button"  class="btn btn-secondary btn-sm mr-2" value="미리보기" @click="onClickWindows()"><br>
              <input type="text" name="sender" size="10" v-model="previewData" hidden>
            </form>
            <!-- <button type="button" class="btn btn-secondary btn-sm mr-2" @click="onClickWindows">미리보기</button> -->
          </div>
          <div v-if="update">
            <button type="button" class="btn btn-primary btn-sm" @click="onClickUpdate">저장</button>
          </div>
          <div v-else>
            <button type="button" class="btn btn-primary btn-sm" @click="onClickRegister">추가</button> 
          </div>
        </div>  
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex'

export default {
  data() {
    return {
        categoryIdx: null,
        categoryName: null,
        picked: 1,
        tags: [],
        priority: 1,
        tag: null,
        imageUrl: null,
        update: false,
        image: null,
        initTags: [],
        initNums: [],
        delTagIdx: [],
        addTags: [],

        newWindow: '',
        previewData: '',
    }
  },
  computed: {
    ...mapGetters('category', ['category'])
  },
  
  watch: {
    category(val) {
      this.categoryIdx = val.id
      this.categoryName = val.name
      for(let i=0; i<val.description.length; i++) {
        this.tags.push(val.description[i].name)
        this.initTags.push(val.description[i].name)
        this.initNums.push(val.description[i].id)
      }
      this.picked = val.template.id
      this.imageUrl = 'http://k3c205.p.ssafy.io' + val.image.slice(56)

      // console.log(val)
    },
    
  },

  methods: {
    ...mapActions('category', [ 'categoryRegister', 'categoryUpdate' ]),
    ...mapMutations('category', ['SET_CATEGORY', 'SET_PREVIEWDATA']),
    onClickRegister(){
      const categoryData = new FormData()
      categoryData.append('name', this.categoryName)
      for(let i=0; i<this.tags.length; i++) {
        categoryData.append('descriptions', this.tags[i])
      }
      categoryData.append('image', this.image)
      categoryData.append('template', this.picked)
      categoryData.append('priority', this.priority)
      this.categoryRegister(categoryData)
    },
  
    onClickUpdate(){
      for(let i=0; i<this.initTags.length; i++) {
        if(!this.tags.includes(this.initTags[i])) {
          this.delTagIdx.push(this.initNums[i])
        } 
      }
      for(let i=0; i<this.tags.length; i++) {
        console.log(this.initTags)
        console.log(this.tags[i])
        if(!this.initTags.includes(this.tags[i])) {
          this.addTags.push(this.tags[i])
        } 
      }
      const categoryData = new FormData()
      categoryData.append('name', this.categoryName)
      for(let i=0; i<this.delTagIdx.length; i++) {
        categoryData.append('descriptions_delete', this.delTagIdx[i])
      }
      
      for(let i=0; i<this.addTags.length; i++) {
        categoryData.append('descriptions_add', this.addTags[i])
      }
      
      categoryData.append('image', this.image)
      categoryData.append('template', this.picked)
      categoryData.append('priority', this.priority)

      this.categoryUpdate({cid : this.categoryIdx, categoryData : categoryData})

    },
    onClickWindows(){
      const previewData = {
        "id" : this.categoryIdx,
        "name" : this.categoryName,
        "image" : this.imageUrl,
        "template" : this.picked,
        "items": [
        {
            "id": 1,
            "name": this.categoryName + '- 제품1',
            "price": 1280000,
            "template": 1,
            "images": [],
            "descriptions": [
                {
                    "id": 1,
                    "category_description": {                   
                        "id": 1,
                        "name": "제품 사양1"
                    },
                    "content": "미리보기입니다."
                },
                {
                    "id": 2,
                    "category_description": {                   
                        "id": 2,
                        "name": "제품 사양2"
                    },
                    "content": "미리보기입니다."
                },
                {
                    "id": 3,
                    "category_description": {                   
                        "id": 3,
                        "name": "제품 사양3"
                    },
                    "content": "미리보기입니다."
                },

            ]
        },
        
        ]
      }



      console.log(previewData['items'][0]['descriptions'])
      this.previewData = JSON.stringify(previewData)
      this.newWindow = window.open("http://localhost:8080/admin/preview", "page");
    },
    onClickImageUpload() {
        this.$refs.imageInput.click();
    },
    onChangeImages(e) {
        console.log(e.target.files)
        this.image = e.target.files[0];
        this.imageUrl = URL.createObjectURL(this.image);
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
  },
  created() {
    if(this.$route.params.update == 'update') {
      const cid = this.$route.params.cid
      this.SET_CATEGORY(cid)
      this.update = true
    }
  },
  destroyed() {
    this.SET_CATEGORY('');
  }
}
</script>

<style>
.form-control {
  width: auto;
}

.form-title {
  display: inline-block;
}

hr {
  border: 3px solid grey;
  border-radius: 3px;
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

.btn {
  margin-right: 20px;
}
</style>