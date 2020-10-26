import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
    redirect: '/main',
    children: [
      {
        path: 'main',
        name: 'Main',
        component: () => import('@/views/home/Main.vue'),
      },
      {
        path: 'manage',
        name: 'Manage',
        component: () => import('@/views/home/Manage.vue')
      },
      {
        path: 'data',
        name: 'Data',
        component: () => import('@/views/home/Data.vue')
      },
      {
        path: 'contents',
        name: 'Contents',
        component: () => import('@/views/home/Contents.vue')
      },
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
