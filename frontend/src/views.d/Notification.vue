<script>
import notificationbar from "@/components/notificationcomp.vue";
import axios from "axios";
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";

dayjs.extend(relativeTime);

export default {
  components: { notificationbar },
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
  <notificationbar
    v-for="tarefa in tarefas"
    :key="tarefa.id"
    :tarefa="tarefa"
  />
</template>
