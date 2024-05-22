// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr: false,
  modules: ['@nuxtjs/tailwindcss'],
  runtimeConfig: {
    public: {
      staticURL: process.env.STATIC_URL || 'http://localhost:8000/api/good/static/',
    },
  },
  tailwindcss: {
    exposeConfig: true,
    viewer: true,
    cssPath: '~/assets/css/input.css'
  }
})
