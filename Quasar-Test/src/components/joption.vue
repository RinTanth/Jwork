<template>
  <q-select
    filled
    v-model="comcode"
    :options="options"
    label="Filled"
    @input="refreshData()"
  />
</template>

<script>
import axios from "axios";
export default {
  props: {
    e_comcode: {
      required: false,
      type: String,
    },
  },

  data() {
    return {
      options: [],
      comcode: null,
    };
  },

  async mounted() {
    //get the comcode value back from comptest.vue page
    this.comcode = this.e_comcode;
    let a = await this.getMasterDS();
    this.options = a;
  },

  methods: {
    refreshData() {
      this.$emit("eventRefreshData", this.comcode); //create event call refreshData and send the new year value to outside world
    },

    async getMasterDS() {
      const response = await axios.get(`${this.apiurl}/api/company_master`);
      return await response.data;
    },
  },
};
</script>

<style></style>
