<script>
import { mapState } from "pinia";
import { useAuthStore } from "@/stores/auth";
import dayjs from "dayjs";
// import locale_pt_br from "dayjs/locale/pt-br";
import relativeTime from "dayjs/plugin/relativeTime";

dayjs.extend(relativeTime);

export default {
  props: ["comentarios"],
  data() {
    return {
      access: "",
      superuser: "",
      value: 1,
      user: {},
    };
  },
  computed: {
    ...mapState(useAuthStore, ["is_superuser", "access", "username"]),
  },
};
</script>

<template>
  <div class="all">
    <div class="flex mb-12">
      <div class="flex flex-col">
        <div
          class="bg-gray-200 p-6 rounded-3xl rounded-bl-none w-96 shadow-sm mb-2"
        >
          <p class="font-medium mb-1">{{ comentarios.autor.username }}</p>
          <small class="inline-block text-gray-500 mb-1">{{
            comentarios.texto
          }}</small>
        </div>
        <small class="text-gray-500">{{ comentarios.data }}</small>
      </div>
    </div>
    <div class="flex flex-row-reverse mb-12">
      <div class="flex flex-col">
        <div
          class="bg-sky-900 text-white p-6 rounded-3xl rounded-br-none w-96 mb-2"
        >
          <p class="font-medium mb-1">{{ comentarios.autor.username }}</p>
          <small class="inline-block mb-1">{{ comentarios.texto }}</small>
        </div>
        <small class="text-gray-500 self-end">{{ comentarios.data }}</small>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
