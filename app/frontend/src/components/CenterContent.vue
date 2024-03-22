<script setup>
import { ref } from 'vue';


var location = ref("");
var selectedDate = ref("");
var bothSelected = ref(false)

const submitRequest = () => {
    if (selectedDate || location) {
      console.log(`${selectedDate.value} ${location.value}`);
      bothSelected.value = ref(true)
      getTickets().then(data => {
        console.log("Tickets: ",data)
      })
    }
  }
const test = {
        name: "PASSARO VERDE",
        price: "R$ 650,00",
        duration: "14h",
        seat: "2 (convencional)",
        seatType: "5L",
        isCheap: true,
    }

  const getTickets = () => {
  return new Promise((resolve, reject) => {
    fetch('http://localhost:3000/api/ticket')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        console.log(response)
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

// Usage example
getTickets()
  .then(data => {
    console.log('Tickets:', data);
    // Here you can work with the received data
  })
  .catch(error => {
    console.error('Error fetching tickets:', error);
  });

</script>

<script>
import SearchResult from "./SearchResult.vue";
</script>

<template>
  <div class="center-content">
    <div class="top-line">
      <h2 class="center-content-title"><v-icon icon="mdi-truck-delivery-outline"></v-icon> Calculadora de Viagem</h2>
    </div>
    <div class="center-content-container">
      <div class="left-side">
        <h2><v-icon icon="mdi-hand-coin-outline"></v-icon> Calcule o Valor da Viagem</h2>
        <h4>Destino:</h4>
        <v-select
                label="Select"
                :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
                variant="outlined"
                v-model="location"
                class="input-field"
              ></v-select>
        <h4>Data:</h4>
        <div>
          <input type="date" id="data" v-model="selectedDate" placeholder="Selecione uma data" class="input-field">
        </div>
        <br>
        <div class="button-container">
          <button @click="submitRequest">Enviar</button>
        </div>
      </div>
      <div class="right-side">
        <p v-if="bothSelected">
          <SearchResult :ticketOption=test></SearchResult>
          
        </p>
        <p v-else>Nenhuma data selecionada.</p>
      </div>
    </div>
  </div>
</template>



<style scoped>
:root {
  --margin: 13rem;
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

button {
  padding: 10px;
  background-color: #03a7b4;
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

.right-side-less-expensive {
  height: 10px;
  background-color: red;
}
.right-side-short-distance {
  background-color: greenyellow;
  height: 10px;
}
</style>
