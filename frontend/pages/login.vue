<script setup>
import HeaderComponent from '@/components/header.vue'
import FooterComponent from '@/components/footer.vue'
import {BaseURL} from "~/api/repositories/auth.repository";

const formData = ref({
  username: "",
  password: ""
})

let error = ref("")

const login = async () => {
  try {
    const response = await fetch(`${BaseURL}/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData.value)
    });

    if (response.ok) {
      const resp = await response.json()
      localStorage.setItem("at", resp.access_token)
      navigateTo("/")
    } else {
      const errorData = await response.json();
      error.value = errorData.detail;
    }
  } catch (error) {
    error.value = error;
  }
}
</script>

<template>
  <HeaderComponent/>
  <section class="flex justify-center self-stretch pt-16 text-sm font-medium leading-5 text-black">
    <div class="flex justify-center items-center px-16 w-full max-w-[1100px] max-md:px-5 w-full max-md:max-w-full">
      <div class="flex flex-col max-w-full w-[600px]">
        <h1 class="self-center text-4xl font-bold leading-10 text-center max-md:max-w-full">
          Вход
        </h1>
        <p class="self-center mt-6 text-base leading-6 text-center max-md:max-w-full mb-10">
          Пожалуйста, введите логин и пароль
        </p>
        <div v-if="error" class="p-4 mb-4 mt-2 text-center text-sm text-red-800 rounded-lg bg-red-50" role="alert">
          <span class="font-medium">Ошибка!</span> {{ error }}
        </div>
        <form method="post" action="/login">
          <div class="mb-3">
            <label for="username" class="block mb-2 text-sm font-medium text-gray-900">Имя пользователя</label>
            <input v-model="formData.username" type="text" id="username" name="username"
                   class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                   placeholder="Введите имя пользователя" required/>
          </div>
          <div class="mb-3">
            <label for="password" class="block mb-2 text-sm font-medium text-gray-900">Пароль</label>
            <input v-model="formData.password" type="password" id="password" name="password"
                   class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                   placeholder="Введите пароль" required/>
          </div>
          <button type="button" @click="login"
                  class="justify-center self-center p-3 px-7 mt-6 text-base font-medium leading-6 text-white whitespace-nowrap bg-black rounded-lg max-md:px-5">
            Войти
          </button>
        </form>
      </div>
    </div>
  </section>
  <FooterComponent/>
</template>

<style scoped>

</style>