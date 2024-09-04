<template>
    <Modal :isVisible="isVisible" @close="closeModal">
      <div v-if="experience">
        <h3>{{ experience.title }}</h3>
        <p><strong>Empresa:</strong> {{ experience.company }}</p>
        <p><strong>Endereço:</strong> {{ experience.address }}</p>
        <p><strong>Telefone:</strong> {{ experience.phone }}</p>
        <p><strong>Descrição:</strong> {{ experience.description }}</p>
      </div>
    </Modal>
  </template>
  
  <script>
  import Modal from "./Modal.vue";
  
  export default {
    name: "ExperienceModal",
    components: {
      Modal,
    },
    props: {
      isVisible: {
        type: Boolean,
        required: true,
      },
      experience: {
        type: Object,
        required: false,
      },
    },
    methods: {
      closeModal() {
        this.$emit("close");
      },
    },
  };
  </script>
  