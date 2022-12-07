<template>
  <div>
    <treeselect
      v-model="value"
      :multiple="true"
      :options="options"
      :value-consists-of="valueConsistsOf"
      @close="sendMessageToParent"
    />
  </div>
</template>

<script>
// import the component
import Treeselect from "@riophae/vue-treeselect";
// import the styles
import "@riophae/vue-treeselect/dist/vue-treeselect.css";

export default {
  // register the component
  name: "MultiSelect",
  components: { Treeselect },
  data() {
    return {
      // define the default value
      value: null,
      // define options
      valueConsistsOf: "LEAF_PRIORITY",
      options: [],
      Attractions: { type: [], name: [] },
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      var reqUrl = "http://127.0.0.1:5000/attractions?type=All";
      console.log("ReqURL " + reqUrl);

      const response = await fetch(reqUrl);
      const responseData = await response.json();

      responseData.forEach((attr) => {
        this.Attractions.type.push(attr.type);
        this.Attractions.name.push(attr.name);
      });

      const types = new Set(this.Attractions.type);

      let tempType = this.Attractions.type;
      let tempName = this.Attractions.name;
      let categories = [];
      types.forEach(function (t) {
        let category = { id: t, label: t, children: [] };
        tempName.map(function (x, i) {
          if (tempType[i] === t) {
            category.children.push({ id: x, label: x });
          }
        });
        categories.push(category);
      });
      categories.forEach((x) => this.options.push(x));
    },
    sendMessageToParent() {
      this.$emit("messageFromChild", this.value);
    },
  },
};
</script>
