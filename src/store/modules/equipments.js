import equipmentsService from '../../services/equipmentsService'
import typeEquipmentsService from '../../services/typeEquipmentsService'
import locationService from '../../services/locationService'

const state = {
  equipments: [],
  equipment: [],
  types:[],
  locations:[],
  errors: []
}

const getters = {
  equipments: state => {
    return state.equipments
  }
}

const actions = {
  getEquipments ({ commit }) {
    equipmentsService.fetchEquipments()
    .then(Equipments => {
      commit('setEquipments', Equipments)
    })
  },
  getTypes ({ commit }) {
    typeEquipmentsService.fetchTypeEquipments()
    .then(types => {
      commit('setTypes', types)
    })
  },
  getLocations ({ commit }) {
    locationService.fetchLocations()
    .then(locations => {
      commit('setLocations', locations)
    })
  },
  getEquipment ({ commit }, id) {
    equipmentsService.showEquipment(id)
    .then(id => {
      commit('getEquipment', id)
    })
  },
  addEquipment({ commit }, Equipment) {
    equipmentsService.postEquipment(Equipment)
    .then(() => {
      commit('addEquipment', Equipment)
    })
  },
  updateEquipment({ commit }, payload) {
    equipmentsService.updateEquipment(payload)
    .then(() => {
      commit('addEquipment', payload)
    })
  },
  deleteEquipment( { commit }, id) {
    equipmentsService.deleteEquipment(id)
    .catch(err => state.errors = err.response.data)
    commit('deleteEquipment', id)
  }
}

const mutations = {
  setEquipments (state, equipments) {
    state.equipments = equipments
  },
  setTypes (state, types) {
    state.types = types
  },
  setLocations (state, locations) {
    state.locations = locations
  },
  getEquipment(state, id) {
    state.equipment = id
  },
  addEquipment(state, equipment) {
    state.equipments.push(equipment)
  },
  updateEquipment(state, id, payload) {
    state.equipments = state.equipments.filter(obj => obj.pk !== id)
    state.equipments.push(payload)
  },
  deleteEquipment(state, id) {
    state.equipments = state.equipments.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}