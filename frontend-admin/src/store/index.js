import Vue from 'vue'
import Vuex from 'vuex'

import account from './account'
<<<<<<< HEAD
import event from './event'
=======
import category from './category'
>>>>>>> 6d8b5a5adcd01c31fa1c54215c629a0b0db3d51c

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    account,
<<<<<<< HEAD
    event,
=======
    category,
>>>>>>> 6d8b5a5adcd01c31fa1c54215c629a0b0db3d51c
  }
})
