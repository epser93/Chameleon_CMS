import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
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
    component: () => import('@/views/Product.vue')
  },
  {
    path: '/event',
    name: 'Event',
    component: () => import('@/views/Event.vue')
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
    path: '/template/design',
    name: 'DesignTemplate',
    component: () => import('@/views/Category/DesignTemplate.vue')
  },
  {
    path: '/design/spec',
    name: 'SpecTemplate',
    component: () => import('@/views/Category/SpecTemplate.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
