import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import equipments from './modules/equipments'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    equipments
  }
})