import axios from 'axios'
import SERVER from '@/api/drf'
import router from '@/router'

export default {
  namespaced: true,

  state: {
    images: '',
    image: '',

    products: '',
    allProducts: ''
  },

  getters: {

  },

  mutations: {
    SET_IMAGES(state, payload) {
      state.images = payload
    },

    SET_IMAGE(state, payload) {
      state.image = payload
    },

    SET_PRODUCTS(state, payload) {
      state.products = payload
    },
    SET_ALL_PRODUCTS(state, payload) {
      state.allProducts = payload
    },
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

    postImage({ rootGetters, dispatch }, mainImageData) {
      axios.post(SERVER.URL + SERVER.ROUTER.carousel, mainImageData, rootGetters['account/formconfig'])
        .then(() => {
          dispatch('getImages')
          router.push({ name : 'MainImage'})
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

    putImage({ rootGetters, dispatch }, {id, mainImageData}) {
      axios.put(SERVER.URL + SERVER.ROUTER.carousel + id + '/', mainImageData, rootGetters['account/config'])
        .then(() => {
          dispatch('getImages')
          router.push({ name : 'MainImage'})
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

    getProducts({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.main, rootGetters['account/config'])
        .then((res) => {
          commit('SET_PRODUCTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getAllProducts({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.search, rootGetters['account/config'])
        .then((res) => {
          commit('SET_ALL_PRODUCTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

  }
}