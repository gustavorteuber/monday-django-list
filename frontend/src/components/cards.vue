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
        <!-- 1 card -->
        <div class="relative bg-white py-6 px-6 rounded-3xl w-64 my-4 shadow-xl">
            <div class=" text-white flex items-center absolute rounded-full py-4 px-4 shadow-xl bg-violet-500 left-4 -top-6">
                <!-- svg  -->
                            <img :src="tarefa.foto.file" alt="" class="w-10 h- rounded-full"/>
            </div>
            <div class="mt-8">
                <p class="text-xl font-semibold my-2">{{ tarefa.titulo }}</p>
                <div class="flex space-x-2 text-gray-400 text-sm">
                    <!-- svg  -->
                     <p>{{ tarefa.descricao }}</p> 
                </div>
                <div class="flex space-x-2 text-gray-400 text-sm my-3">
                    <!-- svg  -->
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                     <p>{{  pegarDia(tarefa.datainicio, tarefa.prazofinal) }}</p> 
                </div>
                <div class="border-t-2"></div>

                <div class="flex justify-between">
                    <div class="my-2">
                        <p class="font-semibold text-base mb-2">Team Member</p>
                        <div class="flex space-x-2">
                            <img src="https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" 
                            class="w-6 h-6 rounded-full"/>
                             <img src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Woman_7.jpg" 
                            class="w-6 h-6 rounded-full"/>
                             <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxSqK0tVELGWDYAiUY1oRrfnGJCKSKv95OGUtm9eKG9HQLn769YDujQi1QFat32xl-BiY&usqp=CAU" 
                            class="w-6 h-6 rounded-full"/>
                        </div>
                    </div>
                     <div class="my-2">
                        <p class="font-semibold text-base mb-2">Lider: </p>
                        <div class="text-base text-gray-400 font-semibold">
                            <img :src="tarefa.lider.foto.file" alt="" class="w-8 h-8 rounded-full"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</template>
<style>
.checkbox:checked {
  border: none;
}
.checkbox:checked + .check-icon {
  display: flex;
}
</style>
