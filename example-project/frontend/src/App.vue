<template>
  <v-app>
    <div>
      <v-card>
        <v-container fluid>

          <v-row align="center">

            <v-col md="3">
              <v-row>
                <v-col md="12">
                  <v-row align="center">
                    <v-col><img src="./assets/pengu.png" style="height: 100px"></v-col>
                    <v-col>
                      <h1>AirPenguins</h1>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-col>



            <v-col md="3">
              Price:
              <BarChartPrice/>
            </v-col>
            <v-col md="3">
              Review:
              <BarChartReview/>
            </v-col>
            <v-col md="3">
              Min Nights:
              <BarChartNights/>
            </v-col>

          </v-row>

        </v-container>
      </v-card>
    </div>
    <v-main>
      <ConfigurationPanel/>
    </v-main>
  </v-app>
</template>

<style>
/* disable scrolling */
html {
  scrollbar-width: none; /* For Firefox */
  -ms-overflow-style: none; /* For Internet Explorer and Edge */
}

html::-webkit-scrollbar {
  width: 0px; /* For Chrome, Safari, and Opera */
}


</style>

<script>
import ConfigurationPanel from "@/components/ConfigurationPanel";
import BarChartPrice from "@/components/BarchartPrice";
import BarChartReview from "@/components/BarchartReview";
import BarChartNights from "@/components/BarchartNights";

export default {
  name: 'App',

  components: {
    ConfigurationPanel,
    BarChartPrice,
    BarChartReview,
    BarChartNights
  },

  data: () => ({
    //
  }),
};
</script>
