<script setup lang="ts">
defineProps<{
  ticketOption: {
    name: String,
    price: String,
    duration: String,
    seat: String,
    seatType: String,
    isCheap: Boolean,
  }
}>()
</script>

<template>
  <div>
    <h4>Estas são as melhores alternativas de viagem para a data selecionada</h4>
    <div class="card-flight">
      <div class="rectangle-info-icon">
          <v-icon icon="mdi-hand-coin-outline" class="white-color"></v-icon>
      </div>
        <div class="rectangle-info">
            <div class="rectangle-info-description">
                <p class="bold-text"> {{ ticketOption.name }}</p>
                <p class="simple-text">Leito: {{ ticketOption.seat }}</p>
                <p class="simple-text">Tempo estimado: {{ ticketOption.duration }}</p>
            </div>
        </div>
        <div class="rectangle-price">
          <p class="bold-text">Preço</p>
          <div class="simple-text">{{ ticketOption.price }}</div>
        </div>
    </div>
  </div>
</template>

<style scoped>

.card-flight {
  display: flex;
  justify-content: space-between;
}

.rectangle-info {
  display: flex;
  align-items: center;
  border-radius: 0 5px 5px 0;
  background-color: #f1f1f1;
  width: 90%;
  min-width: 286px;
}

.rectangle-info-icon {
  background-color: #03a7b4;
  font-size: 20px;
  border-radius: 5px 0 0 5px;
  padding: 1.5rem;
}

.rectangle-info-description {
  font-size: 14px;
  color: #333;
  margin-left: 1rem;
  background-color: #f1f1f1
}

.rectangle-price {
  display: flex;
  flex-direction: column;
  align-items: start;
  font-size: 16px;
  font-weight: bold;
  color: #333;
  width: 30%;
  background-color: #e1e1e1;
  border-radius: 5px;
  padding: 3%;
  margin-left: 2%;
}

.bold-text {
  font-weight: bold;
}

p {
font-size: 16px;
}

h4 {
  margin-bottom: 2%;
  font-size: 100%;
}

.white-color {
  color: white;
  font-size: 40px;
}
</style>