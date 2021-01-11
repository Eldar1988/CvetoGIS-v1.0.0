import Vue from 'vue'
import Vuex from 'vuex'
import main from './modules/main'
import home from './modules/home'
import productDetail from './modules/productDetail'


Vue.use(Vuex)


export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      main,
      home,
      productDetail
    },
    state: {
      // serverURL: 'http://192.168.0.155:8000',
      // serverURL: 'http://192.168.0.199:8000',
      serverURL: 'https://api.cvetogis.kz',
    },
    getters: {
      getServerURL(state) {
        return state.serverURL
      }
    },


    strict: process.env.DEBUGGING
  })

  return Store
}
