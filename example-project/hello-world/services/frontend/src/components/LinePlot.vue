<template>
  <div>
    <div style="height: 80vh">
      <div id="myLinePlot" style="height: inherit"></div>
    </div>
  </div>
</template>

<script>
import Plotly from "plotly.js/dist/plotly";
export default {
  name: "LinePlot",
  props: ["selectedCategory", "selectedBudget", "selected", "lassoAirbnbs"],
  data: () => ({
    TopAirbnbNames: [],
    AttractionData: { x: [], y: [], type: [], name: [] },
    AirbnbData: { x: [], y: [], name: [], cost: [], color: [], rank: [] },
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
      // transform data to usable by lineplot
      responseData.forEach((attr) => {
        this.AttractionData.x.push(attr.longitude);
        this.AttractionData.y.push(attr.latitude);
        this.AttractionData.type.push(attr.type);
        this.AttractionData.name.push(attr.name);
      });

      var reqUrl2 = "http://127.0.0.1:5000/airbnbs";
      console.log("ReqURL " + reqUrl2);
      // await response and data
      const response2 = await fetch(reqUrl2);
      const responseData2 = await response2.json();
      // transform data to usable by lineplot
      responseData2.forEach((attr) => {
        this.AirbnbData.x.push(attr.longitude);
        this.AirbnbData.y.push(attr.latitude);
        this.AirbnbData.name.push(attr.name);
        this.AirbnbData.cost.push(attr.price);
      });
      // draw the lineplot after the data is transformed
      this.calculateMiddlePoint();
      this.drawLinePlot();
      this.passTopAirbnbs();
    },
    calculateMiddlePoint() {
      let resultx = 0;
      let resulty = 0;
      let tempX = this.AttractionData.x;
      let tempY = this.AttractionData.y;
      let tempName = this.AttractionData.name;
      let tempType = this.AttractionData.type;
      const types = new Set(this.AttractionData.type);

      let tempInc = this.$props.selected;

      let numberOfAttractionSelected = 0;

      if (this.$props.selected.length !== 0) {
        // calculate for each explicit attraction
        tempName.forEach(function (x, i) {
          if (tempInc.includes(x)) {
            resultx += tempX[i];
            resulty += tempY[i];
            numberOfAttractionSelected += 1;
          }
        });

        // calculate for each category of attraction
        tempInc.forEach(function (x) {
          if (types.has(x)) {
            tempX.forEach(function (_, i) {
              if (tempType[i] === x) {
                resultx += tempX[i];
                resulty += tempY[i];
                numberOfAttractionSelected += 1;
              }
            });
          }
        });

        this.MiddlePoint.x = resultx / numberOfAttractionSelected;
        this.MiddlePoint.y = resulty / numberOfAttractionSelected;
      } else {
        // calculate for all attractions when none of them are selected
        this.AttractionData.x.map((x) => (resultx += x));
        this.AttractionData.y.map((y) => (resulty += y));

        this.MiddlePoint.x = resultx / this.AttractionData.x.length;
        this.MiddlePoint.y = resulty / this.AttractionData.y.length;
      }

      //console.log(this.$props.selected);
      this.passMidPoint();
    },
    drawLinePlot() {
      let traces = [];

      const types = new Set(this.AttractionData.type);
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

        marker: { color: "rgb(15,255,0)", size: 5 },
      };
      traces.push(traceMiddlePoint);

      let tempType = this.AttractionData.type;
      let tempX = this.AttractionData.x;
      let tempY = this.AttractionData.y;
      let tempName = this.AttractionData.name;
      let selected = this.$props.selected;
      let self = this;
      types.forEach(function (category) {
        let xs = [];
        let ys = [];
        let name = [];
        tempX.map(function (x, i) {
          if (tempType[i] === category) {
            xs.push(tempX[i]);
            ys.push(tempY[i]);
            name.push(tempName[i]);
          }
        });

        traces.push({
          lon: xs,
          lat: ys,
          name: category,
          type: "scattermapbox",
          marker: {
            size: 10,
            color:
              selected === []
                ? "rgba(114,114,114,0.42)"
                : self.checkIfIn(name, selected, category),
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
      Plotly.newPlot("myLinePlot", traces, layout, config);
    },
    checkIfIn(name, list, category) {
      let res = [];
      if (list.includes(category)) {
        res = Array(name.length).fill("#ffcc00");
      } else {
        name.forEach(function (x) {
          if (list.includes(x)) {
            res.push("#ffcc00");
          } else {
            res.push("rgba(114,114,114,0.42)");
          }
        });
      }
      return res;
    },
    compareNumbers(a, b) {
      return a - b;
    },
    rankings(arr) {
      const sorted = [...arr].sort((a, b) => a - b);
      return arr.map((x) => sorted.indexOf(x) + 1);
    },
    calulateDistance(AirbnbLat, AirbnbLong) {
      let result = [];

      const tempX = this.MiddlePoint.x;
      const tempY = this.MiddlePoint.y;
      console.log("Midpoint 11111111111", tempX, tempY);

      AirbnbLat.forEach(function (_, i) {
        result.push(
          Math.sqrt(
            Math.pow(AirbnbLat[i] - tempX, 2) +
              Math.pow(AirbnbLong[i] - tempY, 2)
          )
        );
      });

      const filter = 10;
      const temp = [...result];
      const distNotSorted = [...result];
      const flag = temp.sort(this.compareNumbers)[filter];

      let t = [...result];
      this.AirbnbData.rank = this.rankings(t);

      result = result.map(function (x) {
        return x <= flag ? "#ff0000" : "rgba(114,114,114,0.25)";
      });

      let color = [...result];

      const Lassoedx = this.$props.lassoAirbnbs.x;
      console.log(Lassoedx, temp);

      distNotSorted.forEach(function (_, i) {
        if (Lassoedx.includes(temp[i])) {
          console.log(distNotSorted[i], "changed color");
          color[i] = "rgba(20,205,200,1)";
        }
      });

      this.AirbnbData.color = color;

      return color;
    },
    passMidPoint() {
      this.$emit("passMidPoint", this.MiddlePoint);
    },

    passTopAirbnbs() {
      const airnameTemp = this.AirbnbData.name;
      let topNames = [];

      this.AirbnbData.rank.forEach(function (rank, index) {
        if (rank <= 10) {
          topNames.push(airnameTemp[index]);
        }
      });
      this.TopAirbnbNames = topNames;
      this.$emit("passTopNames", this.TopAirbnbNames);
    },
  },
};
</script>
