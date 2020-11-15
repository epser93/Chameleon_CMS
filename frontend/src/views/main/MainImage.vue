<template>
  <div v-if="images" class="container pl-0">
    <div v-if="images" class="table-container">
      <div class="btn-background">
        <div class="event-btn align-items-center mt-3 mb-3">
          <h5 class="mb-0">대표 이미지</h5>
          <button type="button" class="btn btn-info btn-sm" @click="onCreate()">추가</button>
        </div>
      </div>
      <table class="table">
        <thead class="">
          <tr>
            <th scope="col">이미지 제목</th>
            <th scope="col">상태</th>
            <th scope="col">이미지 보기</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(image, index) in imagesForList" :key="index">
            <td>{{ image.title }}</td>
            <!-- 스위치 -->
            <td v-if="image.is_active" class="row justify-content-center">
              <span class="badge badge-success" @click="changeActive(image)">활성화</span>
            </td>
            <td v-else class="row justify-content-center">
              <span class="badge badge-danger" @click="changeActive(image)">비활성화</span>
            </td>
            <!-- 스위치 -->
            <td><button type="button" class="btn btn-outline-secondary btn-sm" @click="onClickWindows(image.image)">보기</button></td>
            <td><button type="button" class="btn btn-warning btn-sm" @click="onUpdate(image.id)">수정</button></td>
          </tr>
        </tbody>
      </table>
      <div class="page-navi">
        <nav aria-label="Page navigation example">
          <ul v-if="pages == 0" class="pagination align-items-center">
            <li class="page-item">
              <img src="@/assets/icons/caret-left.svg" width="26" height="26" title="caret-left" @click="prevPage()">
            </li>
            <p> {{ nowPage + 1 }}  / {{ pages + 1}} </p>
            <li class="page-item">
              <img src="@/assets/icons/caret-right.svg" width="26" height="26" title="caret-right" @click="nextPage()">
            </li>
          </ul>
          <ul v-else class="pagination">
            <li class="page-item">
              <img v-if="nowPage == 0" src="@/assets/icons/caret-left.svg" width="26" height="26" title="caret-left" @click="prevPage()">
              <img v-else src="@/assets/icons/caret-left-fill.svg" width="26" height="26" title="caret-left-fill" @click="prevPage()">
            </li>
            <p> {{ nowPage + 1 }}  / {{ pages }} </p>
            <li class="page-item">
              <img v-if="nowPage == (pages-1)" src="@/assets/icons/caret-right.svg" width="26" height="26" title="caret-right" @click="nextPage()">
              <img v-else src="@/assets/icons/caret-right-fill.svg" width="26" height="26" title="caret-right-fill" @click="nextPage()">
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data() {
    return {
      perPage: 7,
      nowPage: 0,
    }
  },
  computed: {
    ...mapState('main',['images']),
    rows() {
      return this.images.length
    },
    pages() {
      return Math.ceil(this.images.length/this.perPage)
    },
    imagesForList() {
      return this.images.slice(
        (this.nowPage) * this.perPage,
        (this.nowPage + 1) * this.perPage
      )
    },
  },
  methods: {
    ...mapActions('main', ['getImages', 'delImage', 'actImage']),
    onCreate() {
			this.$router.push({name: 'MainImageCreate', params: {method: 'create'}}, () => {})
    },
    onUpdate(id) {
			this.$router.push({name: 'MainImageUpdate', params: {method: 'update', id: id}}, () => {})
    },
    onClickWindows(url) {
      window.open(url) 
    },
    changeActive(image){
      if (confirm("상태를 변경하시겠습니까?") == true){    //확인
          if (image.is_active) {
            this.delImage(image.id)
          }
          else {
            this.actImage(image.id)
          }
      }
    },
    prevPage() {
      if (this.nowPage > 0) {
        this.nowPage -= 1
      }
    },
    nextPage() {
      if (this.nowPage < this.pages-1) {
        this.nowPage += 1
      }
    }
  },
  created() {
    this.getImages()
  }
}
</script>

<style scoped>
.table-container {
  width: 100%;
  text-align: center;
}

.event-btn {
  display: flex;
}

td {
  padding-top: 16px;
  padding-bottom: 10px;
}

.page-navi {
  position: absolute;
  bottom: 0;
  left: 50%;
}

.custom-control-label {
  cursor: pointer;
}

span {
  cursor: pointer;
  margin-top: 4px;
}

.page-item {
  cursor: pointer;
}
</style>