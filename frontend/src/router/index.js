import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  // customer
  {
    path: '/',
    name: 'CustomerMain',
    component: () => import('@/customers/Main.vue'),
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
        path: 'product',
        name: 'CustomerProduct',
        component: () => import('@/customers/Product.vue'),
        children: [
          {
            path: 'design',
            name: 'DesignTemplate',
            component: () => import('@/customers/Category/DesignTemplate.vue')
          },
          {
            path: 'spec',
            name: 'SpecTemplate',
            component: () => import('@/customers/Category/SpecTemplate.vue')
          },
        ]
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
      {
        path: 'carousel',
        name: 'CarouselTemplate',
        component: () => import('@/customers/ProductDetail/CarouselTemplate.vue')
      },
      {
        path: 'movingimage',
        name: 'MovingImageTemplate',
        component: () => import('@/customers/ProductDetail/MovingImageTemplate.vue')
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
        redirect: 'login',
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
                component: () => import('@/views/Contents/Main.vue'),
                redirect: 'main',
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
                    path: 'product',
                    name: 'MainProduct',
                    component: () => import('@/views/main/MainProduct.vue')
                  },

                  // {
                  //   path: ':method',
                  //   name: 'EventCreate',
                  //   component: () => import('@/views/main/EventForm.vue')
                  // },
                  // {
                  //   path: ':method/:eid',
                  //   name: 'EventUpdate',
                  //   component: () => import('@/views/main/EventForm.vue'),
                  // },
                ]
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
                      }
                    ]
                  },
                
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
    ]
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
