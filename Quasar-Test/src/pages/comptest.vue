<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <joption :e_comcode="comcode" @eventRefreshData="refreshData2" />
      <jtable :e_comcode="comcode" :key="componentKey" />
    </div>
  </q-page>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import jtable from "../components/jtable";
import joption from "../components/joption";

export default {
  components: { jtable, joption },

  data() {
    return {
      comcode: "JAYMART", // for both jtable and joption
      componentKey: 0, // for jtable
    };
  },
  //hi

  methods: {
    refreshData2(data) {
      this.comcode = data;
      this.componentKey = this.componentKey + 1;
    },
  },
};
</script>
