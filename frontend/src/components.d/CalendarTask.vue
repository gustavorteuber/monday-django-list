<script>
import { mapState } from "pinia";
import { useAuthStore } from "@/stores/auth";
import axios from 'axios'
import dayjs from 'dayjs'
import relativeTime from "dayjs/plugin/relativeTime";
 
dayjs.extend(relativeTime)

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
   pegarDia(diaInicial, diaFinal) {

    console.log(dayjs(diaInicial).to(diaFinal))
    let result = dayjs(diaInicial).to(diaFinal)
    return result;
   },
  },
  computed: {
    ...mapState(useAuthStore, ["id","username", "foto"]),
  },

};
</script>
<template>
    <!-- component -->
  <div class="bg-white text-violet-600 w-full max-w-md flex flex-col rounded-xl shadow-lg p-4">
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-4">
        <div class="rounded-full w-4 h-4 border border-violet-500"></div>
        <div class="text-md font-bold">{{ tarefa.titulo }}</div>
      </div>
      <div class="flex items-center space-x-4">
        <div class="cursor-pointer">
          <img class="w-5 h-5 rounded-lg" :src="tarefa.foto.file" />
        </div>
        <div class="text-gray-500 hover:text-gray-300 cursor-pointer">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
          </svg>
        </div>
        <div class="text-gray-500 hover:text-gray-300 cursor-pointer">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9" />
          </svg>
        </div>
      </div>
    </div>
    <div class="mt-4 text-gray-500 font-bold text-sm">
      {{ tarefa.descricao }}
    </div>
  </div>
</template>