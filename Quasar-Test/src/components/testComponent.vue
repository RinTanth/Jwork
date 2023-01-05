<template>
  <q-select filled v-model="year" :options="options" label="Filled" @input="refreshData()"/>
  <!-- <q-btn :ripple="{ center: true }" color="red-10" label="button" @click="view_j_comps"/> -->
</template>

<script>
export default {
  props: {
    //Properties
    e_year: {
      required: false,
      type: Object, //should be object
    },
  },

  data() {
    return {
      options: [
        // { label: "ALL", value: "JMH" },
        { label: "JMB", value: "JMB" },
        { label: "JMH", value: "JMH" },
        { label: "JEL", value: "JMH" },
        { label: "JVC", value: "JVC" },
      ],

      year: {},
    };
  },

  mounted() {//get the year value back from test.vue page
    this.year = this.e_year;
  },

    methods: {
        refreshData() {
        // console.log('refreshData in testComponent.vue: ' + this.year)
        // console.log(this.year)
        this.$emit("eventRefreshData", this.year);//create event call refreshData and send the new year value to outside world
        },
    },
};
</script>

<style></style>
