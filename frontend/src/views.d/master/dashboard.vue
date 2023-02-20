<script>
import { mapState } from "pinia";
import { useAuthStore } from "@/stores/auth";
import axios from "axios";
export default {
  data() {
    return {
      showDropDown: false,
      showSide: true,
      user: {},
      superuser: "",
    };
  },
  async created() {
    const res = await axios.get(`http://localhost:8000/usuario/${this.id}/`);
    this.user = res.data;
    console.log(this.user);
  },
  methods: {
    // hide show side bar
    toggleSideBar() {
      this.showSide = !this.showSide;
    },
    // toggle user
    toggleDrop() {
      this.showDropDown = !this.showDropDown;
    },
  },
  computed: {
    ...mapState(useAuthStore, [
      "id",
      "is_superuser",
      "username",
      "email",
      "foto",
    ]),
  },
};
</script>

<template>
  <div class="w-screen h-screen flex">
    <!-- Side bar -->
    <div
      class="w-[400px] h-full bg-amber-300 text-violet-600"
      v-show="showSide"
    >
      <div class="h-[50px] bg-gray-100 flex justify-start items-center">
        <div class="px-[20px]">
          <h3 class="font-bold text-xl">proative.com</h3>
        </div>
      </div>
      <div class="h-[calc(100vh-50px)] bg-gray-100 py-[20px]">
        <div
          class="flex flex-col justify-between h-full px-[20px] space-y-[10px]"
        >
          <div class="flex flex-col justify-between space-y-[10px]">
            <router-link
              to="/home"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-violet-800 hover:bg-violet-300 hover:text-violet-900 transition duration-400 ease-in-out"
            >
              <svg
                aria-hidden="true"
                class="mr-2 w-[25px] h-[25px] fill-current"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              Home
            </router-link>
            <router-link
              to="/notification"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-violet-800 hover:bg-violet-300 hover:text-violet-900 transition duration-400 ease-in-out"
            >
              <svg
                aria-hidden="true"
                class="mr-2 w-[25px] h-[25px] fill-current"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z"
                ></path>
              </svg>
              Perfil
            </router-link>
            <router-link
              to="/chat"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-violet-800 hover:bg-violet-300 hover:text-violet-900 transition duration-400 ease-in-out"
            >
              <svg
                aria-hidden="true"
                class="mr-2 w-[25px] h-[25px] fill-current"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              Chat
            </router-link>
            <router-link
              to="/calendar"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-violet-800 hover:bg-violet-300 hover:text-violet-900 transition duration-400 ease-in-out"
            >
              <svg
                aria-hidden="true"
                class="mr-2 w-[25px] h-[25px] fill-current"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M2 9.5A3.5 3.5 0 005.5 13H9v2.586l-1.293-1.293a1 1 0 00-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 15.586V13h2.5a4.5 4.5 0 10-.616-8.958 4.002 4.002 0 10-7.753 1.977A3.5 3.5 0 002 9.5zm9 3.5H9V8a1 1 0 012 0v5z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              Calendar
            </router-link>
          </div>
          <div class="h-[50px]">
            <div class="flex items-center">
              <div
                class="flex items-center justify-start space-x-4"
                @click="toggleDrop"
              >
                <img
                  v-if="user.foto != null"
                  :src="user.foto.url"
                  class="w-10 h-10 rounded-full"
                  alt=""
                />
                <img
                  v-if="user.foto == null"
                  src="@/assets/semfoto.png"
                  class="w-10 h-10 rounded-full"
                  alt="teste"
                />
              </div>
              <div class="flex flex-col pl-3">
                <div class="text-sm text-violet-500">{{ username }}</div>
                <span class="text-xs text-[#acacb0] font-light tracking-tight">
                  {{ email }}
                </span>
              </div>
              <button
                class="text-gray-400 bg-gray-700 rounded focus:outline-none focus:ring-1 focus:ring-gray-500 focus:text-white"
              ></button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full h-full bg-a-400">
      <div
        class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-indigo-800 hover:text-indigo-900 transition duration-400 ease-in-out"
      >
        <!-- Hambuger menu -->
        <div class="cursor-pointer w-[30px]" @click="toggleSideBar">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 448 512"
            class="w-[25px] h-[25px]"
          >
            <!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
            <path
              d="M0 96C0 78.3 14.3 64 32 64H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 128 0 113.7 0 96zM0 256c0-17.7 14.3-32 32-32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zM448 416c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H416c17.7 0 32 14.3 32 32z"
            />
          </svg>
        </div>
        <!-- Search bar -->

        <div class="w-[calc(100%-30px)] flex">
          <div class="w-[calc(100%-200px)] flex justify-center">
            <!-- Search bar -->
            <form class="flex items-center w-[500px]">
              <label class="sr-only">Search</label>
              <div class="relative w-full">
                <input
                  type="text"
                  class="bg-gray-100 border border-violet-600 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Pesquisar"
                  required
                />
                <router-link
                  to="/"
                  class="flex absolute inset-y-0 right-0 items-center pr-3"
                >
                </router-link>
              </div>
            </form>
          </div>
          <!-- User login -->
          <div class="w-[200px]">
            <div
              class="flex items-center justify-start space-x-4"
              @click="toggleDrop"
            >
              <img
                v-if="user.foto != null"
                :src="user.foto.url"
                class="w-10 h-10 rounded-full border-2 border-gray-50"
                alt=""
              />
              <img
                v-if="user.foto == null"
                src="@/assets/semfoto.png"
                class="w-10 h-10 rounded-full border-2 border-gray-50"
                alt="teste"
              />
              <div class="font-semibold dark:text-violet-400 text-left">
                <div>{{ username }}</div>
                <div class="text-xs text-violet-500 dark:text-gray-400">
                  <div class="designation" v-if="is_superuser == true">
                    Admin
                  </div>
                  <div class="designation" v-if="is_superuser == false">
                    Usuario
                  </div>
                </div>
              </div>
            </div>
            <!-- Drop down -->
            <div
              v-show="showDropDown"
              class="absolute right-[10px] z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
              role="menu"
              aria-orientation="vertical"
              aria-labelledby="menu-button"
              tabindex="-1"
            >
              <div class="py-1 text-left" role="none">
                <!-- Active: "bg-gray-100 text-gray-900", Not Active: "text-gray-700" -->
                <a
                  href="/config"
                  class="text-gray-700 block px-4 py-2 text-sm"
                  role="menuitem"
                  tabindex="-1"
                  id="menu-item-0"
                  >Configurações da conta</a
                >
                <a
                  href="#"
                  class="text-gray-700 block px-4 py-2 text-sm"
                  role="menuitem"
                  tabindex="-1"
                  id="menu-item-2"
                  >Sobre nós</a
                >
                <a
                  href="/"
                  class="text-eg-700 block px-4 py-2 text-sm"
                  role="menuitem"
                  tabindex="-1"
                  id="menu-item-2"
                  >Sair</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="h-[calc(100vh-50px)] bg-gray-50 p-[20px]">
        <div class="border border-gray-300 rounded-md p-[20px] h-full">
          <router-view></router-view>
        </div>
      </div>
    </div>
    <!-- Main  -->
  </div>
</template>

<style></style>
