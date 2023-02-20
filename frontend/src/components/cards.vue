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
    special() {
      if (this.isDark == true) {
        return "inline-flex items-center px-3 py-2 text-sm font-bold text-center text-neutral-900 rounded-lg bg-gradient-to-r to-emerald-600 from-sky-400";
      } else {
        return "inline-flex items-center px-3 py-2 text-sm font-bold text-center text-white rounded-lg bg-gradient-to-r to-emerald-600 from-sky-400";
      }
    },

    colorCard() {
      if (this.isDark == true) {
        return "max-w-sm border border-emerald-500 rounded-lg shadow bg-neutral-800 m-5 flex flex-col sm:flex-row h-auto w-full";
      } else {
        return "max-w-sm border border-emerald-500 rounded-lg shadow bg-white m-5 flex flex-col sm:flex-row h-auto w-full ";
      }
    },
    ColorTitle() {
      if (this.isDark == true) {
        return "mb-2 text-2xl font-bold tracking-tight text-emerald-500";
      } else {
        return "mb-2 text-2xl font-bold tracking-tight text-emerald-500";
      }
    },
    ColorSubtitle() {
      if (this.isDark == true) {
        return "mb-3 font-normal text-gray-400";
      } else {
        return "mb-3 font-normal text-gray-700";
      }
    },
    ColorButton() {
      if (this.isDark == true) {
        return "inline-flex items-center px-3 py-2 text-sm font-bold text-center text-neutral-900 bg-emerald-600 rounded-lg hover:bg-emerald-800 focus:ring-4 ";
      } else {
        return "inline-flex items-center px-3 py-2 text-sm font-bold text-center text-white border border-emerald-500 bg-emerald-600  rounded-lg hover:bg-emerald-800  focus:ring-4";
      }
    },
  },
};
</script>
<template>
  <div :class="colorCard()">
    <a href="#"> </a>
  </div>
  <div class="flex justify-center mt-20">
    <div :class="colorCard()">
      <a href="#"> </a>
      <div class="p-5">
        <a href="/login">
          <h5 :class="ColorTitle()">Plano Free</h5>
        </a>
        <p :class="ColorSubtitle()">
          Aqui temos o Plano Free, no qual apresentamos uma demonstração da
          plataforma com limitações de uso.
        </p>
        <RouterLink to="/login" :class="ColorButton()">
          Conheça mais!
          <svg
            aria-hidden="true"
            class="w-4 h-4 ml-2 -mr-1"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </RouterLink>
      </div>
    </div>
    <div :class="colorCard()">
      <a href="#"> </a>
      <div class="p-5">
        <a href="/login">
          <h5 :class="ColorTitle()">Plano Pro</h5>
        </a>
        <p :class="ColorSubtitle()">
          Aqui temos o Plano Pro, no qual é perfeito para quem está iniciando no
          gerenciamento empresarial.
        </p>
        <a href="#" :class="ColorButton()">
          Conheça mais!
          <svg
            aria-hidden="true"
            class="w-4 h-4 ml-2 -mr-1"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </a>
      </div>
    </div>
    <div :class="colorCard()">
      <a href="#"> </a>
      <div class="p-5">
        <a href="login">
          <h5 :class="ColorTitle()">Plano Premium</h5>
        </a>
        <p :class="ColorSubtitle()">
          Aqui temos o Plano Premium, no qual está desbloqueado todas as
          funcionalidades e tudo o que o Proative tem a oferecer.
        </p>
        <a href="/login" :class="special()">
          Conheça mais!
          <svg
            aria-hidden="true"
            class="w-4 h-4 ml-2 -mr-1"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </a>
      </div>
    </div>
  </div>
</template>

<style></style>
