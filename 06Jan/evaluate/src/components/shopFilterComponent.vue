<template>
  <div class="row">
    <q-select
      filled
      v-model="branchCode"
      :options="options"
      label="Filled"
      @input="sendData()"
    />
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    e_branchCode: {
      required: false,
      type: Number,
    },
  },

  data() {
    return {
      options: [],
      branchCode: [],
    };
  },

  async mounted() {
    this.options = await this.getMaster();
  },

  methods: {
    sendData() {
      this.$emit("eventSendData", this.branchCode);
    },

    async getMaster() {
      const response = await axios.get(`${this.apiurl}/api/branch_master`);
      return await response.data;
    },
  },
};
</script>

<style></style>
