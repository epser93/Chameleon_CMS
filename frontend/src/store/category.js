import axios from 'axios'
import SERVER from '@/api/drf'
import router from '@/router'

export default {
  namespaced: true,

  state: {
    // data
    categories: '',
    category: '',
    items: '',
    item: '',
    history: '',
  },

  getters: {
    // watch, computed
    category(state) {
      for (let i=0; i<state.categories.length; i++) {
        // console.log(state.categories[i])
				if (state.category == state.categories[i].id) {
          return state.categories[i]
          
				}
      }
      return null
    },
  },

  mutations: {
    // state 값을 변경 시켜주기 위한 함수
    SET_CATEGORIES(state, payload) {
      state.categories = payload
    },
    SET_CATEGORY(state, payload) {
      state.category = payload
    },
    SET_ITEMS(state, payload) {
      state.items = payload
    },
    SET_ITEM(state, payload) {
      state.item = payload
    },
    SET_HISTORY(state, payload) {
      state.history = payload
    },
  },

  actions: {
    // API 함수
    categoryRegister({ rootGetters, dispatch }, categoryData) {
      // console.log(categoryData)
      axios.post(SERVER.URL + SERVER.ROUTER.category, categoryData, rootGetters['account/config'])
        .then(() => {
            // console.log("등록완료")
            dispatch('getCategoryList')
            router.push({ name : 'Product'})
        })
        .catch(error => {console.log(error.response)})
    },

    categoryUpdate({ rootGetters, dispatch }, {cid, categoryData}) {
      axios.put(SERVER.URL + SERVER.ROUTER.category + cid + '/', categoryData, rootGetters['account/config'])
        .then(() => {
            // console.log("수정완료")
            dispatch('getCategoryList')
            router.push({ name : 'Product'})
        })
        .catch(error => {console.log(error.response)})
    },

    getCategoryList({ rootGetters, commit }) {
        axios.get(SERVER.URL + SERVER.ROUTER.category, rootGetters['account/config'])
        .then((res) => {
            commit('SET_CATEGORIES', res.data)
            // console.log("카테고리리스트")
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
        axios.post(SERVER.URL + SERVER.ROUTER.category + id + '/', null, rootGetters['account/config'])
        .then(() => {
          router.push({name:'Product'}, () => {})
          alert("등록이 완료되었습니다.")
          dispatch('getCategoryList')
        })
        .catch((err) => {
          console.log(err)
        })   
    },

    itemRegister({ rootGetters, dispatch }, {cid, itemData}) {
      axios.post(SERVER.URL + SERVER.ROUTER.item, itemData, rootGetters['account/config'])
        .then(() => {
            // console.log("등록완료")
            router.push({name:'ProductItem'}, () => {})
            dispatch('getItem', cid)
        })
        .catch(error => {console.log(error.response)})
    },


   
    getItem({ rootGetters, commit }, id) {
      // console.log(SERVER.URL + SERVER.ROUTER.category + id + '/')
      axios.get(SERVER.URL + SERVER.ROUTER.category + id + '/', rootGetters['account/config'])
      .then((res) => {
        commit('SET_ITEMS', res.data)
      })
      .catch(() => {console.log('왜에러남')})
    },

    delItem({ dispatch, rootGetters }, {cid, pid}) {
        axios.delete(SERVER.URL + SERVER.ROUTER.item + pid + '/', rootGetters['account/config'])
        .then(() => {
          router.push({name:'ProductItem'}, () => {})
          alert("등록이 해제되었습니다.")
          dispatch('getItem', cid)
        })
        .catch((err) => {
          console.log(err)
        })   
    },

    postItem({ dispatch, rootGetters }, {cid, pid}) {
        axios.post(SERVER.URL + SERVER.ROUTER.item + pid + '/', null, rootGetters['account/config'])
        .then(() => {
          router.push({name:'ProductItem'}, () => {})
          alert("등록이 완료되었습니다.")
          dispatch('getItem', cid)
        })
        .catch((err) => {
          console.log(err)
        })   
    },

    getItemDetail({ rootGetters, commit }, id) {
      // console.log(SERVER.URL + SERVER.ROUTER.category + id + '/')
      axios.get(SERVER.URL + SERVER.ROUTER.item + id + '/', rootGetters['account/config'])
      .then((res) => {
        commit('SET_ITEM', res.data)
      })
      .catch(() => {console.log('왜에러')})
    },

    getItemHistory({ rootGetters, commit }, id) {
      // console.log(SERVER.URL + SERVER.ROUTER.category + id + '/')
      axios.get(SERVER.URL + SERVER.ROUTER.itemhistory + id + '/', rootGetters['account/config'])
      .then((res) => {
        commit('SET_HISTORY', res.data)
      })
      .catch(() => {console.log('왜에')})
    },

    // 히스토리에 있는 내역으로 변경
    putItemHistory({ rootGetters, dispatch }, {cid, pid, hisData}) {
      axios.put(SERVER.URL + SERVER.ROUTER.item + pid + '/', hisData, rootGetters['account/config'])
        .then(() => {
            // console.log("원본에다가 등록완료")
            router.push({name:'ProductItem'}, () => {})
            dispatch('getItem', cid)
        })
        .catch(error => {console.log(error.response)})
    },
    

    postTempItem({ rootGetters, dispatch }, {pid, tmpData}) {
      axios.post(SERVER.URL + SERVER.ROUTER.itemhistory + pid + '/', tmpData, rootGetters['account/formconfig'])
      .then(() => {
        alert("임시저장이 완료되었습니다.")
        // router.push({name:'ProductItem'}, () => {})
        dispatch('getItemHistory', pid)
      })
      .catch((error) => {
        console.log(error.response)
      })   
    },


  }
}