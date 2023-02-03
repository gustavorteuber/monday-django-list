import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/HomeView.vue";
import Login from "@/views/LoginView.vue";
import About from "@/views/AboutView.vue";
import Chat from "@/views/ChatView.vue";
import Perfil from "@/views/PerfilView.vue";
import Config from "@/views/ConfigView.vue";
import Status from "@/views/StatusView.vue";
import dashboard from "../views/master/dashboard";
import Calendar from "@/views/CalendarView.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    name: "Dashboard",
    path: "/home",
    component: dashboard,
    children: [
      { path: "/home", name: "Home", component: Home },
      {
        path: "/about",
        name: "About",
        component: About,
      },
      {
        path: "/chat",
        name: "Chat",
        component: Chat,
      },
      {
        path: "/config",
        name: "Config",
        component: Config,
      },
      {
        path: "/perfil",
        name: "Perfil",
        component: Perfil,
      },
      {
        path: "/status",
        name: "Status",
        component: Status,
      },
      {
        path: "/calendar",
        name: "Calendar",
        component: Calendar,
      }
    ],
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
