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
            component: () => import('@/views/Manage/User.vue')
          },
          {
            path: 'log',
            name: 'Log',
            component: () => import('@/views/Manage/Log.vue')
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
            component: () => import('@/views/Contents/Main.vue')
          },
          {
            path: 'product',
            name: 'CategoryMain',
            component: () => import('@/views/Contents/Product.vue'),
            redirect: 'product',
            children: [
              {
                path: '',
                name: 'Product',
                component: () => import('@/views/category/CategoryMain.vue')
              },
              {
                path: 'category',
                name: 'Category',
                component: () => import('@/views/category/CategoryInfo.vue')
              },
              {
                path: 'category/:cid/:update',
                name: 'CGupdate',
                component: () => import('@/views/category/CategoryInfo.vue')
              },
              {
                path: 'category/:cid',
                name: 'ItemMain',
                component: () => import('@/views/Item/ItemMain.vue')
              },
              {
                path: 'item',
                name: 'Item',
                component: () => import('@/views/Item/ItemInfo.vue')
              }
            ]
          },
          {
            path: 'event',
            name: 'Event',
            component: () => import('@/views/Contents/Event.vue'),
            redirect: 'event',
            children: [
              {
                path: '',
                name: 'EventMain',
                component: () => import('@/views/event/EventMain.vue')
              },
              {
                path: 'form',
                name: 'EventForm',
                component: () => import('@/views/event/EventForm.vue')
              },
            ]
          },
          {
            path: 'notice',
            name: 'Notice',
            component: () => import('@/views/Contents/Notice.vue'),
            redirect : 'notice',
            children : [
              {
                path: '',
                name: 'NoticeMain',
                component : () => import('@/views/notice/NoticeMain.vue')
              },
              {
                path: 'form',
                name: 'NoticeForm',
                component: () => import('@/views/notice/NoticeForm.vue')
              },
              {
                path: 'form/:id',
                name: 'NoticeUpdate',
                props: true,
                component: () => import('@/views/notice/NoticeForm.vue')
              },
              {
                path: ':id',
                name: 'NoticeDetail',
                component: () => import('@/views/notice/NoticeDetail')
              }
            ]
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
