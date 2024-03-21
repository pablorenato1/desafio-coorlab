<template>
  <div class="center-content">
    <div class="top-line">
      <p class="center-content-title">Calculadora de Viagem</p>
    </div>
    <div class="center-content-container">
      <div class="left-side">
        <h2>Calcule o Valor da Viagem</h2>
        <h4>Destino:</h4>
        <input type="text" placeholder="Selecione um Destino" v-model="input2">
        <h4>Data:</h4>
        <div>
          <input type="date" id="data" v-model="selectedDate" placeholder="Selecione uma data">
        </div>
        <br>
        <div class="button-container">
          <button @click="submitForm">Enviar</button>
        </div>
      </div>
      <div class="right-side">
        <p v-if="selectedData">{{ selectedData }}</p>
        <p v-else>Nenhuma data selecionada.</p>
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
      selectedDate: null,
      selectedData: ''
    };
  },
  methods: {
    submitForm() {
      // Process form data here
      this.selectedData = `${this.input1} - ${this.input2} - ${this.selectedDate}`;
      // You can modify this logic to fit your actual requirements
    }
  }
};
</script>

<style scoped>
:root {
  --margin: 13rem;
}

.center-content {
  margin: 2rem auto;
  max-width: 1280px;
  background-color: #fff;
  border-radius: 2px;
  width: 60%;
  box-shadow: 0 3px 8px -2px rgb(95, 93, 93);
  overflow: hidden;
}

.center-content-container {
  display: flex;
  max-height: fit-content;
  height: 87%;
}

.top-line {
  background-color: #2a2f40;
  margin-bottom: 1rem;
  border-radius: 2px 2px 0 0;
  color: #fff;
}

.center-content-title {
  padding: 1rem;
  font-weight: 700;
  margin: 0; /* Remove default margin for the title */
}

.left-side {
  background-color: #f3f3f3;
  padding: 100px 30px;
  margin: 1rem;
  border-radius: 6px;
  margin-right: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.right-side {
  flex: 2;
  background-color: #ccc;
  padding: 20px;
  border-radius: 6px;
  margin: 1rem 1rem 1rem 0;
}

.right-side p {
  color: #333;
  font-style: italic;
  margin: 0; /* Remove default margin for paragraphs */
}

h4 {
  text-align: left;
  margin-bottom: 0;
  font-weight: 100;
}

input {
  margin-bottom: 1rem;
  width: calc(100% - 20px);
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  box-sizing: border-box;
  margin-left: 0;
  width: 100%;
}

button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  width: 140px;
}

.button-container {
  text-align: center;
}

button:hover {
  background-color: #0056b3;
}
</style>
