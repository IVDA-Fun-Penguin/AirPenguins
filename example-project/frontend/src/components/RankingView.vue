<template>
  <div>
    <h1>Top 10</h1>
    <ol>
      <li v-for="airbnb in selectedAirbnbs" :key="airbnb.id">
        {{ airbnb.name }}
      </li>
    </ol>
  </div>
</template>
<script>
export default {
  name: "RankingView",
  props: ["selectedAirbnbs"],
  data() {
    return {};
  },
};
</script>
