<template>
  <section class="projects">
    <h2>Projetos</h2>
    <div class="project-list">
      <div v-for="project in projects" :key="project.id" class="project-item" @click="openModal(project)">
        <img :src="project.image" alt="Project Image" class="project-image" />
        <div class="project-info">
          <h3>{{ project.name }}</h3>
          <p>{{ project.shortDescription }}</p>
        </div>
      </div>
    </div>
    <ProjectModal :isVisible="isModalVisible" :project="selectedProject" @close="closeModal" />
  </section>
</template>

<script>
import ProjectModal from "./ProjectModal.vue";

export default {
  name: "Projects",
  components: {
    ProjectModal,
  },
  data() {
    return {
      projects: [
        {
          id: 1,
          name: "Sistema de Gestão de Tarefas",
          description: "Um sistema completo para gerenciar tarefas com funcionalidades como adição, edição e exclusão.",
          shortDescription: "Sistema de Gestão de Tarefas com Vue.js",
          link: "https://github.com/seuusuario/sistema-gestao-tarefas",
          technologies: ["Vue.js", "Node.js", "MongoDB"],
          image: "link-para-imagem-projeto-1.png"
        },
        {
          id: 2,
          name: "Website Portfólio",
          description: "Um website portfólio moderno e responsivo para apresentar projetos e habilidades.",
          shortDescription: "Website Portfólio Responsivo",
          link: "https://github.com/seuusuario/website-portfolio",
          technologies: ["HTML", "CSS", "JavaScript"],
          image: "link-para-imagem-projeto-2.png"
        }
      ],
      isModalVisible: false,
      selectedProject: null,
    };
  },
  methods: {
    openModal(project) {
      this.selectedProject = project;
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
      this.selectedProject = null;
    },
  },
};
</script>

<style scoped>
.projects {
  padding: 20px;
}
.project-list {
  display: flex;
  flex-direction: column;
}
.project-item {
  display: flex;
  align-items: center;
  cursor: pointer;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 5px;
  transition: background-color 0.2s;
}
.project-item:hover {
  background-color: #f0f0f0;
}
.project-image {
  width: 50px;
  height: 50px;
  border-radius: 8px;
  margin-right: 15px;
}
.project-info {
  flex-grow: 1;
}
</style>
