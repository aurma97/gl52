import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Messages from '@/components/Messages'
import Equipements from '@/components/equipments/Equipements'
import Reservation from '@/components/equipments/Reservation'
import Users from '@/components/Users'
import login from '@/components/accounts/Login.vue';
import register from '@/components/accounts/Register.vue';
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Index
    },
    { 
      path: '/connexion', 
      component:login
    },
    { 
      path: '/inscription', 
      component:register
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    },
    {
      path: '/equipements',
      name: 'equipements',
      component: Equipements
    },
    {
      path: '/reservation',
      name: 'reservation',
      component: Reservation
    },
    {
      path: '/users',
      name: 'users',
      component: Users
    }
  ]
})
