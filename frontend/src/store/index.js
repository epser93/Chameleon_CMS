import Vue from 'vue'
import Vuex from 'vuex'

import account from './account'
import event from './event'
import category from './category'
import notice from './notice'
import main from './main'
import customer from './customer'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    account,
    event,
    category,
    notice,
    main,
    customer,
  }
})
