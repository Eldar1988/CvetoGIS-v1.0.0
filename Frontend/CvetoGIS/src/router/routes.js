
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
    path: '/category',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: ':slug', component: () => import('pages/CategoryDetail.vue')}
    ]
  },
  {
    path: '/reason',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: ':slug', component: () => import('pages/ReasonDetail.vue')}
    ]
  },
  {
    path: '/sort',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: ':slug', component: () => import('pages/SortDetail.vue')}
    ]
  },
  {
    path: '/product',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: ':slug', component: () => import('pages/ProductDetail')}
    ]
  },
  {
    path: '/about',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '', component: () => import('pages/About.vue')}
    ]
  },
  {
    path: '/testimonials',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '', component: () => import('pages/Testimonials.vue')}
    ]
  },
  {
    path: '/privacy_policy',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '', component: () => import('pages/PrivacyPolicy.vue')}
    ]
  },
  {
    path: '/public_offer',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '', component: () => import('pages/PublicOffer.vue')}
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
