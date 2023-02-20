<script>
import { useDark, useToggle } from "@vueuse/core";
import heading from "../components/heading.vue";
import footerinfo from "../components/footer.vue";
import cardsinfo from "../components/cards.vue";
import headerinfo from "../components/header.vue";
export default {
  components: { headerinfo, heading, footerinfo, cardsinfo },
  setup() {
    const isDark = useDark();
    const toggle = useToggle(isDark);

    return {
      isDark,
      toggle,
    };
  },
  data() {
    return {};
  },
  methods: {
    colorBody() {
      if (this.isDark == true) {
        return "bg-neutral-900";
      } else {
        return "bg-white";
      }
    },
  },
};
</script>

<template>
  <button
    v-if="isDark == true"
    type="button"
    class="block py-2 pl-3 pr-4 text-neutral-700 rounded hover:bg-neutral-100 md:hover:bg-transparent md:hover:text-emerald-700 md:p-0 :text-neutral-400 md::hover:text-emerald-500 :hover:bg-neutral-700 :hover:text-emerald-500 md::hover:bg-transparent :border-neutral-700"
    @click="isDark = !isDark"
  ></button>
  <button
    v-if="isDark == false"
    type="button"
    class="block py-2 pl-3 pr-4 text-neutral-700 rounded hover:bg-neutral-100 md:hover:bg-transparent md:hover:text-emerald-700 md:p-0 :text-neutral-400 md::hover:text-emerald-500 :hover:bg-neutral-700 :hover:text-emerald-500 md::hover:bg-transparent :border-neutral-700"
    @click="isDark = !isDark"
  ></button>
  <body :class="colorBody()">
    <headerinfo></headerinfo>
    <heading></heading>
    <cardsinfo></cardsinfo>
    <footerinfo></footerinfo>
  </body>
</template>
