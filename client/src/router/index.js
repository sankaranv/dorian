import Vue from 'vue';
import VueRouter from 'vue-router';
import PingTest from '../components/PingTest.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/ping',
    name: 'PingTest',
    component: PingTest,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
