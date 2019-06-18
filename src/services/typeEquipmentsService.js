import api from '@/services/api'

export default {
  fetchTypeEquipments() {
    return api.get(`type-of-equipments/`)
              .then(response => response.data)
  },
  fetchOneTypeEquipment(id) {
    return api.get(`type-of-equipments/show/${id}`)
              .then(response => response.data)
  },
  postTypeEquipment(payload) {
    return api.post(`type-of-equipments/`, payload)
              .then(response => response.data)
              .catch(error => error.response)
  },
  updateTypeEquipment(payload) {
    return api.put(`type-of-equipments/update-or-delete/${payload.id}`, payload)
              .then(response => response.data)
              .catch(error => error.response)
  },
  deleteTypeEquipment(id) {
    return api.delete(`type-of-equipments/update-or-delete/${id}`)
              .then(response => response.data)
              .catch(error => error.response)
  }
}