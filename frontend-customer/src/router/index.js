import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: () => import('@/views/Main.vue'),
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
      },
      {
        path: '/about',
        name: 'About',
        component: () => import('@/views/About.vue')
      },
      {
        path: '/product',
        name: 'Product',
        component: () => import('@/views/Product.vue'),
        children: [
          {
            path: 'design',
            name: 'DesignTemplate',
            component: () => import('@/views/Category/DesignTemplate.vue')
          },
          {
            path: 'spec',
            name: 'SpecTemplate',
            component: () => import('@/views/Category/SpecTemplate.vue')
          },
        ]
      },
      {
        path: '/event',
        name: 'Event',
        component: () => import('@/views/Event.vue'),
        redirect: '/event',
        children: [
          {
            path: '',
            name: 'EventMain',
            component: () => import('@/views/Event/EventMain.vue')
          },
          {
            path: ':eid',
            name: 'EventDetail',
            component: () => import('@/views/Event/EventDetail.vue')
          },
        ]
      },
      {
        path: '/contact',
        name: 'Contact',
        component: () => import('@/views/Contact.vue')
      },
      {
        path: '/search/:text',
        name: 'Search',
        component: () => import('@/views/Search.vue')
      },
      {
        path: 'carousel',
        name: 'CarouselTemplate',
        component: () => import('@/views/ProductDetail/CarouselTemplate.vue')
      },
      {
        path: 'movingimage',
        name: 'MovingImageTemplate',
        component: () => import('@/views/ProductDetail/MovingImageTemplate.vue')
      },
    ]
  },
  {
    path: '/notice',
    name: 'Notice',
    component: () => import('@/views/Notice.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
