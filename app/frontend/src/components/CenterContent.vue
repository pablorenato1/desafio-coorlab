<template>
    <div class="center-content">
      <div class="top-line"><p class="center-content-title">Calculadora de Viagem</p></div>
      <div class="center-content-container">
        <div class="left-side">
          <p>Calcule o Valor da Viagem</p>
          <input type="text" placeholder="Input 1" v-model="input1">
          <input type="text" placeholder="Input 2" v-model="input2">
          <br>
          <button @click="submitForm">Submit</button>
        </div>
        <div class="right-side">
          <p v-if="selectedData">{{ selectedData }}</p>
          <p v-else>No data selected.</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        input1: '',
        input2: '',
        selectedData: null
      };
    },
    methods: {
      submitForm() {
        // Process form data here
        this.selectedData = `${this.input1} - ${this.input2}`;
        // You can modify this logic to fit your actual requirements
      }
    }
  }
  </script>
  
  <style scoped>
  .center-content {
    margin-top: 2rem;
    background-color: #fff;
    /* height: ; */
    border-radius: 2px;
    box-shadow: 0 3px 8px -2px rgb(95, 93, 93);
  }
  
  .center-content-container {
    display: flex;
    justify-content: space-between;
    border-radius: 2px;
  }

  .top-line {
    background-color: #2a2f40;
    height: 3rem;
    width: inherit;
    margin-bottom: 1.5rem;
    border-radius: 2px 2px 0 0;
    color: #fff;
  }

  .center-content-title {
    padding: 1rem;
    font-weight: 700;
  }
  
  .left-side {
    width: 12rem;
    background-color: #f3f3f3;
    padding: 5rem 2rem 8rem 2rem;
    border-radius: 6px;
    margin: 1rem;
  }

  .right-side {
    width: 55%;
    background-color: #fff;
    padding: 20px;
    margin: 1rem;
  }
  
  .right-side p {
    color: #888;
    font-style: italic;
  }
  
  input {
    margin-bottom: 2rem;
  }
  </style>
  