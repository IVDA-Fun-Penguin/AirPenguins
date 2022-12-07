<template>
  <div>
    <div style="height: 10vh" >
      <div id='myBarChartNight' style="height: inherit" ></div>
    </div>
  </div>
</template>


<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "BarChartNight",
  props: [
    "selectedCategory",
      "selectedBudget"
  ],
  data: () => ({
    AirbnbData: {minimum_nights: []}
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {

      var reqUrl2 = 'http://127.0.0.1:5000/airbnbs'
      console.log("ReqURL " + reqUrl2)
      // await response and data
      const response2 = await fetch(reqUrl2)
      const responseData2 = await response2.json();
      // transform data to usable by lineplot
      responseData2.forEach((attr) => {
        this.AirbnbData.minimum_nights.push(attr.minimum_nights)

      })

      this.drawScatterPlot()
    },
    compareNumbers(a, b) {
      return a - b;
    },
    drawScatterPlot() {

      let array = this.AirbnbData.minimum_nights
      let interval = 10
      let intervals = []
      let temp = array.reduce(function (r, a) {
        var slot = Math.floor((a - 1) / interval);
        intervals.push(interval);
        (r[slot] = r[slot] || []).push(a);
        return r;
      }, []);

      let result = []
      temp.map(function (x){ result.push(x.length)})

      var data = [
        {
          y: result,

          width: 1,
          type: 'bar'
        }
      ];
      var layout = {
        margin: { r: 0, t: 0, b: 0, l: 0 },

      }
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myBarChartNight', data, layout, config);
    }
  }
}
</script>
