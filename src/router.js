import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Equipements from '@/components/equipments/Equipements'
import Reservation from '@/components/equipments/Reservation'
//import Users from '@/components/Users'
import login from '@/components/accounts/Login.vue';
import register from '@/components/accounts/Register.vue';
import Accounts from '@/components/accounts/Accounts.vue';
import store from '@/store' 
Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Index,
      meta: {
        requiresAuth: true
      }
    },
    { 
      path: '/connexion', 
      name: 'connexion',
      component: login
    },
    { 
      path: '/inscription',
      name: 'register', 
      component: register
    },
    { 
      path: '/mon-compte', 
      component: Accounts,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/equipements',
      name: 'equipements',
      component: Equipements,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/reservation',
      name: 'reservation',
      component: Reservation,
      meta: {
        requiresAuth: true
      }
    },
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!store.getters['authentication/isLoggedIn']) {
      next({ name: 'connexion' })
    } else {
      next() // go to wherever I'm going
    }
  } else {
    next() // does not require auth, make sure to always call next()!
  }
})

export default router;