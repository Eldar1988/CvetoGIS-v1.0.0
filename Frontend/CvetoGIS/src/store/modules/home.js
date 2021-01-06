import axiosInstance from "axios";

export default {
  actions: {
    fetchHomeData({ commit }, slug) {
      if (slug !== undefined) {
        return axiosInstance.get(`${this.state.serverURL}/home/${slug}`).then(({ data }) => {
          commit('setHomeData', data)
        })
      } else {
        return axiosInstance.get(`${this.state.serverURL}/home`).then(({ data }) => {
          commit('setHomeData', data)
        })
      }
    }
  },
  mutations: {
    setHomeData(state, data) {
      state.HomeInfo = data.homePageInfo
      state.slides = data.slides
    }
  },
  state: {
    HomeInfo: {},
    slides: []
  },
  getters: {
    getHomeInfo: (state) => state.HomeInfo,
    getSlides: (state) => state.slides
  }
}
