<template>
  <q-page class="flex flex-center">
    <!-- <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    >
    <q-avatar color="green" text-color="white" icon="directions" />

     <q-input outlined v-model="text" label="Outlined" @input="func_test()" />

     <br>

     <q-input outlined v-model="text2" label="Outlined"  /> -->

    <div class="q-pa-md">
      <!-- <q-btn :ripple="{ center: true }" color="red-10" label="JAYMART" @click="view_j_comps"/>
      <br><br> -->
      <q-btn
        :loading="loading"
        color="red-10"
        @click="view_j_comps2"
        label="JAYMART"
      >
        <template v-slot:loading>
          <q-spinner-gears />
        </template>
      </q-btn>

      <br /><br />

      <q-table
        title="J Companies"
        :data="data"
        :columns="columns"
        row-key="name"
      />
    </div>

    <test-component
      :e_year="year"
      @eventRefreshData="refreshData2"
      :key="componentKey"
    />
    <!-- testComponent.vue using short close form and this must be attribute only-->
    <!-- event must use @ -->

    <q-btn
      :ripple="{ center: true }"
      color="blue-10"
      label="button"
      @click="eventTestYear"
    />
  </q-page>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import Closed from "../components/testComponent";
import testComponent from "src/components/testComponent.vue";

export default {
  components: { testComponent },
  name: "PageIndex",
  testComponent: {
    //make sure the name matched
    Closed,
  },

  data() {
    return {
      // Components
      text: "",
      text2: "",
      tvalue: [],
      loading: false,
      // loading,
      columns: [
        {
          name: "COMCODE",
          required: true,
          label: "CODE",
          align: "left",
          field: (row) => row.COMCODE,
          format: (val) => `${val}`,
          sortable: true,
        },
        {
          name: "COMPANY",
          label: "COMPANY",
          align: "center",
          field: "COMPANY",
        },
        { name: "index", label: "INDEX", field: "index" },
      ],
      data: [
        //placeholder value
        {
          COMCODE: "AAA",
          COMPANY: "aaaaaaaaaaaa",
          index: 0,
        },
        {
          COMCODE: "BB",
          COMPANY: "bbbbbbbbbbb",
          index: 1,
        },
        {
          COMCODE: "C",
          COMPANY: "ccccc",
          index: 2,
        },
      ],

      year: { label: "2021", value: 21 }, //for testComponent.vue
      componentKey: 0,
    };
  },

  methods: {
    // Similar to JS Functions

    simulateProgress(number) {
      // we set loading state
      this[`loading${number}`] = true;
      // simulate a delay
      setTimeout(() => {
        // we're done, we reset loading state
        this[`loading${number}`] = false;
      }, 3000);
    },

    async view_j_comps() {
      const postdata = {
        datasource: "JAYMART",
      };

      await axios.post(`${this.apiurl}/api/company`, postdata).then((res) => {
        this.data = res.data.data;
        // console.log(res.data)
      });
    },

    async view_j_comps2() {
      // we set loading state
      this[`loading`] = true;
      // simulate a delay
      setTimeout(() => {
        // we're done, we reset loading state
        this[`loading`] = false;
      }, 3000);

      const postdata = {
        datasource: "JAYMART",
      };

      await axios.post(`${this.apiurl}/api/company`, postdata).then((res) => {
        this.data = res.data.data;
        console.log(res.data);
      });
    },

    eventTestYear() {
      //testComponent.vue
      console.log(this.year);
    },

    refreshData2(data) {
      //testComponent.vue
      console.log("refreshdata2 data");
      console.log(data);
      this.year = data;
      this.componentKey = this.componentKey + 1;
    },
  },
};
</script>
