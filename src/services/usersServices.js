import api from '@/services/api'

export default  {
  fetchUsers() {
    return api.get(`employee/`)
              .then(response => response.data)
  },
  showUser(id) {
    return api.get(`employee/${id}`)
              .then(response => response.data)
  },
  updateUser(payload) {
    return api.put(`employee/${payload.id}`, payload)
              .then(response => response.data)
              .catch(function (error) {
                })
  },
  deleteUser(id) {
    return api.delete(`employee/${id}`)
              .then(response => { 
              })  
  },
  postUser(payload) {
    return api.post(`employee/`, payload)
              .then(response => response.data)

  }
}