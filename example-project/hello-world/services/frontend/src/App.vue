<template>
  <v-app>

    <v-main>
      <ConfigurationPanel/>
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

.slider {
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  box-shadow: #1b1b1b;
  background: #fafafa;
  padding-left: 17px;
}
</style>

<script>
import ConfigurationPanel from "@/components/ConfigurationPanel";
export default {
  name: 'App',

  components: {
    ConfigurationPanel,

  },

  data: () => ({
    //
  }),
};
</script>
