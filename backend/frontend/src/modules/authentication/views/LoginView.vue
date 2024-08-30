<script setup>
  import LoginComponent from '../components/LoginComponent.vue'
</script>

<template>
  <main class="about">
    <LoginComponent/>
  </main>
</template>

<style>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
</style>
