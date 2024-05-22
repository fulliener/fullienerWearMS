<script setup lang="ts">
import HeaderComponent from '@/components/header.vue'
import FooterComponent from '@/components/footer.vue'
</script>

<template>

  <section class="flex flex-col pb-16 bg-white">
    <HeaderComponent/>

      <section class="justify-center items-center p-16 w-full text-4xl font-bold leading-10 text-center text-white bg-black bg-opacity-60 max-md:px-5 max-md:max-w-full">
        Наши контакты
      </section>

      <div class="mt-10 px-5 md:px-10 lg:px-0 grid lg:flex justify-center lg:mt-20 lg:gap-20 flex-row justify-center">
          <div class="text-center grid justify-center lg:block">
            <div>
                <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A283c652d3e61c43675b8a07c08f9312b96b8ccc82da5f092c0b9b09a17ced653&amp;source=constructor" class="h-[200px] w-[300px] md:h-[400px] md:w-[600px]" frameborder="0"></iframe>
            </div>
          </div>
          <div class="mt-5 lg:mt-0">
              <a href="https://web.telegram.org/a/" target="_blank" type="button" class="text-white bg-[#1da1f2] hover:bg-[#1da1f2]/90 focus:ring-4 focus:outline-none focus:ring-[#1da1f2]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#1da1f2]/55 me-2 mb-2">
              <svg class="w-4 h-4 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                <path fill-rule="evenodd" d="M3 5.983C3 4.888 3.895 4 5 4h14c1.105 0 2 .888 2 1.983v8.923a1.992 1.992 0 0 1-2 1.983h-6.6l-2.867 2.7c-.955.899-2.533.228-2.533-1.08v-1.62H5c-1.105 0-2-.888-2-1.983V5.983Zm5.706 3.809a1 1 0 1 0-1.412 1.417 1 1 0 1 0 1.412-1.417Zm2.585.002a1 1 0 1 1 .003 1.414 1 1 0 0 1-.003-1.414Zm5.415-.002a1 1 0 1 0-1.412 1.417 1 1 0 1 0 1.412-1.417Z" clip-rule="evenodd"/>
              </svg>
              Telegram
              </a>
              <br>
              <a type="button" href="https://vk.com/" target="_blank" class="text-white bg-[#4285F4] hover:bg-[#4285F4]/90 focus:ring-4 focus:outline-none focus:ring-[#4285F4]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#4285F4]/55 me-2 mb-2">
              <svg class="w-4 h-4 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                <path d="M20 14h-2.722L11 20.278a5.511 5.511 0 0 1-.9.722H20a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1ZM9 3H4a1 1 0 0 0-1 1v13.5a3.5 3.5 0 1 0 7 0V4a1 1 0 0 0-1-1ZM6.5 18.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2ZM19.132 7.9 15.6 4.368a1 1 0 0 0-1.414 0L12 6.55v9.9l7.132-7.132a1 1 0 0 0 0-1.418Z"/>
              </svg>
              VK
              </a>
              <br>
              <a href="https://avito.ru/" target="_blank" type="button" class="text-white bg-blue-200 hover:bg-[#4285F4]/90 focus:ring-4 focus:outline-none focus:ring-[#4285F4]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#4285F4]/55 me-2 mb-2">
            <svg class="w-4 h-4 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
              <path fill-rule="evenodd" d="M20 10H4v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8ZM9 13v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1Z" clip-rule="evenodd"/>
              <path d="M2 6a2 2 0 0 1 2-2h16a2 2 0 1 1 0 4H4a2 2 0 0 1-2-2Z"/>
            </svg>
            Avito
            </a>
          </div>
        </div>
    <FooterComponent/>
  </section>

</template>

<style scoped>

</style>