<template>
    <main class="form-signin w-100 m-auto" data-bs-theme="dark">
        <form>
            <h1 class="h1 mb-3 fw-normal">Inicio de sesión</h1>

            <div class="form-floating">
            <input type="text" class="form-control" id="floatingInput" placeholder="Usuario">
            <label for="floatingInput">Nombre de usuario</label>
            </div>
            <div class="form-floating">
            <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
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
    import { useUserStore } from '../store/userStore.js'

    const userStore = useUserStore()
</script>