<template>
  <v-app>
    <div>
      <v-card>
        <v-container fluid>
          <v-row align="center">
            <v-col md="3">
              <LogoCard />
            </v-col>

            <v-col md="3">
              <BarChartPrice />
            </v-col>
            <v-col md="3">
              <BarChartReview />
            </v-col>
            <v-col md="3">
              <BarChartNights />
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </div>
    <v-main>
      <ConfigurationPanel />
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
import LogoCard from "@/components/LogoCard";

export default {
  name: "App",

  components: {
    ConfigurationPanel,
    BarChartPrice,
    BarChartReview,
    BarChartNights,
    LogoCard,
  },

  data: () => ({
    //
  }),
};
</script>
