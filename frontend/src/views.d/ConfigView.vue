<script>
import { mapState, mapStores } from "pinia";
import { useAuthStore } from "@/stores/auth";
import axios from "axios";
export default {
  data() {
    return {
      user: {
        username: "",
        email: "",
        first_name: "",
      },
    };
  },
  // async created() {
  //   // const user = await axios.get("https://horseti.pythonanywhere.com/token/");
  //   // this.user = cachorros.data;
  // },
  async created() {
    const res = await axios.get(`http://localhost:8000/usuario/${this.id}/`);
    this.user = res.data;
    console.log(this.user);
  },
  methods: {
    async editarPerfil() {
      const info = {
        foto_attachment_key: this.user.foto_attachment_key,
        username: this.user.username,
        email: this.user.email,
        first_name: this.user.first_name,
      };
      try {
        await axios.patch(`http://localhost:8000/usuario/${this.id}/`, info);
        alert("por favor deslogar para salvar as informações");
      } catch {
        ("Algo deu errado, tente novamente ");
      }
    },
    uploadFile() {
      this.Images = this.$refs.file.files[0];
    },
    async submitFile() {
      const formData = new FormData();
      formData.append("file", this.Images);
      const headers = { "Content-Type": "multipart/form-data" };
      const { data } = await axios.post(
        "http://localhost:8000/media/images/",
        formData,
        { headers }
      );
      this.user.foto_attachment_key = data.attachment_key;
      alert("Foto adicionada!");
    },
  },
  computed: {
    ...mapStores(useAuthStore),
    ...mapState(useAuthStore, ["username", "email", "id", "first_name"]),
  },
};
</script>
<template>
  <h1>ksdksdjsk</h1>
</template>
