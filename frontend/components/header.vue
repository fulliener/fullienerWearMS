<script setup lang="ts">
  import {BaseURL} from "~/api/repositories/auth.repository";

  const { data: user, user_pending, user_error } = await useFetch(() => `${BaseURL}/me`, {
    headers: {
      "Authorization": `Bearer ${localStorage.getItem("at")}`
    }
  });
</script>

<template>
  <header class="flex gap-5 justify-center items-center p-5 text-black bg-white shadow-sm max-md:flex-wrap">
    <div class="container flex gap-5 justify-center items-center text-black bg-white max-md:flex-wrap">
        <a href="/" class="flex-1 self-stretch my-auto text-2xl leading-9 max-md:max-w-full font-bold">FullienerWear</a>
        <nav class="flex gap-5 justify-center self-stretch my-auto text-base leading-6 bg-white">
          <a href="/catalog" class="hover:underline">каталог</a>
          <a href="/contacts" class="hover:underline">контакты</a>
        </nav>
        <div v-if="!user" class="flex gap-2 mx-2 justify-center">
            <a href="/login" class="text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-4 focus:ring-green-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">Вход</a>
            <a href="/register" class="text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Регистрация</a>
        </div>
        <a v-else href="#" class="flex gap-2 mx-5 justify-center items-center hover:underline">
            <p class="">{{ user.first_name }}</p>
            <div class="relative w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600">
                <svg class="absolute w-12 h-12 text-gray-400 -left-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path></svg>
            </div>
        </a>
    </div>
</header>
</template>

<style scoped>

</style>