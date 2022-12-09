<template>
  <div>
    <h1>Top 10</h1>
    <ol>
      <li v-for="item in items" :key="item.id">
        {{ item.message }}
      </li>
    </ol>
  </div>
</template>
<script>
export default {
  name: "RankingView",
  data() {
    return {
      parentMessage: "Parent",
      items: [{ message: "Foo" }, { message: "Bar" }],
    };
  },
};
</script>
