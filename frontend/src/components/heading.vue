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
    colorText() {
      if (this.isDark == true) {
        return "mb-4 text-3xl font-extrabold text-white md:text-5xl lg:text-6xl";
      } else {
        return "mb-4 text-3xl font-extrabold text-slate-900 md:text-5xl lg:text-6xl";
      }
    },
  },
};
</script>
<template>
  <body>
    <div class="m-20"></div>
    <div class="flex justify-center">
      <h1 :class="colorText()">
        <span
          class="text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400"
          >O Proative</span
        >
        Chegou!
      </h1>
    </div>
    <p
      class="mb-6 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 text-gray-400"
    >
      Oferecemos soluções logísticas personalizadas para empresas. Com sistemas
      avançados e equipe capacitada, garantimos eficiência e segurança nas
      entregas. Entre em contato conosco para otimizar a sua cadeia de
      suprimentos.
    </p>
  </body>
</template>
