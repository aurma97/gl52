import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store' 
import router from '@/router'

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import DateRangePicker from "@gravitano/vue-date-range-picker";
import axios from 'axios'

Vue.use(DateRangePicker);
Vue.use(Buefy)


Vue.config.productionTip = false


Vue.prototype.$http = axios;
const token = localStorage.getItem('token')

if (token){
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}


// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
