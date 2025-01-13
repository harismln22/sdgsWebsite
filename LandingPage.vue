<template>
  <div>
    <HeaderComponent />
    <main class="main">
      <!-- Body content remains unchanged -->
    </main>
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from './HeaderComponent.vue';
import FooterComponent from './FooterComponent.vue';

export default {
  components: {
    HeaderComponent,
    FooterComponent
  }
};
</script>