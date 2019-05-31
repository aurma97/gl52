import api from '@/services/api'

const config = {
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
}

export default {
  fetchReservations() {
    return api.get(`reservation/`)
              .then(response => response.data)
  },
  showReservation(id) {
    return api.get(`reservation/show/${id}`)
              .then(response => response.data)
  },
  postReservation(payload) {
    return api.post(`reservation/create`, payload)
              //.then(response => response.data)

  },
  updateReservation(payload) {
    return api.put(`reservation/update-or-delete/${payload.id}`, payload)
              .then(response => response.data)
              .catch(function (error) {
               
              })
  },
  deleteReservation(id) {
    return api.delete(`reservation/update-or-delete/${id}`)
              .then(response => { 
                
              })  
  }
}