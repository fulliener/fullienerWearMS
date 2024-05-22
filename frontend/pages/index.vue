<script setup lang="ts">
import HeaderComponent from '@/components/header.vue'
import FooterComponent from '@/components/footer.vue'
import {BaseURL} from "~/api/repositories/good.repository";

const { data: goods, goods_pending, goods_error } = await useFetch(() => `${BaseURL}/`, {});
</script>

<template>
  <HeaderComponent/>

  <section class="justify-center items-center p-16 w-full text-4xl font-bold leading-10 text-center text-white bg-black bg-opacity-60 max-md:px-5 max-md:max-w-full">
    Добро пожаловать в FullienerWear
  </section>
  <section class="flex justify-center items-center p-16 w-full text-xs leading-4 text-center text-black max-md:px-5 max-md:max-w-full">
    <div class="flex flex-col justify-center items-center w-full rounded-xl bg-zinc-300 bg-opacity-50 h-[250px] md:h-[450px] max-h-[450px] max-w-[1415px] max-md:px-5 max-md:max-w-full"
         style="background-image: url('/banner.png'); background-position: center; background-repeat: no-repeat">
        <div class="w-full h-full flex justify-center rounded-xl  items-center bg-black/30">
            <p class="text-4xl text-white font-bold">ТОЛЬКО УНИКАЛЬНЫЙ ТОВАР</p>
        </div>
    </div>
  </section>
  <section  v-if="!goods_pending && goods.length != 0" class="flex flex-col justify-center items-center px-20 py-16 w-full max-md:px-5 max-md:max-w-full">
    <h2 class="text-4xl font-bold leading-10 text-center text-black max-md:max-w-full">Новинки</h2>
    <div class="justify-center py-5 mt-6 w-full max-w-[1415px] max-md:max-w-full">
      <div class="flex gap-5 max-md:flex-col max-md:gap-0">
        <a v-for="good in goods.slice(0, 3)" class="flex flex-col ml-5 w-[33%] max-md:ml-0 max-md:w-full" :href="`/catalog/${ good.id }`">
          <div class="flex flex-col grow text-black rounded-md border border-solid border-black border-opacity-10 max-md:mt-10 max-md:max-w-full">
            <div class="justify-center items-center px-16 pt-40 pb-32 text-xs leading-4 text-center bg-zinc-300 bg-opacity-50 max-md:px-5 py-10 max-md:max-w-full"
                 :style="`background-image: url('${ useRuntimeConfig().public.staticURL }${ good.image_url }');
                         background-size: cover;
                         background-position: center;`"></div>
            <div class="flex flex-col p-3 max-md:max-w-full">
              <h3 class="text-base leading-6 max-md:max-w-full">{{ good.name }}</h3>
              <div class="mt-1 text-xl font-medium leading-7 max-md:max-w-full">{{ good.price }} руб.</div>
            </div>
          </div>
        </a>
      </div>
    </div>
  </section>
  <section v-if="!goods_pending && goods.length >= 5" class="flex justify-center items-center p-16 w-full max-md:px-5 max-md:max-w-full">
    <div class="w-full max-w-[1415px] max-md:max-w-full">
      <div class="flex gap-5 max-md:flex-col max-md:gap-0">
        <div class="flex flex-col w-6/12 max-md:ml-0 max-md:w-full">
          <h2 class="self-stretch my-auto text-4xl font-bold leading-10 text-black max-md:mt-10 max-md:max-w-full">Хиты продаж</h2>
        </div>
        <div class="flex flex-col ml-5 w-6/12 max-md:ml-0 max-md:w-full">
          <div class="grow justify-center max-md:mt-10 max-md:max-w-full">
            <div class="flex gap-5 max-md:flex-col max-md:gap-0">
              <a v-for="good in goods.slice(3, 5)" class="flex flex-col w-6/12 max-md:ml-0 max-md:w-full" :href="`/catalog/${ good.id }`">
                <div class="flex flex-col grow text-black rounded-md border border-solid border-black border-opacity-10 max-md:mt-10">
                <div class="justify-center items-center px-16 pt-40 pb-32 text-xs leading-4 text-center bg-zinc-300 bg-opacity-50 max-md:px-5 py-10 max-md:max-w-full"
                 :style="`background-image: url('${ useRuntimeConfig().public.staticURL }${ good.image_url }');
                         background-size: cover;
                         background-position: center;`"></div>
                  <div class="flex flex-col p-3">
                    <h3 class="text-base leading-6">{{ good.name }}</h3>
                    <div class="mt-1 text-xl font-medium leading-7">{{ good.price }} руб.</div>
                  </div>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section v-if="!goods_pending && goods.length >= 7" class="flex justify-center items-center p-16 w-full max-md:px-5 max-md:max-w-full">
    <div class="w-full max-w-[1415px] max-md:max-w-full">
      <div class="flex gap-5 max-md:flex-col max-md:gap-0">
        <div class="flex flex-col w-6/12 max-md:ml-0 max-md:w-full">
          <h2 class="self-stretch my-auto text-4xl font-bold leading-10 text-black max-md:mt-10 max-md:max-w-full">Распродажа</h2>
        </div>
        <div class="flex flex-col ml-5 w-6/12 max-md:ml-0 max-md:w-full">
          <div class="grow justify-center max-md:mt-10 max-md:max-w-full">
            <div class="flex gap-5 max-md:flex-col max-md:gap-0">
              <a v-for="good in goods.slice(5, 7)" class="flex flex-col w-6/12 max-md:ml-0 max-md:w-full" :href="`/catalog/${ good.id }`">
                <div class="flex flex-col grow text-black rounded-md border border-solid border-black border-opacity-10 max-md:mt-10">
                <div class="justify-center items-center px-16 pt-40 pb-32 text-xs leading-4 text-center bg-zinc-300 bg-opacity-50 max-md:px-5 py-10 max-md:max-w-full"
                 :style="`background-image: url('${ useRuntimeConfig().public.staticURL }${ good.image_url }');
                         background-size: cover;
                         background-position: center;`"></div>
                  <div class="flex flex-col p-3">
                    <h3 class="text-base leading-6">{{ good.name }}</h3>
                    <div class="mt-1 text-xl font-medium leading-7">{{ good.price }} руб.</div>
                  </div>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <FooterComponent/>
</template>

<style scoped>

</style>