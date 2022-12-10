<template>
  <div class="rankingPanel">
    <div class="rankingTitle">
      <span>
        <h3>Recommended Airbnbs</h3>
      </span>
    </div>
    <div v-for="airbnb in this.$props.topAirbnbs" :key="airbnb">
      <AirbnbRow :airbnbNames="airbnb" />
    </div>
  </div>
</template>

<script>
import AirbnbRow from "./AirbnbRow.vue";
export default {
  components: { AirbnbRow },
  name: "RankingView",
  props: ["topAirbnbs"],

  data: () => ({}),
  mounted() {},
  methods: {},
};
</script>
<style>
.rankingPanel {
  width: 90%;
  height: 40%;
  margin-left: 10px;
  justify-content: center;
}
.rankingTitle {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 5px;
  padding: 3px 5px;
}
</style>
