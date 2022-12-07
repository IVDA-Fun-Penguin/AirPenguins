<template>
  <div>
    <div>
      <h1>Top 10</h1>
      <div class="pa-2 mb-4">
        <h3>1. {{ this.ScatterPlotData.name[1] }}</h3>

        <h3>2. {{ this.ScatterPlotData.name[2] }}</h3>

        <h3>3. {{ this.ScatterPlotData.name[3] }}</h3>

        <h4>4. {{ this.ScatterPlotData.name[4] }}</h4>
        <h4>5. {{ this.ScatterPlotData.name[5] }}</h4>
        <h5>6. {{ this.ScatterPlotData.name[6] }}</h5>
        <h5>7. {{ this.ScatterPlotData.name[7] }}</h5>
        <h5>8. {{ this.ScatterPlotData.name[8] }}</h5>
        <h5>9. {{ this.ScatterPlotData.name[9] }}</h5>

        <h5>10. {{ this.ScatterPlotData.name[10] }}</h5>
      </div>
    </div>
    <div style="height: 40vh">
      <div id="myScatterPlot" style="height: inherit" class="ma-4"></div>
    </div>
  </div>
</template>

<script>
import Plotly from "plotly.js/dist/plotly";
export default {
  name: "ScatterPlot",
  props: ["selectedCategory", "selectedBudget"],
  data: () => ({
    ScatterPlotData: {
      x: [],
      y: [],
      price: [],
      number_of_reviews: [],
      name: [],
    },
  }),
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      // req URL to retrieve companies from backend
      var reqUrl = "http://127.0.0.1:5000/airbnbs";
      console.log("ReqURL " + reqUrl);
      // await response and data
      const response = await fetch(reqUrl);
      const responseData = await response.json();

      // transform data to usable by scatterplot
      responseData.forEach((attr) => {
        this.ScatterPlotData.x.push(attr.longitude);
        this.ScatterPlotData.y.push(attr.latitude);
        this.ScatterPlotData.price.push(attr.price);
        this.ScatterPlotData.number_of_reviews.push(attr.number_of_reviews);
        this.ScatterPlotData.name.push(attr.name);
      });
      // after the data is loaded, draw the plot
      this.drawScatterPlot();
    },
    drawScatterPlot() {
      var myPlot = document.getElementById("myScatterPlot");

      const airXTemp = this.ScatterPlotData.x;
      const airYTemp = this.ScatterPlotData.y;
      const airnameTemp = this.ScatterPlotData.name;
      const airrewTemp = this.ScatterPlotData.number_of_reviews;

      let airX = [];
      let airY = [];
      let airname = [];
      let airrew = [];
      const maxPrice = this.$props.selectedBudget;

      const aircost = this.ScatterPlotData.price.filter(function (cost, i) {
        if (cost <= maxPrice) {
          airX.push(airXTemp[i]);
          airY.push(airYTemp[i]);
          airname.push(airnameTemp[i]);
          airrew.push(airrewTemp[i]);
          return cost;
        }
      });

      var trace = {
        y: aircost,
        x: this.calulateDistance(airX, airY),
        mode: "markers",
        type: "scatter",
        text: airname,
        marker: {
          size: 12,
        },
      };
      var data = [trace];
      var layout = {
        margin: { r: 0, t: 0, b: 0, l: 0 },
        xaxis: {
          title: "price",
          titlefont: {
            size: 12,
            color: "grey",
          },
        },
        yaxis: {
          title: "distance",
          titlefont: {
            size: 12,
            color: "grey",
          },
        },
      };
      var config = { responsive: true, displayModeBar: false };
      Plotly.newPlot("myScatterPlot", data, layout, config);

      myPlot.on("plotly_click", function (data) {
        var pts = "";
        for (var i = 0; i < data.points.length; i++) {
          pts =
            "x = " +
            data.points[i].x +
            "\ny = " +
            data.points[i].y.toPrecision(4) +
            "\n\n";
        }
        alert("Closest point clicked:\n\n" + pts);
      });
    },
    calulateDistance(x, y) {
      let result = [];

      x.forEach(function (x, i) {
        result.push(
          Math.sqrt(
            Math.pow(x - 8.536477780554755, 2) +
              Math.pow(y[i] - 47.374806473560426, 2)
          )
        );
      });
      return result;
    },
  },
};
</script>
