import Vue from 'vue';
import VueRouter from 'vue-router';
import PingTest from '../components/PingTest.vue';
import TweetsView from '../components/TweetsView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/ping',
    name: 'PingTest',
    component: PingTest,
  },
  {
    path: '/',
    name: 'TweetsView',
    component: TweetsView,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
