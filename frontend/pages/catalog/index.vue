<script setup lang="ts">
import HeaderComponent from '@/components/header.vue'
import FooterComponent from '@/components/footer.vue'
import {BaseURL} from "~/api/repositories/good.repository";

const { data: goods, goods_pending, goods_error } = await useFetch(() => `${BaseURL}/`, {});
</script>

<template>
<section class="flex flex-col pb-16 bg-white">
    <HeaderComponent/>

    <section
            class="justify-center items-center p-16 w-full text-4xl font-bold leading-10 text-center text-white bg-black bg-opacity-60 max-md:px-5 max-md:max-w-full">
        Каталог FullienerWear
    </section>

    <section class="flex justify-center mt-10">
        <div class="container">
            <div class="md:flex gap-10">
                <div class="w-full">
                    <section v-if="!goods_pending && goods.length != 0" class="flex flex-col justify-center items-center px-20 py-16 w-full max-md:px-5 max-md:max-w-full">
                    <div class="justify-center py-5 mt-6 w-full max-w-[1415px] max-md:max-w-full">
                      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 max-md:flex-col max-md:gap-0">
                        <a v-for="good in goods" class="flex flex-col ml-5 max-md:ml-0 max-md:w-full" :href="`/catalog/${ good.id }`">
                          <div class="flex flex-wrap flex-col grow text-black rounded-md border border-solid border-black border-opacity-10 max-md:mt-10 max-md:max-w-full">
                            <div class="justify-center items-center px-16 pt-40 pb-32 text-xs leading-4 text-center bg-zinc-300 bg-opacity-50 max-sm:px-5 py-10 max-md:max-w-full"
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
                </div>
            </div>
        </div>
    </section>

    <FooterComponent/>
</section>
</template>

<style scoped>

</style>