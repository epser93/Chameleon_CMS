import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Bootstrap.
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'

// vue-cookies
import VueCookies  from 'vue-cookies'
Vue.use(VueCookies)

Vue.config.productionTip = false

// google-analytics
import VueAnalytics from 'vue-analytics';
Vue.use(VueAnalytics, {
    id: 'UA-183274370-1',
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
