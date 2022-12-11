<template>
  <div>
    <div>
      <v-card>
        <v-container fluid>

          <v-row align="center">

            <v-col md="2">
              <v-row>
                <v-col md="12">
                  <v-row align="center">
                    <!--<v-col><img src="../assets/pengu.png" style="height: 100px"></v-col>-->
                    <v-col>
                      <h1>AirPenguins</h1>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-col>



            <v-col  md="3" class="slider">
              Price:
              <RangeSliderPrice @messageFromPrice="captureMyPrice"
                                :selectedRoomType="categories.selectedValue"
                                :key="sliderID"/>
            </v-col>
            <v-col md="3" class="slider">
              Review:
              <RangeSliderReview @messageFromReview="captureMyReview"
                                 :selectedRoomType="categories.selectedValue"
                                 :key="sliderID"/>
            </v-col>
            <v-col md="3" class="slider">
              Min Nights:
              <RangeSliderNight @messageFromNight="captureMyNight"
                                :selectedRoomType="categories.selectedValue"
                                :key="sliderID"/>
            </v-col>

            <v-col md="1" >
              <v-select
                  :items="categories.values"
                  label="Select a type of room"
                  dense
                  v-model="categories.selectedValue"
                  @change="changeCategory"
              ></v-select>
            </v-col>

          </v-row>

        </v-container>
      </v-card>
    </div>
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="2" class="sideBar">
          <v-card class="pa-3">
            <v-row>
              <v-col cols="12" sm="12">
                <div class="control-panel-font">Attraction Overview</div>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="12">
                <Multiselect @messageFromChild="captureMyMessage"/>
              </v-col>
            </v-row>

          </v-card>
        </v-col>
        <v-col cols="12" md="6" class="sideBar">
          <LinePlot :key="linePlotId"
                    :selectedRoomType="categories.selectedValue"
                    :selectedBudget="budget.selectedValue"
                    :selected="selected"
                    :priceRange="priceRange"
                    :reviewRange="reviewRange"
                    :nightRange="nightRange"
          />
        </v-col>

        <v-col cols="12" md="4" class="sideBar">
          <v-col cols="12" sm="12" class="scatter">
            <ScatterPlot :key="scatterPlotId"
                         :selectedBudget="budget.selectedValue"
                         :selectedRoomType="categories.selectedValue"
            />
          </v-col>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import ScatterPlot from './ScatterPlot';
import LinePlot from './LinePlot';
import Multiselect from './Multiselect';
import RangeSliderPrice from './RangeSliderPrice';
import RangeSliderReview from './RangeSliderReview';

import RangeSliderNight from './RangeSliderNight';

export default {
  components: {LinePlot, ScatterPlot, Multiselect,RangeSliderPrice,RangeSliderReview, RangeSliderNight },
  data: () => ({
    scatterPlotId: 0,
    linePlotId: 0,
    sliderID:0,
    selected: [],
    priceRange:[0,1430],
    reviewRange:[0,930],
    nightRange:[0,360],
    categories: {
      values: ['All',
        'Entire home/apt',
        'Private room',
        'Shared room'],
      selectedValue: 'All'
    },
    budget: {
      values: [
        25,
        50,
        75,
        100,
        250,
        500,
        750,
        1000,
        1500
      ],
      selectedValue: 1500
    },
  }),
  methods: {
    changeCategory() {
      this.scatterPlotId += 1
      this.linePlotId += 1
      this.sliderID+=1
    },
    captureMyMessage(msg){
      this.selected=msg
      this.scatterPlotId += 1
      this.linePlotId += 1
      console.log(msg)
    },
    captureMyPrice(msg){
      this.priceRange=msg
      this.scatterPlotId += 1
      this.linePlotId += 1
      console.log(msg)
    },
    captureMyReview(msg){
      this.reviewRange=msg
      this.scatterPlotId += 1
      this.linePlotId += 1
      console.log(msg)
    },
    captureMyNight(msg){
      this.nightRange=msg
      this.scatterPlotId += 1
      this.linePlotId += 1
      console.log(msg)
    }
  }
}
</script>


<style scoped>
.control-panel-font {
  font-family: "Open Sans", verdana, arial, sans-serif;
  align-items: center;
  font-size: 15px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  display: flex;
  font-weight: 500;
  height: 40px;
}

.sideBar {
  border-right: 1px solid rgba(0, 0, 0, 0.1);
  background: #fafafa;
  padding-left: 17px;
  height: calc(85vh);
}
</style>
