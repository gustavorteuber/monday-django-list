<script>
import { mapActions } from "pinia";
import { useAuthStore } from "../login/stores/auth";
import { useDark, useToggle } from "@vueuse/core";
export default {
  setup() {
    const isDark = useDark();
    const toggle = useToggle(isDark);

    return {
      isDark,
      toggle,
    };
  },
  data() {
    return {
      user: {},
    };
  },
  methods: {
    colorBody() {
      if (this.isDark == true) {
        return "bg-neutral-900";
      } else {
        return "bg-white";
      }
    },
    colorText() {
      if (this.isDark == true) {
        return "text-sm font-medium text-transparent bg-clip-text bg-emerald-600";
      } else {
        return "text-sm font-medium";
      }
    },
    ...mapActions(useAuthStore, ["login"]),
    async submitLogin() {
      try {
        await this.login(this.user);
        this.$router.push("/home");
      } catch {
        alert("Usuário ou senha invalidos!");
      }
    },
  },
};
</script>

<template>
  <body :class="colorBody()">
    <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-lg">
        <h1
          class="text-center text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400 sm:text-3xl"
        >
          Bem-vindo ao Proative!
        </h1>
        <form action="" class="mt-6 mb-0 space-y-4 rounded-lg p-12 shadow-2xl">
          <p class="text-lg font-medium">Entre com a sua conta</p>

          <div>
            <label for="email" :class="colorText()">Nome de usuario:</label>

            <div class="relative mt-1">
              <input
                type="email"
                v-model="user.username"
                id="email"
                class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm"
                placeholder="Enter email"
              />

              <span class="absolute inset-y-0 right-4 inline-flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
                  />
                </svg>
              </span>
            </div>
          </div>

          <div>
            <label for="password" :class="colorText()">Senha:</label>

            <div class="relative mt-1">
              <input
                type="password"
                v-model="user.password"
                id="password"
                class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm"
                placeholder="Enter password"
              />

              <span class="absolute inset-y-0 right-4 inline-flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                  />
                </svg>
              </span>
            </div>
          </div>

          <button
            @click="submitLogin()"
            @keydown.enter="submitLogin()"
            type="submit"
            class="block w-full rounded-lg bg-emerald-600 px-5 py-3 text-sm font-medium text-white"
          >
            Entrar
          </button>

          <p class="text-center text-sm text-gray-500">
            Não tem uma conta?
            <a class="underline" href="/cadastro">Clique aqui</a>
          </p>
        </form>
      </div>
    </div>
  </body>
</template>

<style scoped></style>
