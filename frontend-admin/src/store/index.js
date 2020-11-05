import Vue from 'vue'
import Vuex from 'vuex'

import account from './account'
import category from './category'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    account,
    category,
  }
})
