import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/login.vue";
import About from "../views/about.vue";
import Home from "../views/home.vue";
import homedash from "../views/homedash.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/home",
    name: "homeDash",
    component: homedash,
  },
];
const router = Router();
export default router;
function Router() {
  const router = new createRouter({
    history: createWebHistory(),
    routes,
  });
  return router;
}
