<template>
  <div id="app">
    <Header />
    <main>
      <Projects />
      <Experience />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Projects from "./components/Projects.vue";
import Experience from "./components/Experience.vue";
import Footer from "./components/Footer.vue";


export default {
  name: "App",
  components: {
    Header,
    Projects,
    Experience,
    Footer,
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
</style>
