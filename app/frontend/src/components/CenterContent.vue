<script setup>
import { ref } from 'vue';
import { VueElement } from 'vue';
import SearchResult from './SearchResult.vue';

// Variables
const location = ref("");
const allLocation = ref([]);
const selectedDate = ref("");
const noDataSelected = ref(true);
let tickets = ref([]);
const dialog = ref(false)

const clearInputs = () => {
  tickets = []
  selectedDate.value = ""
  location.value = ""
}

// Function to fetch locations
const getLocations = () => {
  fetch('http://localhost:3000/api/locals')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      allLocation.value = data;
    })
    .catch(error => {
      console.error('Error fetching locations:', error);
    });
};

// Call the function to fetch locations
getLocations();

// Function to submit the request
const submitRequest = () => {
  // 
  if (!selectedDate.value || !location.value) {
    dialog.value = true;
    return;
  }


  getTickets().then(data => {
    tickets.value = data;
    noDataSelected.value = false;
  });
};

// Function to get tickets
const getTickets = () => {
  return new Promise((resolve, reject) => {
    fetch('http://localhost:3000/api/ticket', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        location: location.value,
        date: selectedDate.value
      })
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        resolve(data);
      })
      .catch(error => {
        reject(error);
      });
  });
};
</script>


<template>
  <div class="center-content">
    <div class="top-line">
      <h2 class="center-content-title"><v-icon icon="mdi mdi-airplane"></v-icon> Calculadora de Viagem</h2>
    </div>
    <div class="center-content-container">
      <div class="left-side">
        <h2><v-icon icon="mdi-hand-coin-outline"></v-icon> Calcule o Valor da Viagem</h2>
        <h4>Destino:</h4>
        <v-select label="Select" :items=allLocation variant="outlined" v-model="location"
          class="inputField"></v-select>
        <h4>Data:</h4>
        <div>
          <input type="date" id="data" v-model="selectedDate" placeholder="Selecione uma data" class="inputField">
        </div>
        <br>
        <div class="button-container">
          <button class="sent-button" @click="submitRequest">Enviar</button>
          <v-btn class="clear-selected" @click="clearInputs">Limpar</v-btn>
          <v-dialog v-model="dialog" width="auto">
            <div class="modal">
              <img class="modal-exclamation" src="../assets/exclamation.png" alt="" srcset="">
              <p class="modal-text">Insira os valores para realizar a cotação</p>
              <v-btn @click="dialog = false">Fechar</v-btn>
            </div>
          </v-dialog>
        </div>
      </div>
      <div class="right-side">
        <div class="right-container">
          <div class="right-container-content" v-if="noDataSelected">
            <h3>Não há nenhum dado seleciondo</h3>
          </div>

          <div class="right-container-content" v-else>
            <h3 class="distance-content">Estas são as melhores alternativas de viagem para a data selecionada</h3>
            <SearchResult :ticketOption=tickets></SearchResult>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<style scoped>
:root {
  --margin: 13rem;
}

.distance-content {
  margin-bottom: 2%;
}

.sent-button {
  padding: 10px;
  background-color: #03a7b4;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  width: 200px;
}

.clear-selected {
  background-color: #f2a42f;
  color: black;
  border: none;
  padding: 4px 20px;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
  width: 200px;
  bottom: 0;
  margin-top: 2%;
}

.modal-exclamation {
  width: 3.5rem;
  margin-bottom: 1rem;
}

.modal-text {
  font-weight: 16px;
}

.center-content {
  margin: 2rem;
  max-width: 1280px;
  background-color: #fff;
  border-radius: 2px;
  width: 70%;
  box-shadow: 0 3px 8px -2px rgb(95, 93, 93);
  overflow: hidden;
}

.center-content-container {
  display: flex;
  max-height: fit-content;
  height: 87%;
  /* wid */
}

.top-line {
  background-color: #2a2f40;
  margin-bottom: 1rem;
  border-radius: 2px 2px 0 0;
  color: #fff;
}

.center-content-title {
  padding: 1rem;
  font-weight: 400;
  margin-left: 1rem;
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
  background-color: #fff;
  padding: 20px;
  border-radius: 6px;
  margin: 1rem 1rem 1rem 0;
}

.right-side p {
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
  color: #333;
  font-style: italic;
  margin: 0;
}

h4 {
  text-align: left;
  margin-bottom: 0;
  font-weight: 100;
}

h2 {
  padding-bottom: 5%;
  font-size: 18px;
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

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center
}

button:hover {
  background-color: #0056b3;
}

.right-side-less-expensive {
  height: 10px;
  background-color: red;
}

.right-side-short-distance {
  background-color: greenyellow;
  height: 10px;
}

.modal {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  background-color: #ffffff;
  padding-top: 2.5rem;
  padding-bottom: 1.5rem;
  padding-left: 5rem;
  padding-right: 5rem;
  border-radius: 1rem;
}

.modal p {
  font-size: 1.2rem;
}

.modal button {
  background-color: #03a8b4;
  color: #024b55;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  text-transform: none;
}

.exlamation-mark-modal {
  color: #03a7b4;
  font-size: 50px;
  padding: 5px;
  border: 4px solid #03a7b4;
  border-radius: 5px;
}
</style>
