<template>
  <div id="app">
    <Header />
    <select @change="changeLanguage($event)" class="language-selector">
      <option value="pt">Português</option>
      <option value="en">English</option>
    </select>
    <main>
      <Projects />
      <Experience />
      <CertificateCarousel />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Projects from "./components/Projects.vue";
import Experience from "./components/Experience.vue";
import CertificateCarousel from "./components/CertificateCarousel.vue"; 
import Footer from "./components/Footer.vue";


export default {
  name: "App",
  components: {
    Header,
    Projects,
    Experience,
    CertificateCarousel,
    Footer,
  },
  methods: {
    changeLanguage(event) {
      this.$i18n.locale = event.target.value;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0;
}
main {
  padding: 20px;
}
.language-selector {
  position: fixed;
  top: 10px;
  right: 10px;
  background-color: white;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
</style>
