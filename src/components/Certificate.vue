<template>
    <section class="certificates">
      <h2>Certificados</h2>
      <div class="certificate-list">
        <div v-for="cert in certificates" :key="cert.id" class="certificate-item" @click="openModal(cert)">
          <img :src="cert.image" alt="Certificate Logo" class="certificate-image" />
          <div class="certificate-info">
            <h3>{{ cert.title }}</h3>
            <p>{{ cert.issuer }}</p>
          </div>
        </div>
      </div>
      <CertificateModal :isVisible="isModalVisible" :certificate="selectedCertificate" @close="closeModal" />
    </section>
  </template>
  
  <script>
  import CertificateModal from "./CertificateModal.vue";
  
  export default {
    name: "Certificates",
    components: {
      CertificateModal,
    },
    data() {
      return {
        certificates: [
          {
            id: 1,
            title: "Certificado de Vue.js",
            issuer: "Coursera",
            date: "Jan 2023",
            description: "Curso completo de Vue.js abordando desde conceitos básicos até avançados.",
            image: "link-para-imagem-certificado-vuejs.png"
          },
          {
            id: 2,
            title: "Certificado de Data Science",
            issuer: "DataCamp",
            date: "Feb 2022",
            description: "Curso focado em técnicas de Data Science e Machine Learning.",
            image: "link-para-imagem-certificado-datascience.png"
          }
        ],
        isModalVisible: false,
        selectedCertificate: null,
      };
    },
    methods: {
      openModal(cert) {
        this.selectedCertificate = cert;
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
        this.selectedCertificate = null;
      },
    },
  };
  </script>
  
  <style scoped>
  .certificates {
    padding: 20px;
  }
  .certificate-list {
    display: flex;
    flex-direction: column;
  }
  .certificate-item {
    display: flex;
    align-items: center;
    cursor: pointer;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
    transition: background-color 0.2s;
  }
  .certificate-item:hover {
    background-color: #f0f0f0;
  }
  .certificate-image {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 15px;
  }
  .certificate-info {
    flex-grow: 1;
  }
  </style>
  