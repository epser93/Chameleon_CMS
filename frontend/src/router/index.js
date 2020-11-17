import Vue from 'vue'
import VueRouter from 'vue-router'
import account from '@/store/account'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  // customer
  {
    path: '/',
    name: 'CustomerMain',
    component: () => import('@/Customer.vue'),
    redirect: '/',
    children: [
      {
        path: '',
        name: 'CustomerHome',
        component: () => import('@/customers/Home.vue'),
      },
      {
        path: 'about',
        name: 'CustomerAbout',
        component: () => import('@/customers/About.vue')
      },
      {
        path: 'category/:cid',
        name: 'CustomerCategory',
        component: () => import('@/customers/Category.vue'),
      },
      {
        path: 'product/:cid',
        name: 'CustomerProduct',
        component: () => import('@/customers/Product.vue'),
      },
      {
        path: 'event',
        name: 'CustomerEvent',
        component: () => import('@/customers/Event.vue'),
        redirect: '/event',
        children: [
          {
            path: '',
            name: 'CustomerEventMain',
            component: () => import('@/customers/Event/EventMain.vue')
          },
          {
            path: ':eid',
            name: 'CustomerEventDetail',
            component: () => import('@/customers/Event/EventDetail.vue')
          },
        ]
      },
      {
        path: 'contact',
        name: 'CustomerContact',
        component: () => import('@/customers/Contact.vue')
      },
      {
        path: 'search/:text',
        name: 'CustomerSearch',
        component: () => import('@/customers/Search.vue'),
        redirect: 'search/:text',
        children: [
          {
            path: '',
            name: 'SearchResult',
            component: () => import('@/customers/Search/SearchResult.vue')
          },
          {
            path: 'product',
            name: 'SearchProduct',
            component: () => import('@/customers/Search/SearchProduct.vue')
          },
          {
            path: 'event',
            name: 'SearchEvent',
            component: () => import('@/customers/Search/SearchEvent.vue')
          },
        ]
      },
    ]
  },
  {
    path: '/notice',
    name: 'CustomerNotice',
    component: () => import('@/customers/Notice.vue')
  },

  // admin
  {
    path: '/admin',
    name: 'admin',
    component: () => import('@/Admin.vue'),
    redirect: '/admin',
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
        redirect: '',
        beforeEnter(to, from, next) {
          if (!account.state.authToken) {
            alert('로그인이 필요합니다.')
            next({ name: 'Login'})
          } else {
            store.dispatch('account/getUserInfo')  
            setTimeout(function() {
              next()
            }, 1000)
          }
        },
        children: [
          {
            path: 'manage',
            name: 'Manage',
            component: () => import('@/views/home/Manage.vue'),
            redirect: 'manage/log',
            beforeEnter(to, from, next) {
              if (account.state.userInfo.is_superuser || account.state.userInfo.is_logger) {
                next()
              } else {
                alert('권한이 없습니다.')
              }
            },
            children: [
              {
                path: 'departments',
                name: 'Departments',
                component: () => import('@/views/Manage/Departments.vue'),
                beforeEnter(to, from, next) {
                  if (account.state.userInfo.is_superuser) {
                    next()
                  } else {
                    alert('권한이 없습니다.')
                  }
                }
              },
              {
                path: 'user',
                name: 'User',
                component: () => import('@/views/Manage/User.vue'),
                beforeEnter(to, from, next) {
                  if (account.state.userInfo.is_superuser) {
                    next()
                  } else {
                    alert('권한이 없습니다.')
                  }
                }
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
                component: () => import('@/views/Contents/Main.vue'),
                redirect: 'main',
                beforeEnter(to, from, next) {
                  if (account.state.userInfo.is_superuser || account.state.userInfo.is_marketer) {
                    next()
                  } else if (account.state.userInfo.is_producter) {
                    next({ name : 'Product'})
                  } else if (account.state.userInfo.is_eventer) {
                    next({ name : 'Event'})
                  } 
                },
                children: [
                  {
                    path: '',
                    name: 'Main',
                    component: () => import('@/views/main/Main.vue')
                  },
                  {
                    path: 'image',
                    name: 'MainImage',
                    component: () => import('@/views/main/MainImage.vue')
                  },
                  {
                    path: 'image/:method',
                    name: 'MainImageCreate',
                    component: () => import('@/views/main/MainImageForm.vue')
                  },
                  {
                    path: 'image/:method/:id',
                    name: 'MainImageUpdate',
                    component: () => import('@/views/main/MainImageForm.vue'),
                  },
                ]
              },
              {
                path: 'product',
                name: 'Product',
                component: () => import('@/views/Contents/Product.vue'),
                redirect: 'product',
                beforeEnter(to, from, next) {
                  if (account.state.userInfo.is_superuser || account.state.userInfo.is_producter) {
                    next()
                  } else {
                    alert('권한이 없습니다.')
                  }
                },
                children: [
                  {
                    path: '',
                    name: 'CategoryMain',
                    component: () => import('@/views/category/CategoryMain.vue')
                  },
                  {
                    path: 'category',
                    name: 'ProductCG',
                    component: () => import('@/views/category/CategoryInfo.vue')
                  },
                  {
                    path: 'category/:cid/:update',
                    name: 'ProductCGupdate',
                    component: () => import('@/views/category/CategoryInfo.vue')
                  },
                  {
                    path: 'category/:cid',
                    name: 'ProductItemMain',
                    component: () => import('@/views/Contents/Category.vue'),
                    redirect: 'category/:cid',
                    children: [
                      {
                        path: '',
                        name: 'ProductItem',
                        component: () => import('@/views/Item/ItemMain.vue')
                      },
                      {
                        path: 'item',
                        name: 'ProductItemCreate',
                        component: () => import('@/views/Item/ItemInfo.vue')
                      },
                      {
                        path: 'item/:pid/:update',
                        name: 'ProducItemUpdate',
                        component: () => import('@/views/Item/ItemInfo.vue')
                      },
                    ]
                  },
                ]
              },
              {
                path: 'event',
                name: 'Event',
                component: () => import('@/views/Contents/Event.vue'),
                redirect: 'event',
                beforeEnter(to, from, next) {
                  if (account.state.userInfo.is_superuser || account.state.userInfo.is_eventer) {
                    next()
                  } else {
                    alert('권한이 없습니다.')
                  }
                },
                children: [
                  {
                    path: '',
                    name: 'Event',
                    component: () => import('@/views/event/EventMain.vue')
                  },
                  {
                    path: ':method',
                    name: 'EventCreate',
                    component: () => import('@/views/event/EventForm.vue')
                  },
                  {
                    path: ':method/:eid',
                    name: 'EventUpdate',
                    component: () => import('@/views/event/EventForm.vue'),
                  },
                ]
              },
              {
                path: 'notice',
                name: 'Notice',
                component: () => import('@/views/Contents/Notice.vue'),
                redirect : 'notice',
                beforeEnter(to, from, next) {
                  if (account.state.userInfo.is_superuser || account.state.userInfo.is_marketer) {
                    next()
                  } else {
                    alert('권한이 없습니다.')
                  }
                },
                children : [
                  {
                    path: '',
                    name: 'Notice',
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
        path: 'login',
        name: 'Login',
        component: () => import('@/views/Login.vue')
      },
      {
        path: 'preview',
        name: 'Preview',
        component: () => import('@/views/Preview.vue')
      },
    ]
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

import VueAnalytics from 'vue-analytics';
Vue.use(VueAnalytics, {
    id: 'UA-183274370-1',
    router
});

export default router
