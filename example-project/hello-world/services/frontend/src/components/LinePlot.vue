<template>
  <div>
    <div style="height: 80vh">
      <div id='myLinePlot' style="height: inherit"></div>
    </div>
  </div>
</template>


<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "LinePlot",
  props: [
    "selectedCategory",
    "selectedBudget"
  ],
  data: () => ({
    LinePlotData: {x: [], y: [], type: []},
    AirbnbData: {x: [], y: [], name: [], cost: []}
  }),
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      // req URL to retrieve single company from backend
      var reqUrl = 'http://127.0.0.1:5000/attractions?type='+ this.$props.selectedCategory
      console.log("ReqURL " + reqUrl)
      // await response and data
      const response = await fetch(reqUrl)
      const responseData = await response.json();
      // transform data to usable by lineplot
      responseData.forEach((attr) => {
        this.LinePlotData.x.push(attr.longitude)
        this.LinePlotData.y.push(attr.latitude)
        this.LinePlotData.type.push(attr.type)
      })

      var reqUrl2 = 'http://127.0.0.1:5000/airbnbs'
      console.log("ReqURL " + reqUrl2)
      // await response and data
      const response2 = await fetch(reqUrl2)
      const responseData2 = await response2.json();
      // transform data to usable by lineplot
      responseData2.forEach((attr) => {
        this.AirbnbData.x.push(attr.longitude)
        this.AirbnbData.y.push(attr.latitude)
        this.AirbnbData.name.push(attr.name)
        this.AirbnbData.cost.push(attr.price)

      })
      // draw the lineplot after the data is transformed
      this.drawLinePlot()
    },
    drawLinePlot() {

      const types = new Set(this.LinePlotData.type)



      const airXTemp = this.AirbnbData.x
      const airYTemp= this.AirbnbData.y
      const airnameTemp = this.AirbnbData.name

      let airX = []
      let airY= []
      let airname= []


      const maxPrice = this.$props.selectedBudget

      this.AirbnbData.cost.map(function(cost, i){
        if(cost <= maxPrice){
          airX.push(airXTemp[i])
          airY.push(airYTemp[i])
          airname.push(airnameTemp[i])
        }
      })


      var trace2 = {
        name: "Airbnbs",
        lon: airX,
        lat: airY,
        text: airname,
        type: 'scattermapbox',

        marker: { color: this.calulateDistance(airX,airY), size: 5, colorscale: 'Jet' }
      }

      let traces = []


      traces.push(trace2)

      let tempType= this.LinePlotData.type
      let tempX= this.LinePlotData.x
      let tempY= this.LinePlotData.y

      types.forEach(function(t) {
        let xs = [];
        let ys = [];
        tempX.map(function(x,i) {
          if (tempType[i] === t){
            xs.push(tempX[i])
            ys.push(tempY[i])
          }
        });
        traces.push({
          lon: xs,
          lat: ys,
          name: t,
          type: 'scattermapbox',
          marker: { size: 10 }
        })
      })


      var layout = {
        mapbox: { style: "carto-positron", center: { lat: 47.374, lon: 8.536 }, zoom: 11 },
        margin: { r: 0, t: 0, b: 0, l: 0 }
      };
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myLinePlot', traces, layout, config);
    },

    calulateDistance(x,y){
      let result = []

      x.forEach(function(x,i){result.push(-Math.sqrt(Math.pow(x - 8.536477780554755,2)+Math.pow(y[i]-47.374806473560426,2)))})
      return result
    }
  }
}
</script>
