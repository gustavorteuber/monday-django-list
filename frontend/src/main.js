import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { createPinia } from "pinia";
import router from "./router/index";

const app = createApp(App);
createApp(App).mount("#app");
app.use(router);
app.use(createPinia());
import "./plugins/axios";
app.mount("#app");
