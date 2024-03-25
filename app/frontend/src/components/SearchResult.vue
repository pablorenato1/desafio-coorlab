<script setup lang="ts">
defineProps<{
  ticketOption: {
    name: string,
    price: string,
    duration: string,
    seat_code: string,
    seat_type: string,
    ticket_code: number
  }[]
}>()
</script>

<template>
  <div class="travel-option-item" v-for="(ticket, index) in ticketOption" :key="index">
    <div class="card-flight">
      <div v-if="ticket.ticket_code  === 1" class="rectangle-info-icon">
        <v-icon icon="mdi-hand-coin-outline" class="white-color"></v-icon>
      </div>
      <div v-else class="rectangle-info-icon">
        <v-icon icon="mdi-clock-check-outline" class="white-color"></v-icon>
      </div>
      <div class="rectangle-info">
        <div class="rectangle-info-description">
          <h3>{{ ticket.name }}</h3>
          <p class="simple-text">{{ ticket.seat_type }}: {{ ticket.seat_code }}</p>
          <p class="simple-text">Tempo estimado: {{ ticket.duration }}</p>
        </div>
      </div>
      <div class="rectangle-price">
        <h3 class="bold-text">Preço</h3>
        <div class="simple-text">{{ ticket.price }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-flight {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2.5%;
  height: 100%;
}

.rectangle-info-icon {
  background-color: #03a7b4;
  font-size: 20px;
  border-radius: 5px 0 0 5px;
  padding: 1.3rem 1.5rem;
}

.rectangle-info {
  display: flex;
  align-items: center;
  border-radius: 0 5px 5px 0;
  background-color: #f1f1f1;
  width: 90%;
  min-width: 286px;
  padding: 1rem;
  box-sizing: border-box;
}

.rectangle-info-description {
  font-size: 14px;
  color: #333;
  margin-left: 1rem;
}

.rectangle-price {
  color: #333;
  width: 30%;
  background-color: #e1e1e1;
  border-radius: 5px;
  padding: 1rem;
  margin-left: 1.5rem;
}

.bold-text {
  font-weight: bold;
}

.simple-text {
  margin-left: 0.5rem;
  font-size: 16px;
}

.white-color {
  color: white;
  font-size: 40px;
  padding-top: 50%;
}
</style>