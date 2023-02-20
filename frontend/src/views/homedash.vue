<script>
import dashboard from "../components/dashboard.vue";
import notificationbar from "../components/notifications.vue";
export default {
  components: { dashboard, notificationbar },
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
