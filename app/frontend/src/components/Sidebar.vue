<template>
    <div class="sidebar">
        <img src="../assets/logo.png" alt="" srcset="">
        
      <ul>
        <li><a href="#"><v-icon icon="mdi-calculator-variant-outline"></v-icon>  Calculadora de Viagem</a></li>
      </ul>
    </div>
  </template>

  <script>
  
  </script>
  
  <style scoped>
  .sidebar {
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
    width: 17rem;
    background-color: #2a2f40;
    color: #fff;
    padding-top: 20px;
    padding-left: 20px;
    z-index: 1;
  }
  img {
    width: 10rem;
    margin-bottom: 1rem;
  }
  
  ul {
    list-style-type: none;
    padding-left: 0;
  }
  
  li {
    margin-bottom: 10px;
  }
  
  a {
    color: #fff;
    text-decoration: none;
    padding: 10px;
  }
  
  a:hover {
    background-color: #555;
  }
  </style>
  