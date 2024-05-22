<script setup lang="ts">
import HeaderComponent from '@/components/header.vue'
import FooterComponent from '@/components/footer.vue'
import {BaseURL} from "~/api/repositories/auth.repository";

const formData = ref({
  username: "",
  first_name: "",
  last_name: "",
  email: "",
  password: "",
})

const repeat_password = ref("")

let error = ref("")

const register = async () => {
  error.value = ""

  if (formData.value.username.trim() == "") {
    error.value = "Введите корректное имя пользователя"
    return
  }
  if (formData.value.first_name.trim() == "") {
    error.value = "Введите корректное имя"
    return
  }
  if (formData.value.last_name.trim() == "") {
    error.value = "Введите корректную фамилию"
    return
  }
  if (formData.value.email.trim() == "") {
    error.value = "Введите корректную почту"
    return
  }
  if (formData.value.password.trim() == "") {
    error.value = "Введите корректный пароль"
    return
  }
  if (repeat_password.value.trim() == "") {
    error.value = "Введите корректный повторный пароль"
    return
  }
  if (repeat_password.value != formData.value.password) {
    error.value = "Пароль не совпадают"
    return
  }

  try {
    const response = await fetch(`${BaseURL}/register`, {
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
  <section class="flex flex-col pb-16 bg-white">

    <section class="flex flex-col justify-center self-stretch pt-16 text-sm font-medium leading-5 text-black">
      <div
          class="flex justify-center items-center self-center px-16 w-full max-w-[1100px] max-md:px-5 max-md:max-w-full">
        <div class="flex flex-col max-w-full w-[600px]">
          <h1 class="self-center text-4xl font-bold leading-10 text-center max-md:max-w-full mb-10">Регистрация</h1>
          <div v-if="error" class="p-4 mb-4 mt-2 text-center text-sm text-red-800 rounded-lg bg-red-50" role="alert">
          <span class="font-medium">Ошибка!</span> {{ error }}
        </div>
          <form action="/register" method="post">
            <div class="mb-3">
              <label for="username" class="block mb-2 text-sm font-medium text-gray-900">Имя пользователя</label>
              <input v-model="formData.username" type="text" id="username" name="username"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                     placeholder="Введите имя пользователя" required/>
            </div>
            <div class="mb-3">
              <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900">Имя</label>
              <input v-model="formData.first_name" type="text" id="first_name" name="first_name"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                     placeholder="Введите имя" required/>
            </div>
            <div class="mb-3">
              <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900">Фамилия</label>
              <input v-model="formData.last_name" type="text" id="last_name" name="last_name"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                     placeholder="Введите фамилию" required/>
            </div>
            <div class="mb-3">
              <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Email</label>
              <input v-model="formData.email" type="email" id="email" name="email"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                     placeholder="Введите email" required/>
            </div>
            <div class="mb-3">
              <label for="password1" class="block mb-2 text-sm font-medium text-gray-900">Пароль</label>
              <input v-model="formData.password" type="password" id="password1" name="password1"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                     placeholder="Введите пароль" required/>
            </div>
            <div class="mb-3">
              <label for="password2" class="block mb-2 text-sm font-medium text-gray-900">Повторите пароль</label>
              <input v-model="repeat_password" type="password" id="password2" name="password2"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                     placeholder="Введите пароль ещё раз" required/>
            </div>
            <button type="button" @click="register"
                    class="justify-center self-center p-3 mt-6 text-base leading-6 text-white whitespace-nowrap bg-black rounded-lg max-md:px-5">
              Зарегистрироваться
            </button>
          </form>
        </div>
      </div>
    </section>

    <FooterComponent/>
  </section>
</template>

<style scoped>

</style>