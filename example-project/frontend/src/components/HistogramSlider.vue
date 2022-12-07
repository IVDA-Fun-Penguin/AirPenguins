<template>
  <div>
    <histogramSlider
      style="margin: 200px auto"
      :width="600"
      :bar-height="100"
      :bar-width="31"
      :data="data"
      :prettify="prettify"
      :drag-interval="true"
      :force-edges="false"
      :colors="['#4facfe', '#00f2fe']"
      :min="5"
      :max="40"
    />
  </div>
</template>

<script>
import HistogramSlider from "vue-histogram-slider";
import "vue-histogram-slider/dist/histogram-slider.css";

export default {
  name: "HistogramSlider",
  components: { HistogramSlider },
  data() {
    return {
      data: [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 20, 30, 30, 40, 40, 40],
      prettify: (point) => {
        console.log(this.data.length);
        return point;
      },
    };
  },
};
</script>
