import axios from 'axios'
import SERVER from '@/api/drf'
// import cookies from 'vue-cookies'
import router from '@/router'
export default {
  namespaced: true,

  state: {
    notices: '', // 공지 리스트
    notice: '', // 특정 공지
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
  },

  actions: {
    // 공지 리스트 조회
    getNotices({ commit, rootGetters }) {
      axios.get(SERVER.URL + SERVER.ROUTER.notice, rootGetters['account/config'])
        .then (res => {
          commit('SET_NOTICES', res.data)
        })
        .catch (error => console.log(error.response))
    },

    // 특정 공지 조회
    getNotice({ commit, rootGetters }, id) {
      axios.get(SERVER.URL + SERVER.ROUTER.notice + id, rootGetters['account/config'])
        .then(res => {
          commit('SET_NOTICE', res.data)
        })
        .catch(error => console.log(error.response))
    },

    // 공지 종료
    endNotice({ rootGetters }) {
      axios.delete(SERVER.URL + SERVER.ROUTER.notice + router.currentRoute.params.id, rootGetters['account/config'])
      .then(() => {
        router.push({ name : 'Notice' })
      })
      .catch(error => console.log(error.response))
    },

    // customer 공지 조회
    getCustomerNotice({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.notice)
        .then(res => {
          commit('SET_NOTICES', res.data)
        })
        .catch(error => console.log(error.response))
    }
  },
}