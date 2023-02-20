<script>
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
  methods: {
    colorHeader() {
      if (this.isDark == true) {
        return "bg-neutral-900 top";
      } else {
        return "bg-white top";
      }
    },
    colorDetail() {
      if (this.isDark == true) {
        return "flex flex-col p-4 mt-4 text-neutral-100  md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0";
      } else {
        return "flex flex-col p-4 mt-4 text-neutral-300 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0";
      }
    },
  },
};
</script>

<template>
  <body>
    <nav :class="colorHeader()">
      <div
        class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl px-4 md:px-6 py-2.5"
      >
        <span
          class="self-center text-xl font-extrabold whitespace-nowrap text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400"
          >Proative</span
        >
        <button
          data-collapse-toggle="mega-menu-full"
          type="button"
          class="inline-flex items-center p-2 ml-1 text-sm text-neutral-500 rounded-lg md:hidden hover:bg-neutral-100 focus:outline-none focus:ring-2 focus:ring-neutral-200 :text-neutral-400 :hover:bg-neutral-700 :focus:ring-neutral-600"
          aria-controls="mega-menu-full"
          aria-expanded="false"
        >
          <span class="sr-only">Open main menu</span>
          <svg
            class="w-6 h-6"
            aria-hidden="true"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </button>
        <div
          id="mega-menu-full"
          class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1"
        >
          <ul :class="colorDetail()">
            <li>
              <a
                href="/"
                class="block py-2 pl-3 pr-4 text-neutral-700 rounded hover:bg-neutral-100 md:hover:bg-transparent md:hover:text-emerald-700 md:p-0 :text-neutral-400 md::hover:text-emerald-500 :hover:bg-neutral-700 :hover:text-emerald-500 md::hover:bg-transparent :border-neutral-700"
                aria-current="page"
                >Home</a
              >
            </li>
            <li>
              <a href="/about">
                <button
                  id="mega-menu-full-dropdown-button"
                  data-collapse-toggle="mega-menu-full-dropdown"
                  class="flex items-center justify-between w-full py-2 pl-3 pr-4 font-medium text-neutral-700 rounded md:w-auto hover:bg-neutral-100 md:hover:bg-transparent md:border-0 md:hover:text-emerald-600 md:p-0 :text-neutral-400 md::hover:text-emerald-500 :hover:bg-neutral-700 :hover:text-emerald-500 md::hover:bg-transparent :border-neutral-700"
                >
                  Sobre nós
                  <path
                    fill-rule="evenodd"
                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                    clip-rule="evenodd"
                  ></path></button
              ></a>
            </li>
            <li>
              <a
                href="#"
                class="block py-2 pl-3 pr-4 text-neutral-700 rounded hover:bg-neutral-100 md:hover:bg-transparent md:hover:text-emerald-700 md:p-0 :text-neutral-400 md::hover:text-emerald-500 :hover:bg-neutral-700 :hover:text-emerald-500 md::hover:bg-transparent :border-neutral-700"
                >Entre em contato</a
              >
            </li>
            <li>
              <button
                v-if="isDark == true"
                type="button"
                class="block py-2 pl-3 pr-4 text-neutral-700 rounded hover:bg-neutral-100 md:hover:bg-transparent md:hover:text-emerald-700 md:p-0 :text-neutral-400 md::hover:text-emerald-500 :hover:bg-neutral-700 :hover:text-emerald-500 md::hover:bg-transparent :border-neutral-700"
                @click="isDark = !isDark"
              >
                <i class="fa-regular fa-sun"></i>
              </button>
              <button
                v-if="isDark == false"
                type="button"
                class="block py-2 pl-3 pr-4 text-neutral-700 rounded hover:bg-neutral-100 md:hover:bg-transparent md:hover:text-emerald-700 md:p-0 :text-neutral-400 md::hover:text-emerald-500 :hover:bg-neutral-700 :hover:text-emerald-500 md::hover:bg-transparent :border-neutral-700"
                @click="isDark = !isDark"
              >
                <i class="fa-regular fa-moon"></i>
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </body>
</template>
<style scoped>
i {
  font-size: 16pt;
}
</style>
