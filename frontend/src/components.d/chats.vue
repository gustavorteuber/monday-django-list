<template>
  <div
    class="all"
    :class="{
      'bg-gray-200': !isCommentByLoggedUser,
      'bg-violet-900 ': isCommentByLoggedUser,
      'flex-row-reverse  mb-12': isCommentByLoggedUser,
      'flex-row  mb-12': !isCommentByLoggedUser,
      'flex-row-reverse  mb-12': isCommentByLoggedUser,
      'flex-row  mb-12': !isCommentByLoggedUser,
    }"
    ref="comentariosContainer"
  >
    <div class="all">
      <div class="flex flex-col">
        <div
          class="p-6 rounded-3xl rounded-br-none w-96 mb-2"
          :class="{
            'text-white': isCommentByLoggedUser,
            'self-end': isCommentByLoggedUser,
          }"
        >
          <p class="font-medium mb-1">{{ comentarios.autor.username }}</p>
          <small class="inline-block mb-1">{{ comentarios.texto }}</small>
        </div>
        <small
          class="text-gray-500"
          :class="{ 'self-end': isCommentByLoggedUser }"
          >{{ comentarios.data }}</small
        >
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "pinia";
import { useAuthStore } from "@/stores/auth";
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";

dayjs.extend(relativeTime);

export default {
  props: ["comentarios"],
  data() {
    return {};
  },
  computed: {
    ...mapState(useAuthStore, ["is_superuser", "access", "username"]),
    isCommentByLoggedUser() {
      return this.username === this.comentarios.autor.username;
    },
  },
};
</script>
