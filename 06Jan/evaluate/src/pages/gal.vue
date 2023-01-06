<template>
  <div class="row">
    <q-input filled v-model="subinvCODE0" label="enter number" type="number" />
    <q-btn round color="brown-5" icon="directions" @click="refreshData()" />
    <jtable :e_subinvCODE="subinvCODE" :key="componentKey" />
  </div>
</template>

<script>
// import axios from "axios";
import jtable from "../components/jtable";

export default {
  components: { jtable },
  data() {
    return {
      subinvCODE0: "",
      subinvCODE: 0,
      galdemostring: "",
      galdemo: "",
      componentKey: 0, // for jtable
    };
  },

  methods: {
    sendData() {
      this.$emit("eventSendData", this.subinvCODE);
      console.log("pressed button");
      console.log("pressed subinvCODE: " + this.subinvCODE);
    },
    refreshData() {
      //   this.subinvCODE = data;
      this.subinvCODE = Number(this.subinvCODE0);
      console.log("pressed button refreshData");
      this.componentKey = this.componentKey + 1;
      console.log("componentKey updated");

      this.galdemo = this.galdemostring;
      console.log("galdemostring: " + this.galdemostring);
      console.log(this.galdemo);
    },
  },
};
</script>

<style></style>
