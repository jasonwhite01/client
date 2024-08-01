// import Vue from 'vue';
// import Router from 'vue-router';
import { createWebHistory, createRouter } from "vue-router";
import NewsFeed from "@/components/NewsFeed.vue";

// Vue.use(Router);

const routes = [
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
