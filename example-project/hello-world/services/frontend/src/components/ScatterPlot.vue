<template>
  <div>
    <div style="height: 60vh">
      <div id='myScatterPlot' style="height: inherit"></div>
    </div>
  </div>
</template>


<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "ScatterPlot",
  props: [
    "selectedCategory",
      "selectedBudget"
  ],
  data: () => ({
    ScatterPlotData: {x: [], y: [], price: [], number_of_reviews: [], name: []}
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
        this.ScatterPlotData.name.push(attr.name)
      })
      // after the data is loaded, draw the plot
      this.drawScatterPlot()
    },
    drawScatterPlot() {

      const airXTemp = this.ScatterPlotData.x
      const airYTemp= this.ScatterPlotData.y
      const airnameTemp = this.ScatterPlotData.name
      const airrewTemp = this.ScatterPlotData.number_of_reviews

      let airX = []
      let airY= []
      let airname= []
      let airrew= []
      const maxPrice = this.$props.selectedBudget
      this.$props.selectedBudget=2
      const aircost = this.ScatterPlotData.price.filter(function(cost, i){
        if(cost<=maxPrice){
          airX.push(airXTemp[i])
          airY.push(airYTemp[i])
          airname.push(airnameTemp[i])
          airrew.push(airrewTemp[i])
          return cost
        }
      })



      var trace = {
        x: aircost,
        y: airrew,
        mode: 'markers',
        type: 'scatter',
        text: airname,
        marker: {
          color: aircost,
          size: 12,
          colorscale: 'Jet'
        }
      };
      var data = [trace];
      var layout = {
        xaxis: {
          title: 'price',
          titlefont: {
            size: 12,
            color: 'grey'
          },
        },
        yaxis: {
          title: 'number_of_reviews',
          titlefont: {
            size: 12,
            color: 'grey'
          },
        }
      }
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myScatterPlot', data, layout, config);
    }
  }
}
</script>
