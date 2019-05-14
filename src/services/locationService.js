import api from '@/services/api'

export default {
  fetchLocations() {
    return api.get(`location/`)
              .then(response => response.data)
  },
  fetchOneLocation(id) {
    return api.get(`location/show/${id}`)
              .then(response => response.data)
  },
  postLocation(payload) {
    return api.post(`location/`, payload)
              .then(response => response.data)
  },
  updateLocation(payload) {
    return api.put(`location/update-or-delete/${payload.id}`, payload)
              .then(response => response.data)
  },
  deleteLocation(id) {
    return api.delete(`location/update-or-delete/${id}`)
              .then(response => response.data)
  }
}