<template>
    <main class="form-signin w-100 m-auto" data-bs-theme="dark">
        <form @submit.prevent="onSubmit">
            <h1 class="h1 mb-3 fw-normal">Inicio de sesión</h1>

            <!-- Mensaje de error -->
            <div v-if="errorMessage" class="alert alert-danger" role="alert">
                {{ errorMessage }}
            </div>

            <div class="form-floating">
            <input type="text" class="form-control" id="floatingInput" placeholder="Usuario" v-model="username">
            <label for="floatingInput">Nombre de usuario</label>
            </div>
            <div class="form-floating">
            <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password">
            <label for="floatingPassword">Password</label>
            </div>

            <div class="form-check text-start my-3">
            <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">
                Recordarme
            </label>
            </div>
            <button class="btn btn-primary w-100 py-2" type="submit">Iniciar sesión</button>
        </form>
    </main>
</template>

<script setup>
    import { ref } from 'vue';
    import { useUserStore } from '../store/userStore.js'

    const username = ref('')
    const password = ref('')
    const errorMessage = ref('')

    const userStore = useUserStore()

    async function onSubmit() {
        if (!username.value || !password.value) {
            errorMessage.value = 'Por favor, ingrese el nombre de usuario y contraseña'
            return
        }

        let response = await userStore.login(username.value, password.value)
        console.log(response)
        if (response) {
            errorMessage.value = response   
        }
    }
</script>