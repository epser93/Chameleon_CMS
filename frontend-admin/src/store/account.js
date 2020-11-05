import axios from 'axios'
import SERVER from '@/api/drf'
import cookies from 'vue-cookies'
import router from '@/router'

export default {
  namespaced: true,

  state: {
    // data
    authToken: '',
    userInfo: '',

  },

  getters: {
    // watch, computed
    config(state) {
      return {
        headers: {
          'Authorization' : 'Token ' + state.authToken
        }
      }
    }

  },

  mutations: {
    // state 값을 변경 시켜주기 위한 함수
    SET_TOKEN(state, payload) {
      state.authToken = payload
      cookies.set('auth-token', payload)
    },

    SET_USERINFO(state, payload) {
      state.userInfo = payload
    },

  },

  actions: {
    // API 함수
    userLogin({ commit, dispatch }, loginData) {
      axios.post(SERVER.URL + SERVER.ROUTER.login, loginData)
        .then(res => {
          cookies.set('auth-token', res.data.key)
          commit('SET_TOKEN', res.data.key)
          dispatch('loginRoute')
          dispatch('getUserInfo')
        })
        .catch(error => {alert(error.response.data.message)})
    },

    loginRoute({ getters }) {
      axios.get(SERVER.URL + SERVER.ROUTER.userinfo, getters.config)
        .then(res => {
          if (res.data.is_superuser ){
            router.push({ name : 'Manage'})
          } else {
            router.push({ name : 'Data'})
          }
        })
        .catch(error => console.log(error.response))
    },

    getUserInfo({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.userinfo, getters.config)
        .then(res => {
          commit('SET_USERINFO', res.data)
        })
        .catch(error => alert(error.response.data.message))
    }

  },
}