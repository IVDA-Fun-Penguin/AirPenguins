<template>
  <div>
    <div style="height: 80vh">
      <div id="myGeoPlot" style="height: inherit"></div>
    </div>
  </div>
</template>

<script>
import Plotly from "plotly.js/dist/plotly";
export default {
  name: "GeoPlot",
  props: ["selectedCategory", "selectedBudget", "selected"],
  data: () => ({
    GeoPlotData: { x: [], y: [], type: [], name: [] },
    AirbnbData: { x: [], y: [], name: [], cost: [] },
    MiddlePoint: { x: 0, y: 0 },
  }),
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      // req URL to retrieve single company from backend
      var reqUrl =
        "http://127.0.0.1:5000/attractions?type=" +
        this.$props.selectedCategory;
      console.log("ReqURL " + reqUrl);
      // await response and data
      const response = await fetch(reqUrl);
      const responseData = await response.json();
      // transform data to usable by Geoplot
      responseData.forEach((attr) => {
        this.GeoPlotData.x.push(attr.longitude);
        this.GeoPlotData.y.push(attr.latitude);
        this.GeoPlotData.type.push(attr.type);
        this.GeoPlotData.name.push(attr.name);
      });

      var reqUrl2 = "http://127.0.0.1:5000/airbnbs";
      console.log("ReqURL " + reqUrl2);
      // await response and data
      const response2 = await fetch(reqUrl2);
      const responseData2 = await response2.json();
      // transform data to usable by Geoplot
      responseData2.forEach((attr) => {
        this.AirbnbData.x.push(attr.longitude);
        this.AirbnbData.y.push(attr.latitude);
        this.AirbnbData.name.push(attr.name);
        this.AirbnbData.cost.push(attr.price);
      });
      // draw the Geoplot after the data is transformed
      this.calculateMiddlePoint();
      this.drawGeoPlot();
    },
    calculateMiddlePoint() {
      let resultx = 0;
      let resulty = 0;

      this.GeoPlotData.x.map((x) => (resultx += x));
      this.GeoPlotData.y.map((y) => (resulty += y));

      this.MiddlePoint.x = resultx / this.GeoPlotData.x.length;
      this.MiddlePoint.y = resulty / this.GeoPlotData.y.length;
    },
    drawGeoPlot() {
      let traces = [];

      const types = new Set(this.GeoPlotData.type);
      const airXTemp = this.AirbnbData.x;
      const airYTemp = this.AirbnbData.y;
      const airnameTemp = this.AirbnbData.name;

      let airX = [];
      let airY = [];
      let airname = [];

      const maxPrice = this.$props.selectedBudget;

      this.AirbnbData.cost.map(function (cost, i) {
        if (cost <= maxPrice) {
          airX.push(airXTemp[i]);
          airY.push(airYTemp[i]);
          airname.push(airnameTemp[i]);
        }
      });

      var trace2 = {
        name: "Airbnbs",
        lon: airX,
        lat: airY,
        text: airname,
        type: "scattermapbox",

        marker: { color: this.calulateDistance(airX, airY), size: 5 },
      };
      traces.push(trace2);

      var traceMiddlePoint = {
        name: "MiddlePoint",
        lon: [this.MiddlePoint.x],
        lat: [this.MiddlePoint.y],
        type: "scattermapbox",

        marker: { color: "rgba(17,255,0,0.37)", size: 100 },
      };
      traces.push(traceMiddlePoint);

      let tempType = this.GeoPlotData.type;
      let tempX = this.GeoPlotData.x;
      let tempY = this.GeoPlotData.y;
      let tempName = this.GeoPlotData.name;
      let selected = this.$props.selected;
      let self = this;
      types.forEach(function (t) {
        let xs = [];
        let ys = [];
        let name = [];
        tempX.map(function (x, i) {
          if (tempType[i] === t) {
            xs.push(tempX[i]);
            ys.push(tempY[i]);
            name.push(tempName[i]);
          }
        });

        traces.push({
          lon: xs,
          lat: ys,
          name: t,
          type: "scattermapbox",
          marker: {
            size: 10,
            color: selected === [] ? "#727272" : self.checkIfIn(name, selected),
          },
        });
      });

      var layout = {
        mapbox: {
          style: "carto-positron",
          center: { lat: 47.374, lon: 8.536 },
          zoom: 11,
        },
        margin: { r: 0, t: 0, b: 0, l: 0 },
      };
      var config = { responsive: true, displayModeBar: false };
      Plotly.newPlot("myGeoPlot", traces, layout, config);
    },
    checkIfIn(name, list) {
      let res = [];
      name.forEach(function (x) {
        if (list.includes(x)) {
          res.push("#ffcc00");
        } else {
          res.push("#727272");
        }
      });
      return res;
    },
    compareNumbers(a, b) {
      return a - b;
    },
    calulateDistance(x, y) {
      let result = [];

      const tempX = this.MiddlePoint.x;
      const tempY = this.MiddlePoint.y;
      x.forEach(function (x, i) {
        result.push(
          Math.sqrt(Math.pow(x - tempX, 2) + Math.pow(y[i] - tempY, 2))
        );
      });

      const filter = 100;
      const temp = [...result];
      const flag = temp.sort(this.compareNumbers)[filter];
      result = result.map(function (x) {
        return x <= flag ? "#ff0000" : "#727272";
      });
      return result;
    },
  },
};
</script>
