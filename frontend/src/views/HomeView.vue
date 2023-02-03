<script>
import cards from "@/components/cards.vue";
import axios from "axios";
export default {
  name: 'Home',
  components: { cards },
  data() {
    return {
      tarefas: [],
    };
  },
  async created() {
    await this.getAllTasks();
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
}
};
</script>

<template>
  <div class="content">
    <h3 class="text-2xl font-bold text-left py-2">Pagina Inicial</h3>
    <br>
    <div class="card-group">
      <cards
        v-for="tarefa in tarefas"
        :key="tarefa.id"
        :tarefa="tarefa"
      />
    </div>
    <div class="overflow-x-auto relative sm:rounded-lg">
      <table
        class="w-full text-sm text-left text-violet-500 dark:text-gray-400"
      >
        <thead
          class="text-xs text-black uppercase bg-gray-50 dark:bg-violet-700 dark:text-gray-400"
        >
          <tr>
            <th scope="col" class="py-3 px-6">
              <div class="flex items-center">
                <a href="#">
                  <path
                    d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"
                  ></path>
                </a>
              </div>
            </th>
            <th scope="col" class="py-3 px-6">
              <div class="flex items-center"></div>
            </th>
            <th scope="col" class="py-3 px-6">
              <div class="flex items-center">
                <path
                  d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"
                ></path>
              </div>
            </th>
            <th scope="col" class="py-3 px-6">
              <span class="sr-only">Edit</span>
            </th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>
  </div>
</template>

<style>
</style>
