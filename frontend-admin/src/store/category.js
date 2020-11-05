import axios from 'axios'
import SERVER from '@/api/drf'
import router from '@/router'

export default {
  namespaced: true,

  state: {
    // data
    categories: '',
  },

  getters: {
    // watch, computed

  },

  mutations: {
    // state 값을 변경 시켜주기 위한 함수
    SET_CATEGORIES(state, payload){
        state.categories = payload
    }
  },

  actions: {
    // API 함수
    categoryRegister({ rootGetters }, categoryData) {
      axios.post(SERVER.URL + SERVER.ROUTER.category, categoryData, rootGetters['account/config'])
        .then(() => {
            console.log("등록완료")
            router.push({ name : 'Product'})
        })
        .catch(error => {console.log(error.response)})
    },

    getCategoryList({ commit, rootGetters }) {
        axios.get(SERVER.URL + SERVER.ROUTER.category, rootGetters['account/config'])
        .then((res) => {
            commit('SET_CATEGORIES', res.data),
            console.log("카테고리리스트")
        })
        .catch(() => {console.log('에러')})
    },

    delCategory({ dispatch, rootGetters }, id) {
        axios.delete(SERVER.URL + SERVER.ROUTER.category + id + '/', rootGetters['account/config'])
        .then(() => {
          router.push({name:'Product'}, () => {})
          alert("등록이 해제되었습니다.")
          dispatch('getCategoryList')
        })
        .catch((err) => {
          console.log(err)
        })   
    },

    postCategory({ dispatch, rootGetters }, id) {
        axios.post(SERVER.URL + SERVER.ROUTER.category + id + '/', rootGetters['account/config'])
        .then(() => {
          router.push({name:'Product'}, () => {})
          alert("등록이 완료되었습니다.")
          dispatch('getCategoryList')
        })
        .catch((err) => {
          console.log(err)
        })   
    },


  }
}