<script setup lang="ts">

import HeaderComponent from '@/components/header.vue';
import FooterComponent from '@/components/footer.vue';
import {BaseURL} from "~/api/repositories/good.repository";
import {useRoute} from "vue-router";
import {initFlowbite, Modal} from "flowbite";
import {onMounted} from "vue";

const { data: good, good_pending, good_error } = await useFetch(() => `${BaseURL}/${useRoute().params.id}`);

const defmodal = ref(null)

onMounted(() => {
  initFlowbite();
})

// const modal = new Modal(defmodal, {
//   closable: true,
// }, {});

</script>

<template>
<section class="flex flex-col pb-16 bg-white">
    <HeaderComponent/>

      <section class="justify-center items-center p-16 w-full text-4xl font-bold leading-10 text-center text-white bg-black bg-opacity-60 max-md:px-5 max-md:max-w-full">
        Добро пожаловать в FullienerWear
      </section>

        <div v-if="!good_pending && good" class="mt-10 px-5 md:px-10 lg:px-0 grid lg:flex justify-center lg:mt-20 lg:gap-20 flex-row justify-center">
          <div class="text-center grid justify-center lg:block">
            <div class="max-w-[300px] h-64 w-64">
                <div class="relative h-64 w-64" :style="`background-image: url('${ useRuntimeConfig().public.staticURL }${ good.image_url }');
                         background-size: cover;
                         background-position: center;`"></div>
            </div>
          </div>
          <div class="mt-5 lg:mt-0">
            <h1 class="my-2 font-bold text-xl">{{ good.name }}</h1>
            <h1 class="my-2 font-bold"><span class="font-bold text-black">Цена:</span> {{ good.price }} руб.</h1>
            <button type="button" data-modal-target="default-modal" data-modal-toggle="default-modal" class="justify-center self-center p-3 mt-6 text-base leading-6 text-white whitespace-nowrap bg-black rounded-lg max-md:px-5">Связаться с продавцом</button>
          </div>
        </div>

    <FooterComponent/>
  </section>

  <div v-if="!good_pending && good" ref="defmodal" id="default-modal" tabindex="-1" aria-hidden="true" class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
    <div class="relative p-4 w-full max-w-2xl max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t">
                <h3 class="text-xl font-semibold text-gray-900">
                    Контакты продавца
                </h3>
                <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center" data-modal-hide="default-modal">
                    <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                    </svg>
                    <span class="sr-only">Закрыть</span>
                </button>
            </div>
            <!-- Modal body -->
            <div class="p-4 md:p-5 space-y-4">
                <p class="text-base leading-relaxed text-gray-500">
                    Контакты продавца товара "{{ good.name }}"
                </p>
                <div class="flex flex-wrap gap-5">
                    <a :href="good.seller_telegram_url" target="_blank" class="text-white bg-[#1da1f2] hover:bg-[#1da1f2]/90 focus:ring-4 focus:outline-none focus:ring-[#1da1f2]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#1da1f2]/55 me-2 mb-2">
                    <svg class="w-4 h-4 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                      <path fill-rule="evenodd" d="M3 5.983C3 4.888 3.895 4 5 4h14c1.105 0 2 .888 2 1.983v8.923a1.992 1.992 0 0 1-2 1.983h-6.6l-2.867 2.7c-.955.899-2.533.228-2.533-1.08v-1.62H5c-1.105 0-2-.888-2-1.983V5.983Zm5.706 3.809a1 1 0 1 0-1.412 1.417 1 1 0 1 0 1.412-1.417Zm2.585.002a1 1 0 1 1 .003 1.414 1 1 0 0 1-.003-1.414Zm5.415-.002a1 1 0 1 0-1.412 1.417 1 1 0 1 0 1.412-1.417Z" clip-rule="evenodd"/>
                    </svg>
                    Telegram
                    </a>
                    <a :href="good.seller_vk_url" target="_blank" class="text-white bg-[#4285F4] hover:bg-[#4285F4]/90 focus:ring-4 focus:outline-none focus:ring-[#4285F4]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#4285F4]/55 me-2 mb-2">
                    <svg class="w-4 h-4 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M20 14h-2.722L11 20.278a5.511 5.511 0 0 1-.9.722H20a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1ZM9 3H4a1 1 0 0 0-1 1v13.5a3.5 3.5 0 1 0 7 0V4a1 1 0 0 0-1-1ZM6.5 18.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2ZM19.132 7.9 15.6 4.368a1 1 0 0 0-1.414 0L12 6.55v9.9l7.132-7.132a1 1 0 0 0 0-1.418Z"/>
                    </svg>
                    VK
                    </a>
                </div>
            </div>
            <!-- Modal footer -->
            <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b">
                <button data-modal-hide="default-modal" type="button" class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100">Закрыть</button>
            </div>
        </div>
    </div>
  </div>
</template>

<style scoped>

</style>