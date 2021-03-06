import Vue from 'vue'
import Vuex from 'vuex'
import equipments from './modules/equipments'
import typeEquipment from './modules/typeEquipment'
import location from './modules/location'
import reservations from './modules/reservations'
import authentication from './modules/authentication'
import users from './modules/users'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    authentication,
    equipments,
    typeEquipment,
    location,
    reservations,
    users
  }
})