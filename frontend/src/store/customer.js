import axios from 'axios'
import SERVER from '@/api/drf'

export default {
  namespaced: true,

  state: {
    events: '',
    event: '',
  },

  getters: {

  },

  mutations: {
    SET_EVENTS(state, payload) {
      state.events = payload
    },
    SET_EVENT(state, payload) {
      state.event = payload
    },
  },

  actions: {


    getEvents({ rootGetters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.event, rootGetters['account/config'])
      .then((res) => {
        commit('SET_EVENTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getEvent({ rootGetters, commit }, eid) {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.event + eid + '/', rootGetters['account/config'])
      .then((res) => {
        commit('SET_EVENT', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },

  }
}