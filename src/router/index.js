// import Vue from 'vue';
// import Router from 'vue-router';
import { createWebHistory, createRouter } from "vue-router";
import NewsFeed from "@/components/NewsFeed.vue";
import SavedNewsFeeds from "@/components/SavedNewsFeeds.vue";

// Vue.use(Router);

const routes = [
    {
        path:'/feeds',
            name: 'Feeds',
            component: NewsFeed,
    },
    {
        path:'/feeds/savedfeeds',
            name: "Saved Feeds",
            component: SavedNewsFeeds,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
export default router;
