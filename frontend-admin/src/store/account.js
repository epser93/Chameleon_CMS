import axios from 'axios'
import SERVER from '@/api/drf'
import cookies from 'vue-cookies'
import router from '@/router'

export default {
  namespaced: true,

  state: {
    // data
    authToken: cookies.get('auth-token'),
    userInfo: '', // 특정 유저 정보
    accessUserInfos : '', // access 권한을 가진 유저들 정보
    unAccessedUserInfos : '', // access 권한을 가지지 못한 유저들 정보
    departments : '', // 부서 정보
  },

  getters: {
    // 유저 토큰
    config(state) {
      return {
        headers: {
          'Authorization' : 'Token ' + state.authToken
        }
      }
    }

  },

  mutations: {
    // 토큰 저장
    SET_TOKEN(state, payload) {
      state.authToken = payload
      cookies.set('auth-token', payload)
    },

    // 특정 유저 정보 상태 변경
    SET_USERINFO(state, payload) {
      state.userInfo = payload
    },

    // access 권한을 가진 유저들 상태 변경
    SET_ACCESSUSERINFOS(state, payload) {
      state.accessUserInfos = payload
    },

    // access 권한을 가지지 못한 유저들 상태 변경
    SET_UNACCESSUSERINFOS(state, payload) {
      state.unAccessedUserInfos = payload
    },

    SET_DEPARTMENTS(state, payload) {
      state.departments = payload
    }
  },

  actions: {
    // 로그인 
    userLogin({ commit, dispatch }, loginData) {
      axios.post(SERVER.URL + SERVER.ROUTER.login, loginData)
        .then(res => {
          cookies.set('auth-token', res.data.key)
          commit('SET_TOKEN', res.data.key)
          dispatch('loginRoute')
          dispatch('getUserInfo')
        })
        .catch(error => {console.log(error.response)})
    },

    // 로그인- 관리자 유무 판단 후 라우팅
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

    // 특정 유저 정보 조회
    getUserInfo({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.userinfo, getters.config)
        .then(res => {
          commit('SET_USERINFO', res.data)
        })
        .catch(error => alert(error.response.data.message))
    },

    // access 권한을 가진 모든 유저 조회
    getAccessUserInfo({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.usersearch + '?type=all', getters.config)
        .then(res => {
          commit('SET_ACCESSUSERINFOS', res.data)
        })
        .catch(error => console.log(error))
    },

    // access 권한을 못 가진 유저들 조회
    getUnAccessUserInfo({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.usersearch + "?type=is_access", getters.config)
        .then(res => {
          commit('SET_UNACCESSUSERINFOS', res.data)
          })
        .catch(error => console.log(error.response))
    },

    // access 권한 부여 
    approveAccess({ getters, dispatch }, userPk) {
      axios.post(SERVER.URL + SERVER.ROUTER.usermanage + `${userPk}/`, null, getters.config)
        .then(res => {
          alert(res.data.message)
          dispatch('getUnAccessUserInfo')
        })
        .catch(error => console.log(error.response))
    },

    // 부서 정보 조회
    getDepartments({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTER.department)
        .then(res => {
          commit('SET_DEPARTMENTS', res.data)
        })
        .catch(error => console.log(error.response))
    }
  },

  
}