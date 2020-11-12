import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    images: '',
    image: '',

  },

  getters: {

  },

  mutations: {
    SET_IMAGES(state, payload) {
      state.images = payload
    },

    SET_IMAGE(state, payload) {
      state.image = payload
    }
  },

  actions: {
    getImages({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.carousel, rootGetters['account/formconfig'])
        .then((res) => {
          commit('SET_IMAGES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    postImage({ rootGetters }, mainImageData) {
      axios.post(SERVER.URL + SERVER.ROUTER.carousel, mainImageData, rootGetters['account/formconfig'])
        .then((res) => {
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getImage({ rootGetters, commit }, id) {
      axios.get(SERVER.URL + SERVER.ROUTER.carousel + id + '/', rootGetters['account/config'])
        .then((res) => {
          commit('SET_IMAGE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      },

    putImage({ rootGetters }, {id, mainImageData}) {
      axios.put(SERVER.URL + SERVER.ROUTER.carousel + id + '/', mainImageData, rootGetters['account/config'])
        .then((res) => {
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  
    delImage({ dispatch, rootGetters }, id) {
      axios.delete(SERVER.URL + SERVER.ROUTER.carousel + id + '/', rootGetters['account/config'])
      .then(() => {
        alert("등록이 해제되었습니다.")
        dispatch('getImages')
      })
      .catch((err) => {
        console.log(err)
      })   
    },
    
    actImage({ dispatch, rootGetters }, id) {
      axios.post(SERVER.URL + SERVER.ROUTER.carousel + id + '/', null, rootGetters['account/config'])
      .then(() => {
        alert("등록이 완료되었습니다.")
        dispatch('getImages')
      })
      .catch((err) => {
        console.log(err)
      })   
    },

  }
}