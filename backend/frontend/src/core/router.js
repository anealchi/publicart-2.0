import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/modules/authentication/store/userStore'
import LandPage from '@/components/LandPage.vue'
import LoginView from '@/modules/authentication/views/LoginView.vue'
import RegistroView from '@/modules/authentication/views/RegistroView.vue'
import ProfileView from '@/modules/profile/views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: 'login',
      component: LandPage,
      children: [
        {
          path: 'login',
          name: 'login',
          component: LoginView
        },
        {
          path: 'registro',
          name: 'registro',
          component: RegistroView
        }
      ]
    },
    {
      path: '/perfil',
      name: 'perfil',
      component: ProfileView
    }
  ]
})

router.beforeEach(async (to) => {
  const publicPages = ['/', '/login', '/registro']
  const authRequired = !publicPages.includes(to.path)
  const auth = useUserStore()

  if (authRequired && !auth.is_authenticated) {
    return '/'
  }
})

export default router
