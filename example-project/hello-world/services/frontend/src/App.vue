<template>
  <v-app>
    <div>
      <v-container fluid>
        <img src="./assets/pengu.png" style="height: 100px">
        <h1>AirPenguins</h1>
      </v-container>
    </div>
    <v-main >
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<style>
/* disable scrolling */
html {
  scrollbar-width: none; /* For Firefox */
  -ms-overflow-style: none; /* For Internet Explorer and Edge */
}
html::-webkit-scrollbar {
  width: 0px; /* For Chrome, Safari, and Opera */
}
</style>

<script>
import HelloWorld from './components/ConfigurationPanel';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
