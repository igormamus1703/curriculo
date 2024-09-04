<template>
    <section class="experience">
      <h2>Experiência</h2>
      <div class="experience-list">
        <div v-for="job in jobs" :key="job.id" class="experience-item" @click="openModal(job)">
          <img :src="job.image" alt="Company Logo" class="experience-image" />
          <div class="experience-info">
            <h3>{{ job.title }}</h3>
            <p>{{ job.company }}</p>
          </div>
        </div>
      </div>
      <ExperienceModal :isVisible="isModalVisible" :experience="selectedJob" @close="closeModal" />
    </section>
  </template>
  
  <script>
  import ExperienceModal from "./ExperienceModal.vue";
  
  export default {
    name: "Experience",
    components: {
      ExperienceModal,
    },
    data() {
      return {
        jobs: [
          {
            id: 1,
            title: "Estágio em Desenvolvimento Web",
            company: "Empresa XYZ",
            address: "Rua Exemplo, 123",
            phone: "(11) 98765-4321",
            description: "Trabalhei com desenvolvimento de aplicações web utilizando Vue.js e Node.js.",
            image: "link-para-imagem-empresa-xyz.png"
          },
          {
            id: 2,
            title: "Estágio em Data Science",
            company: "Empresa ABC",
            address: "Avenida Teste, 456",
            phone: "(21) 91234-5678",
            description: "Desenvolvimento de modelos de machine learning e análise de dados.",
            image: "link-para-imagem-empresa-abc.png"
          }
        ],
        isModalVisible: false,
        selectedJob: null,
      };
    },
    methods: {
      openModal(job) {
        this.selectedJob = job;
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
        this.selectedJob = null;
      },
    },
  };
  </script>
  
  <style scoped>
  .experience {
    padding: 20px;
  }
  .experience-list {
    display: flex;
    flex-direction: column;
  }
  .experience-item {
    display: flex;
    align-items: center;
    cursor: pointer;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
    transition: background-color 0.2s;
  }
  .experience-item:hover {
    background-color: #f0f0f0;
  }
  .experience-image {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 15px;
  }
  .experience-info {
    flex-grow: 1;
  }
  </style>
  