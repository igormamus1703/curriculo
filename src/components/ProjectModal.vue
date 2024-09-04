<template>
    <Modal :isVisible="isVisible" @close="closeModal">
      <div v-if="project">
        <h3>{{ project.name }}</h3>
        <p><strong>Descrição:</strong> {{ project.description }}</p>
        <p><strong>Link:</strong> <a :href="project.link" target="_blank">{{ project.link }}</a></p>
        <p><strong>Tecnologias:</strong> {{ project.technologies.join(', ') }}</p>
      </div>
    </Modal>
  </template>
  
  <script>
  import Modal from "./Modal.vue";
  
  export default {
    name: "ProjectModal",
    components: {
      Modal,
    },
    props: {
      isVisible: {
        type: Boolean,
        required: true,
      },
      project: {
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
  