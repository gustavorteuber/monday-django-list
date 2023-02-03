import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/index";
import { createPinia } from "pinia";
import "./assets/app.css";
import Vue from 'vue'
import CalendarView from '../src/views/CalendarView.vue'

const app = createApp(App);
app.use(router);
app.mount("#app");
app.use(createPinia());
import "./plugins/axios";

Vue.config.productionTip = false

new Vue({
  render: h => h(CalendarView),
}).$mount('#single-date-picker')

