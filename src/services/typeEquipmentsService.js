import api from '@/services/api'

export default {
  fetchTypeEquipments() {
    return api.get(`type-of-equipments/`)
              .then(response => response.data)
  },
  fetchOneTypeEquipment() {
    return api.get(`type-of-equipments/show/${msgId}`)
              .then(response => response.data)
  },
  postTypeEquipment(payload) {
    return api.post(`type-of-equipments/`, payload)
              .then(response => response.data)
  },
  updateTypeEquipment(msgId) {
    return api.delete(`type-of-equipments/update-or-delete/${msgId}`, payload)
              .then(response => response.data)
  },
  deleteTypeEquipment(msgId) {
    return api.delete(`type-of-equipments/update-or-delete/${msgId}`)
              .then(response => response.data)
  }
}