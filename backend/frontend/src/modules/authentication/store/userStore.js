import { ref, resolveComponent } from 'vue'
import { defineStore } from 'pinia'
import api from '../../../core/utils/axios'
import apiPrivate from '../../../core/utils/axiosPrivate'

export const useUserStore = defineStore(
    'userStore',
    () => {
        const user = ref({})
        const profile = ref({})
        const is_superuser = ref(false)
        const is_staff = ref(false)
        let is_authenticated = ref(false)

        async function login(username, password) {
            try {
                const data = {
                    username: username,
                    password: password
                }
                const { data: response } = await api.post('/auth/login/', data)
                is_authenticated.value = true
                user.value = response.user

                const { data: responseUsuarios } = await apiPrivate.get('auth/usuarios/' + user.value.pk + '/')
                profile.value = responseUsuarios.perfil
                is_superuser.value = responseUsuarios.is_superuser
                is_staff.value = responseUsuarios.is_staff
            } catch (error) {
                console.log(error)
            }
        }

        function logout() {
            user.value = {}
            profile.value = {}
            is_superuser.value = false
            is_staff.value = false
            is_authenticated.value = false
        }

        return {
            user,
            profile,
            is_authenticated,
            is_staff,
            is_superuser,
            login,
            logout
        }
    }
)