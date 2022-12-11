<template>
  <div>
    <div class="scatterPanel">
      <div id="myScatterPlot" style="height: inherit" class="ma-4"></div>
    </div>
  </div>
</template>

<script>
import Plotly from "plotly.js/dist/plotly";
export default {
  name: "ScatterPlot",
  props: ["selectedCategory", "selectedBudget", "midPoint","selectedRoomType"],
  data: () => ({
    ScatterPlotData: {
      x: [],
      y: [],
      price: [],
      number_of_reviews: [],
      name: [],
    },
    LassoedAirbnbs: { x: [], y: [] },
    MiddlePoint: { x: 0, y: 0 },
  }),
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      // req URL to retrieve companies from backend
      var reqUrl = 'http://127.0.0.1:5000/airbnbs?room_type='+ this.$props.selectedRoomType
      console.log('ReqURL ' + reqUrl)
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

      const priceInCost = this.ScatterPlotData.price.filter(function (cost, i) {
        if (cost <= maxPrice) {
          airX.push(airXTemp[i]);
          airY.push(airYTemp[i]);
          airname.push(airnameTemp[i]);
          airrew.push(airrewTemp[i]);
          return cost;
        }
      });

      var trace = {
        y: priceInCost,
        x: this.calulateDistance(airX, airY),
        mode: "markers",
        type: "scatter",
        text: airname,
        marker: {
          size: 8,
        },
      };
      var data = [trace];
      var layout = {
        margin: { r: 0, t: 0, b: 0, l: 0 },
        xaxis: {
          title: "distance",
          titlefont: {
            size: 12,
            color: "grey",
          },
        },
        yaxis: {
          title: "price",
          titlefont: {
            size: 12,
            color: "grey",
          },
        },
      };
      var config = {
        responsive: false,
        displayModeBar: true,
      };
      Plotly.newPlot("myScatterPlot", data, layout, config);

      myPlot.on("plotly_click", function (data) {
        var alertMsg = "";
        for (var i = 0; i < data.points.length; i++) {
          alertMsg =
            "Distance to center is " +
            data.points[i].x.toPrecision(4) +
            "\nPrice is $" +
            data.points[i].y +
            "\n\n";
        }
        alert("Closest Airbnb clicked:\n\n" + alertMsg);
      });

      myPlot.on("plotly_selected", (eventData) => {
        var lassox = [];
        var lassoy = [];
        if (eventData.points) {
          eventData.points.forEach(function (pt) {
            lassox.push(pt.x);
            lassoy.push(pt.y);
          });
        } else {
          console.log("point not found");
        }
        this.LassoedAirbnbs.x = lassox;
        this.LassoedAirbnbs.y = lassoy;
        this.passLassoAirbnbs();
      });
    },

    calulateDistance(x, y) {
      let result = [];
      this.MiddlePoint.x = this.$props.midPoint.x;
      this.MiddlePoint.y = this.$props.midPoint.y;

      const tempX = this.MiddlePoint.x;
      const tempY = this.MiddlePoint.y;
      console.log("Midpoint 222222222", tempX, tempY);

      x.forEach(function (x, i) {
        result.push(
          Math.sqrt(Math.pow(x - tempX, 2) + Math.pow(y[i] - tempY, 2))
        );
      });
      return result;
    },

    passLassoAirbnbs() {
      this.$emit("passLasso", this.LassoedAirbnbs);
    },
  },
};
</script>
<style scoped>
.scatterPanel {
  height: 40vh;
  width: 30rem;
}
</style>
