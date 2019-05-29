import locationService from '../../services/locationService'

const state = {
  locations:[],
  location:[],
  errors: ''
}

const getters = {
  equipments: state => {
    return state.locations
  }
}

const actions = {
  getErrors () {
    return state.errors
  },
  getLocations ({ commit }) {
    locationService.fetchLocations()
    .then(locations => {
      commit('setlocations', locations)
    })
  },
  getLocation({ commit }, id) {
    locationService.fetchOneLocation(id)
    .then(location => {
      commit('getLocation', location)
    })
  },
  addLocation({ commit }, location) {
    locationService.postLocation(location)
    .catch(err => state.errors = err.response.status)
    .then(() => {
      commit('addLocation', location)
    })
  },
  updateLocation({ commit }, payload) {
    locationService.updateLocation(payload)
    .catch(err => state.errors = err.response.data)
    .then(() => {
      commit('updateLocation', payload)
    })
  },
  deleteLocation( { commit }, id) {
    locationService.deleteLocation(id)
    .catch(err => state.errors = err.response.data)
    commit('deleteLocation', id)
  }
}

const mutations = {
  setlocations (state, locations) {
    state.locations = locations
  },
  getLocation(state, location) {
    state.location = location
  },
  addLocation(state, location) {
    state.locations.push(location)
  },
  updateLocation(state, id, payload) {
    state.locations = state.locations.filter(obj => obj.pk !== id)
    state.locations.push(payload)
  },
  deleteLocation(state, id) {
    state.locations = state.locations.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}