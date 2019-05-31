import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import store from '@/store.js'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/risks',
      name: 'risks',
      component: () => import('../views/Risks.vue'),
      meta: {
        authRequired: true
      }
    },
    {
      path: '/risks/add',
      name: 'risk',
      component: () => import('../views/Risk.vue'),
      meta: {
        authRequired: true
      }
    },
    {
      path: '/risk-types',
      name: 'risktypes',
      component: () => import('../views/RiskTypes.vue'),
      meta: {
        authRequired: true
      }
    },
    {
      path: '/risk-types/add',
      name: 'risktypeadd',
      component: () => import('../views/RiskType.vue'),
      meta: {
        authRequired: true
      }
    },
    {
      path: '/risk-types/:id/edit',
      name: 'risktypeedit',
      component: () => import('../views/EditRiskType.vue'),
      meta: {
        authRequired: true
      }
    },
    {
      path: '/risk-types/:id/risks',
      name: 'risktyperisks',
      component: () => import('../views/Risks.vue'),
      meta: {
        authRequired: true
      }
    },
    {
      path: '/sign-in',
      name: 'signin',
      component: () => import('../views/Signin.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/Register.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.authRequired)) {
    if (!store.state.isAuthenticated) {
      next({
        path: '/sign-in'
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
