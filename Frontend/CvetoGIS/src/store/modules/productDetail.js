import axiosInstance from "axios";

export default {
  actions: {
    fetchProduct({ commit }, slug) {
      axiosInstance.get(`${this.getters.getServerURL}/product/${slug}`)
        .then(({ data }) => {
          commit('setProduct', data)
        })
    }
  },
  mutations: {
    setProduct(state, data) {
      state.product = data.product
    }
  },
  state: {
    product: {}
  },
  getters: {
    getProduct: (state) => state.product
  }
}
