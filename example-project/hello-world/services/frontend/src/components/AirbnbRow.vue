<template>
  <div class="airbnbNames">
    <h4>{{ airbnbNames }}</h4>
  </div>
</template>
<script>
export default {
  name: "AirbnbRow",
  props: ["airbnbNames"],

  data: () => ({}),
  mounted() {},
  methods: {},
};
</script>
<style scoped>
.airbnbNames {
  background-color: #f4f4f4;
  margin: 5px;
  padding: 3px 5px;
  cursor: pointer;
}
.airbnbNames h4 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
