import axios from 'axios'
import SERVER from '@/api/drf'
import router from '@/router'

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
      axios.get(SERVER.URL + SERVER.ROUTER.event, rootGetters['account/config'])
        .then((res) => {
          commit('SET_EVENTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    postEvent({ rootGetters, dispatch }, eventData) {
      axios.post(SERVER.URL + SERVER.ROUTER.event, eventData, rootGetters['account/formconfig'])
        .then(() => {
          dispatch('getEvents')
          router.push({ name : 'Event'})
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getEvent({ rootGetters, commit }, eid) {
      axios.get(SERVER.URL + SERVER.ROUTER.event + eid + '/', rootGetters['account/config'])
        .then((res) => {
          commit('SET_EVENT', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      },

    delEvent({ dispatch, rootGetters }, eid) {
      axios.delete(SERVER.URL + SERVER.ROUTER.event + eid + '/', rootGetters['account/config'])
      .then(() => {
        alert("등록이 해제되었습니다.")
        dispatch('getEvents')
      })
      .catch((err) => {
        console.log(err)
      })   
    },
  
    actEvent({ dispatch, rootGetters }, eid) {
      axios.post(SERVER.URL + SERVER.ROUTER.event + eid + '/', null, rootGetters['account/config'])
      .then(() => {
        alert("등록이 완료되었습니다.")
        dispatch('getEvents')
      })
      .catch((err) => {
        console.log(err)
      })   
    },
  },
}