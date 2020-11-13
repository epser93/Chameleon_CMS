import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    carousels: '',

    itemList: '',

    events: '',
    event: '',

    search: '',
  },

  getters: {

  },

  mutations: {
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
  },

  actions: {

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
  }
}