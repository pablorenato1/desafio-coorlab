<template>
    <div></div>

    <p v-if="fastOption === 'false'">Banana</p>
    <p v-else>Batata</p>
</template>

<style>
</style>

<script setup lang="ts">
    import { ref } from 'vue'
    defineProps<{fastOption: String, ticketOption: Object}>()

</script>
