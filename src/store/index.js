import Vue from 'vue'
import Vuex from 'vuex'
import equipments from './modules/equipments'
import typeEquipment from './modules/typeEquipment'
import location from './modules/location'
import reservations from './modules/reservations'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    equipments,
    typeEquipment,
    location,
    reservations
  }
})