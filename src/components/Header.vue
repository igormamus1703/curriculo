<template>
    <header class="header">
      <h1>{{ name }}</h1>
      <p>{{ description }}</p>
    </header>
  </template>
  
  <script>
  export default {
    name: "Header",
    data() {
      return {
        name: "Igor Mamus Dos Santos",
        description: "Estudante Ciência da Computação | PUCPR",
      };
    },
  };
  </script>
  
  <style scoped>
  .header {
    text-align: center;
    padding: 20px;
    background-color: #f8f8f8;
  }
  </style>
  