<template>
  <div>
    <Sidebar />
    <Navbar />
    <div class="container">
      
        <!-- Conteúdo principal da sua aplicação aqui -->
        <CenterContent  />
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import Sidebar from './components/Sidebar.vue';
import CenterContent from './components/CenterContent.vue';

export default {
  components: {
    Navbar,
    Sidebar,
    CenterContent
  },
}
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  height: fit-content;
  align-items: center;
  margin-left: 14rem;
}



/* Additional styling for a cohesive layout */
.sidebar {
  flex: 0 0 200px; /* Fix sidebar width */
}

.navbar {
  margin-left: 17rem;
}

@ts-ignore
</style>