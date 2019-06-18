import typeEquipmentsService from '../../services/typeEquipmentsService'

const state = {
  types:[],
  type:[],
  errors: ''
}

const getters = {
  equipments: state => {
    return state.types
  }
}

const actions = {
  getErrors () {
    return state.errors
  },
  getTypes ({ commit }) {
    typeEquipmentsService.fetchTypeEquipments()
    .then(types => {
      commit('setTypes', types)
    })
  },
  getType ({ commit }, id) {
    typeEquipmentsService.fetchOneTypeEquipment(id)
    .then(type => {
      commit('getType', type)
    })
  },
  addType({ commit }, type) {
    typeEquipmentsService.postTypeEquipment(type)
    .catch(err =>console.log(err))
    .then(() => {
      commit('addType', type)
    })
  },
  updateType({ commit }, payload) {
    typeEquipmentsService.updateTypeEquipment(payload)
    .catch(err => state.errors = err.response.data)
    .then(() => {
      commit('updateType', payload)
    })
  },
  deleteType( { commit }, id) {
    typeEquipmentsService.deleteTypeEquipment(id)
    .catch(err => state.errors = err.response.data)
    commit('deleteType', id)
  }
}

const mutations = {
  setTypes (state, types) {
    state.types = types
  },
  getType(state, type) {
    state.type = type
  },
  addType(state, type) {
    state.types.push(type)
  },
  updateType(state, id, payload) {
    state.types = state.types.filter(obj => obj.pk !== id)
    state.types.push(payload)
  },
  deleteType(state, id) {
    state.types = state.types.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}