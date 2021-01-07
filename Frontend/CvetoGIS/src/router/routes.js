
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'city/:slug', params: 'slug', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/cart',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Cart.vue') },
    ]
  },
  {
    path: '/shop',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: ':slug', component: () => import('pages/CategoryDetail')}
    ]
  },
  {
    path: '/product',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: ':slug', component: () => import('pages/ProductDetail')}
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
