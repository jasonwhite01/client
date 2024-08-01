import { createApp } from 'vue'
// import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'

createApp(App).use(router).mount('#app')

// Vue.config. = false

// new Vue({
//   router, // we tell our vue instance to use this vue router
//   render: h => h(App),
// }).$mount('#app')