<template>
  <v-card
      flat
      color="transparent"
  >

    <v-card-text>
      <v-row>
        <v-col class="px-4">
          <v-range-slider
              v-model="range"
              :max="max"
              :min="min"
              hide-details
              class="align-center"
              @change="sendMessageToParent"
          >
            <template v-slot:prepend>
              <v-text-field
                  :value="range[0]"
                  class="mt-0 pt-0"
                  hide-details
                  single-line
                  type="number"
                  style="width: 60px"
                  @change="$set(range, 0, $event)"
              ></v-text-field>
            </template>
            <template v-slot:append>
              <v-text-field
                  :value="range[1]"
                  class="mt-0 pt-0"
                  hide-details
                  single-line
                  type="number"
                  style="width: 60px"
                  @change="$set(range, 1, $event)"
              ></v-text-field>
            </template>
          </v-range-slider>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "RangeSliderReview",
  props: [
    "selectedRoomType"
  ],
  data () {
    return {
      min: 0,
      max: 90,
      range: [0, 70],
    }
  },
  mounted() {
    this.fetchData()
  },

  methods: {
    async fetchData() {


      var reqUrl2 = 'http://127.0.0.1:5000/airbnbs?room_type='+ this.$props.selectedRoomType
      console.log("ReqURL " + reqUrl2)
      // await response and data
      const response2 = await fetch(reqUrl2)
      const responseData2 = await response2.json();
      // transform data to usable by lineplot
      let temp=[]
      responseData2.forEach((attr) => {
        temp.push(attr.number_of_reviews)
      })

      this.range=[Math.min(...temp),Math.max(...temp)]
      this.max=Math.max(...temp)
    },
    sendMessageToParent(){
      this.$emit('messageFromReview',this.range)
    }
  }
}
</script>