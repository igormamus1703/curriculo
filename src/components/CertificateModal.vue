<template>
    <Modal :isVisible="isVisible" @close="closeModal">
      <div v-if="certificate">
        <h3>{{ certificate.title }}</h3>
        <p><strong>Emitido por:</strong> {{ certificate.issuer }}</p>
        <p><strong>Data de Emissão:</strong> {{ certificate.date }}</p>
        <p><strong>Descrição:</strong> {{ certificate.description }}</p>
      </div>
    </Modal>
  </template>
  
  <script>
  import Modal from "./Modal.vue";
  
  export default {
    name: "CertificateModal",
    components: {
      Modal,
    },
    props: {
      isVisible: {
        type: Boolean,
        required: true,
      },
      certificate: {
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
  