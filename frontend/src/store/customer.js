import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    mainItems: '',
    carousels: '',

    itemList: '',

    events: '',
    event: '',

    search: '',

    itemInfo: '', // 아이템 detail 정보
    detailImages: [], // 아이템 디테일 이미지
    thumbnails: [], // 아이템 썸네일 이미지
  },

  getters: {

  },

  mutations: {
    SET_MAINITEMS(state, payload) {
      state.mainItems = payload
    },
    SET_CAROUSELS(state, payload) {
      state.carousels = payload
    },

    SET_ITEMLIST(state, payload) {
      state.itemList = payload
    },

    SET_EVENTS(state, payload) {
      state.events = payload
    },
    SET_EVENT(state, payload) {
      state.event = payload
    },

    SET_SEARCH(state, payload) {
      state.search = payload
    },

    // 아이템 detail 상태 변경
    SET_ITEMINFO(state, payload) {
      state.itemInfo = payload
    },

    // detail 이미지 상태 변경
    SET_DETAILIMAGE(state, payload) {
      state.detailImages = payload 
    },

    // thumnail 이미지 상태 변경
    SET_THUMBNAILS(state, payload) {
      state.thumbnails = payload
    },

  },

  actions: {
    getMainItems({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.main)
      .then((res) => {
        commit('SET_MAINITEMS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getCarousels({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.carousel)
      .then((res) => {
        commit('SET_CAROUSELS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getItemList({ commit }, cid) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.category + cid + '/')
      .then((res) => {
        commit('SET_ITEMLIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getEvents({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.event)
      .then((res) => {
        commit('SET_EVENTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getEvent({ commit }, eid) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.event + eid + '/')
      .then((res) => {
        commit('SET_EVENT', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getSearch({ commit }, text) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.search + text)
      .then((res) => {
        commit('SET_SEARCH', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // 아이템 detail 조회
    getItemInfo({ commit }, cid) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.item + cid)
        .then(res => {
          commit('SET_ITEMINFO', res.data)
        })
        .catch(error => console.log(error.response))
    },

    // 이미지 나누기 썸네일, detail로
    divideImage({commit}, src) {
      const thumbnail = []
      const detail = []
      for (let i=0; i<src.length; i++) {
        if (src[i].is_thumbnail) {
          thumbnail.push(src[i])
        } else {
          detail.push(src[i])
        }
      }
      commit('SET_THUMBNAILS', thumbnail)
      commit('SET_DETAILIMAGE', detail)
    },
  }
}