import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/modules/authentication/views/LoginView.vue'
import RegistroView from '@/modules/authentication/views/RegistroView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/registro',
      name: 'registro',
      component: RegistroView
    }
  ]
})

export default router
