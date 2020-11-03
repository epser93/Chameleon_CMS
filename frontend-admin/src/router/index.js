import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
    redirect: '/login',
    children: [
      {
        path: 'manage',
        name: 'Manage',
        component: () => import('@/views/home/Manage.vue'),
        redirect: 'manage/user',
        children: [
          {
            path: 'user',
            name: 'User',
            component: () => import('@/views/home/User.vue')
          },
          {
            path: 'userLog',
            name: 'UserLog',
            component: () => import('@/views/home/UserLog.vue')
          }
        ]
      },
      {
        path: 'data',
        name: 'Data',
        component: () => import('@/views/home/Data.vue')
      },
      {
        path: 'contents',
        name: 'Contents',
        component: () => import('@/views/home/Contents.vue'),
        redirect: 'contents/main',
        children: [
          {
            path: 'main',
            name: 'Main',
            component: () => import('@/views/homeContent/Main.vue')
          },
          {
            path: 'product',
            name: 'Product',
            component: () => import('@/views/homeContent/Product.vue')
          },
          {
            path: 'event',
            name: 'Event',
            component: () => import('@/views/homeContent/Event.vue')
          },
          {
            path: 'notice',
            name: 'Notice',
            component: () => import('@/views/homeContent/Notice.vue')
          }
        ]
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
