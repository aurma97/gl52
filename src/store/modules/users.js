import usersService from '../../services/usersServices'


const state = {
  users: [],
  user: [],
  errors: ''
}

const getters = {
  users: state => {
    return state.users
  }
}

const actions = {
  getUsers ({ commit }) {
    usersService.fetchUsers()
      .then(users => {
        console.log("users:",users);
        commit('getUsers', users)
      })
  },
  getUser ({ commit } , id) {
    usersService.showUser(id)
      .then(id => {
        commit('getUser', id)
      })
  },
  deleteUser( { commit }, id) {
    usersService.deleteUser(id)
    .catch(err => state.errors = err.response.data)
    commit('deleteUser', id)
  },
  addUser({ commit }, user) {
    console.log('user:',user)
    usersService.postUser(user)
      .catch(err => state.errors = err.response.data)
      .then(() => {
        commit('addUser', user)
      })
  },
  updateUser({ commit }, payload) {
    usersService.updateUser(payload)
      .catch(err => state.errors = err.response.data)
      .then(() => {
        commit('updateUser',payload)
      })
  },
  getErrors() {
    return state.errors
  }
}

const mutations = {
  getUsers(state, users) {
    state.users = users
  },
  getUser(state, id) {
    state.user = id
  },
  updateUser(state, payload) {
    let id = payload.id;
    state.users = state.users.filter(obj => obj.pk !== id)
    state.users.push(payload)
  },
  addUser(state, user) {
    state.users.push(user)
  },
  deleteUser(state, id) {
    state.users = state.users.filter(obj => obj.pk !== id)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}