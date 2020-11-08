import axios from 'axios'
import SERVER from '@/api/drf'
// import cookies from 'vue-cookies'
import router from '@/router'
export default {
  namespaced: true,

  state: {
    notices: '', // 공지 리스트
    notice: '', // 특정 공지
    image: '', // 이미지 url 가공
  },

  getters: {

  },

  mutations: {
    // 공지 리스트 상태 변경
    SET_NOTICES(state, payload) {
      state.notices = payload
    },

    // 특정 공지 상태 변경
    SET_NOTICE(state, payload) {
      state.notice = payload
    },

    // 이미지 url 가공
    SET_IMAGEURL(state, payload) {
      state.image = payload
    }
  },

  actions: {
    // 공지 리스트 조회
    getNotices({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.notice)
        .then (res => {
          console.log(res)
          commit('SET_NOTICES', res.data)
        })
        .catch (error => console.log(error.response))
    },

    // 특정 공지 조회
    getNotice({ commit }, id) {
      axios.get(SERVER.URL + SERVER.ROUTER.notice + id)
        .then(res => {
          commit('SET_NOTICE', res.data)
          commit('SET_IMAGEURL', SERVER.URL.slice(0,SERVER.URL.length-4) + res.data.image.substr(1))
        })
        .catch(error => console.log(error.response))
    },

    // 공지 종료
    endNotice() {
      axios.delete(SERVER.URL + SERVER.ROUTER.notice + router.currentRoute.params.id)
      .then(() => {
        router.push({ name : 'NoticeMain' })
      })
      .catch(error => console.log(error.response))
    }
  },
}