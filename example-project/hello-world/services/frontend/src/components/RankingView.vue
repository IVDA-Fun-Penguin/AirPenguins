<template>
  <div>
    <ol>
      <li v-for="airbnb in this.$props.topAirbnbs" :key="airbnb.id">
        name:{{ airbnb }}
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: "RankingView",
  props: ["topAirbnbs"],

  data: () => ({}),
  mounted() {},
  methods: {},
};
</script>
