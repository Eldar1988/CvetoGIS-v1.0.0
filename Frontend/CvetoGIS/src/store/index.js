import Vue from 'vue'
import Vuex from 'vuex'
import main from './modules/main'
import home from './modules/home'


Vue.use(Vuex)


export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      main,
      home
    },
    state: {
      serverURL: 'http://192.168.0.199:8000'
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
