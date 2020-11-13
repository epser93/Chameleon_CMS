<template>
  <div v-if="images" class="container-fluid pl-0">
    <div v-if="images" class="table-container">
      <div class="btn-background">
        <div class="event-btn ml-3 mt-3 mb-3">
          <!-- <button type="button" class="btn btn-danger">삭제</button> -->
          <button type="button" class="btn btn-info ml-3" @click="onCreate()">생성</button>
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
          <tr v-for="(image, index) in images" :key="index">
            <td>{{ image.title }}</td>
            <!-- 스위치 -->
            <td v-if="image.is_active" class="row justify-content-center">
              <span class="badge badge-success" @click="changeActive(image)">활성화</span>
            </td>
            <td v-else class="row justify-content-center">
              <span class="badge badge-danger" @click="changeActive(image)">비활성화</span>
            </td>
            <!-- 스위치 -->
            <td><button type="button" class="btn btn-secondary btn-sm" @click="onClickWindows(image.image)">보기</button></td>
            <td><button type="button" class="btn btn-secondary btn-sm" @click="onUpdate(image.id)">수정</button></td>
          </tr>
        </tbody>
      </table>
      <div class="page-navi">
        <nav aria-label="Page navigation example justify-content-center">
          <ul class="pagination">
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li class="page-item active"><a class="page-link" href="#">1</a></li>
            <li class="page-item">
              <a class="page-link" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
              </a>
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
  computed: {
    ...mapState('main',['images']),
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
      window.open('http://k3c205.p.ssafy.io'+url.slice(56)) 
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
</style>