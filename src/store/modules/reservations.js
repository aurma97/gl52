import reservationService from '../../services/reservationService'

const state = {
  reservations: [],
  reservation: [],
  errors: ''
}

const getters = {
  reservations: state => {
    return state.reservations
  }
}

const actions = {
  getReservations ({ commit }) {
    reservationService.fetchReservations()
    .then(reservations => {
      commit('setReservations', reservations)
    })
  },
  getErrors () {
    return state.errors
  },
  getReservation ({ commit }, id) {
    reservationService.showReservation(id)
    .then(id => {
      commit('getReservation', id)
    })
  },
  addReservation({ commit }, Reservation) {
    reservationService.postReservation(Reservation)
    .catch(err => state.errors = err.response.status)
    .then(() => {
      commit('addReservation', Reservation)
    })
  },
  updateReservation({ commit }, payload) {
    reservationService.updateReservation(payload)
    .catch(err => state.errors = err.response.status)
    .then(() => {
      commit('addReservation', payload)
    })
  },
  deleteReservation( { commit }, id) {
    reservationService.deleteReservation(id)
    .catch(err => state.errors = err.response.status)
    commit('deleteReservation', id)
  }
}

const mutations = {
  setReservations (state, reservations) {
    state.reservations = reservations
  },
  getReservation(state, id) {
    state.reservation = id
  },
  addReservation(state, reservation) {
    state.reservations.push(reservation)
  },
  updateReservation(state, id, payload) {
    state.reservations = state.reservations.filter(obj => obj.pk !== id)
    state.reservations.push(payload)
  },
  deleteReservation(state, id) {
    state.reservations = state.reservations.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}