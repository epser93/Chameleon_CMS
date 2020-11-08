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
    axios.get(SERVER.URL + SERVER.ROUTER.event, rootGetters['account/config'])
      .then((res) => {
        commit('SET_EVENTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
   },

   postEvent({ rootGetters }, eventData) {
    // FormData의 key 확인
    for (let key of eventData.keys()) {
      console.log(key);
    }

    // FormData의 value 확인
    for (let value of eventData.values()) {
      console.log(value);
    }
    
    axios.post(SERVER.URL + SERVER.ROUTER.event, eventData, rootGetters['account/formconfig'])
      .then((res) => {
        console.log(res.data)
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
      axios.post(SERVER.URL + SERVER.ROUTER.event + eid + '/', rootGetters['account/config'])
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