<template>
  <div>
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
                <v-select
                    :items="categories.values"
                    label="Select a type of attraction"
                    dense
                    v-model="categories.selectedValue"
                    @change="changeCategory"
                ></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="12">
                <v-select
                    :items="budget.values"
                    label="Select a max budget"
                    dense
                    v-model="budget.selectedValue"
                    @change="changeCategory"
                ></v-select>
              </v-col>
            </v-row>

          </v-card>
        </v-col>
        <v-col cols="12" md="6" class="map">
          <LinePlot :key="linePlotId"
                    :selectedCategory="categories.selectedValue"
                    :selectedBudget="budget.selectedValue"
          />
        </v-col>

        <v-col cols="12" md="4" class="sideBar">
          <v-col cols="12" sm="12" class="scatter">
            <ScatterPlot :key="scatterPlotId"
                         :selectedCategory="categories.selectedValue"
                         :selectedBudget="budget.selectedValue"
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

export default {
  components: {LinePlot, ScatterPlot},
  data: () => ({
    scatterPlotId: 0,
    linePlotId: 0,
    categories: {
      values: ['All',
        'ArtGallery',
        'BodyOfWater',
        'Church',
        'CivicStructure',
        'MovieTheater',
        'Museum',
        'Park',
        'PerformingArtsTheater',
        'ShoppingCenter',
        'SportsActivityLocation',
        'TouristAttraction',
        'Zoo',
        'None'],
      selectedValue: 'None'
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
  height: calc(100vh - 50px);
}
</style>
