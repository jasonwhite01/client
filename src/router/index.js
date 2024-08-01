// import Vue from 'vue';
// import Router from 'vue-router';
import { createWebHistory, createRouter } from "vue-router";
import Ping from '../components/Ping.vue';
import Home from '../components/Home.vue';
import NewsFeed from "@/components/NewsFeed.vue";

// Vue.use(Router);

const routes = [
    {
        path:'/',
            name: 'Home',
            component: Home,
    },
    {
        path:'/ping',
            name: 'Ping',
            component: Ping,
    },
    {
        path:'/feeds',
            name: 'Feeds',
            component: NewsFeed,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
export default router;
