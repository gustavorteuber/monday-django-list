<script>
import axios from "axios";
export default {
  components: { notificationbar, dashboard },
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
  },
};
</script>

<template>
  <dashboard />
  <notificationbar
    v-for="tarefa in tarefas"
    :key="tarefa.id"
    :tarefa="tarefa"
  />
</template>
