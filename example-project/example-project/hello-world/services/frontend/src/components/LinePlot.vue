<template>
  <div>
    <v-row align="center" justify="center" class="mt-1 mb-0">
      <h3>Map of {{ $props.selectedCategory }} Attractions</h3>
    </v-row>
    <div style="height: 90vh">
      <div id='myLinePlot' style="height: inherit"></div>
    </div>
  </div>
</template>


<script>
import Plotly from 'plotly.js/dist/plotly';
export default {
  name: "LinePlot",
  props: [
      "selectedCategory"
  ],
  data: () => ({
    LinePlotData: {x: [], y: [], type: []},
    AirbnbData: {x: [], y: [], name: []}
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
      })
      // draw the lineplot after the data is transformed
      this.drawLinePlot()
    },
    drawLinePlot() {
      var trace1 = {
        name: "Attractions",
        lon: this.LinePlotData.x,
        lat: this.LinePlotData.y,
        text: this.LinePlotData.type,
        type: 'scattermapbox',
        marker: { color: "red", size: 10 }
      };
      var trace2 = {
        name: "Airbnbs",
        lon: this.AirbnbData.x,
        lat: this.AirbnbData.y,
        text: this.AirbnbData.name,
        type: 'scattermapbox',
        marker: { color: this.calulateDistance(this.AirbnbData.x,this.AirbnbData.y), size: 5 }
      };
      var data = [trace2, trace1]
      var layout = {
        mapbox: { style: "open-street-map", center: { lat: 47.374, lon: 8.536 }, zoom: 11 },
        margin: { r: 0, t: 0, b: 0, l: 0 }
      };
      var config = {responsive: true, displayModeBar: false}
      Plotly.newPlot('myLinePlot', data, layout, config);
    },
    calulateDistance(x,y){
      return Math.sqrt(Math.pow(x - 47.374806473560426,2)+Math.pow(y-8.536477780554755,2) )
    }
  }
}
</script>
