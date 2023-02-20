<script>
import { mapState } from "pinia";
import { useAuthStore } from "../components/login/stores/auth";
import axios from "axios";
export default {
  props: ["tarefa"],
  user: {},
  data() {
    return {
      tarefas: [],
    };
  },
  methods: {
    async getAllTasks() {
      axios
        .get(`http://127.0.0.1:8000/tarefa/`)
        .then((res) => {
          this.tarefas = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  computed: {
    ...mapState(useAuthStore, ["id", "username", "foto"]),
  },
};
</script>
<template>
  <ol class="relative border-l border-gray-200 dark:border-gray-700">
    <li class="mb-10 ml-6">
      <span
        class="absolute flex items-center justify-center w-6 h-6 bg-blue-100 rounded-full -left-3 ring-8 ring-white dark:ring-gray-900 dark:bg-blue-900"
      >
        <svg
          aria-hidden="true"
          class="w-3 h-3 text-blue-800 dark:text-blue-300"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
            clip-rule="evenodd"
          ></path>
        </svg>
      </span>
      <h3
        class="flex items-center mb-1 text-lg font-semibold text-gray-900 dark:text-white"
      >
        {{ tarefa.titulo }}
        <span
          class="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300 ml-3"
          >Novo</span
        >
      </h3>
      <time
        class="block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500"
        >{{ tarefa.datainicio }}</time
      >
      <p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
        {{ tarefa.descricao }}
      </p>
    </li>
  </ol>
</template>
