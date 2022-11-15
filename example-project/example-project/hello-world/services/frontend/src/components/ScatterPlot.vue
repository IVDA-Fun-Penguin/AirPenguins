<template>
  <div>
    <v-row align="center" justify="center" class="mt-1 mb-0">
      <h3>Overview of {{ $props.selectedCategory }} Attractions</h3>
    </v-row>
    <div style="height: 90vh">
      <div id='myScatterPlot' style="height: inherit"></div>
    </div>
  </div>
</template>


<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "ScatterPlot",
  props: [
    "selectedCategory"
  ],
  data: () => ({
    ScatterPlotData: {x: [], y: [], price: [], number_of_reviews: []},
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      // req URL to retrieve companies from backend
      var reqUrl = 'http://127.0.0.1:5000/airbnbs'
      console.log('ReqURL ' + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();

      // transform data to usable by scatterplot
      responseData.forEach((attr) => {
        this.ScatterPlotData.x.push(attr.longitude)
        this.ScatterPlotData.y.push(attr.latitude)
        this.ScatterPlotData.price.push(attr.price)
        this.ScatterPlotData.number_of_reviews.push(attr.number_of_reviews)
      })
      // after the data is loaded, draw the plot
      this.drawScatterPlot()
    },
    drawScatterPlot() {
      var trace1 = {
        x: this.ScatterPlotData.price,
        y: this.ScatterPlotData.number_of_reviews,
        mode: 'markers',
        type: 'scatter',
        text: this.ScatterPlotData.name,
        marker: {
          color: 'black',
          size: 12
        }
      };
      var data = [trace1];
      var layout = {
        xaxis: {
          title: 'price'
        },
        yaxis: {
          title: 'number_of_reviews'
        }
      }
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myScatterPlot', data, layout, config);
    }
  }
}
</script>
