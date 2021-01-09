import axiosInstance from "axios";

export default {
  actions: {
    fetchMainData({commit}, slug) {
      return axiosInstance.get(`${this.getters.getServerURL}/`)
        .then(({data}) => {
          commit('setMainData', data)
        })
    },
    setCurrentCurrency({commit}, currency) {
      commit('setCurrency', currency)
    }
  },
  mutations: {
    setMainData(state, data) {
      state.categories = data.categories
      state.courses = data.courses
      state.cities = data.cities
      state.reasons = data.reasons
      state.sorts = data.sorts
      state.currentCurrency = data.courses[0]
      state.defaultCity = data.cities[0]
      state.benefits = data.benefits
      state.aboutInfo = data.about
      state.socials = data.socials
    },
    setCurrency(state, currency) {
      state.currentCurrency = currency
    }
  },
  state: {
    categories: [],
    courses: [],
    cities: [],
    reasons: [],
    sorts: [],
    currentCurrency: {},
    defaultCity: {},
    benefits: [],
    aboutInfo: {},
    socials: []
  },
  getters: {
    getCategories: (state) => state.categories,
    getCourses: (state) => state.courses,
    getCities: (state) => state.cities,
    getReasons: (state) => state.reasons,
    getSorts: (state) => state.sorts,
    getCurrentCurrency: (state) => state.currentCurrency,
    getDefaultCity: (state) => state.defaultCity,
    getBenefits: (state) => state.benefits,
    getAboutInfo: (state) => state.aboutInfo,
    getSocials: (state) => state.socials
  }
}
