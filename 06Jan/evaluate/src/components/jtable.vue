<template>
  <div class="q-pa-md">
    <q-table
      title="SHOP LIST"
      :data="data"
      :columns="columns"
      row-key="SUBINV_CODE"
      :filter="filter"
    >
      <template v-slot:top-right>
        <q-input
          borderless
          dense
          debounce="300"
          v-model="filter"
          placeholder="Search"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>

      <template v-slot:body-cell-RM_PRS_NO="props">
        <q-td :props="props">
          <div>
            <q-badge color="purple" :label="props.value"></q-badge>
            <q-btn icon="info" @click.stop="btnclick" dense flat />
          </div>
        </q-td>
      </template>
    </q-table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    e_subinvCODE: {
      required: false,
      type: Number,
    },
  },

  data() {
    return {
      filter: "",

      columns: [
        {
          name: "RM_PRS_NO",
          required: true,
          label: "RM_PRS_NO",
          align: "left",
          field: (row) => row.RM_PRS_NO,
          format: (val) => `${val}`,
          sortable: true,
        },
        { name: "RM_NAME", label: "RM_NAME", field: "RM_NAME" },
        { name: "SUBINV_CODE", label: "SUBINV_CODE", field: "SUBINV_CODE" },
        { name: "AM_PRS_NO", label: "AM_PRS_NO", field: "AM_PRS_NO" },
        { name: "AM_NAME", label: "AM_NAME", field: "AM_NAME" },
        { name: "BRANCH_NAME", label: "BRANCH_NAME", field: "BRANCH_NAME" },
        { name: "MON", label: "MON", field: "MON" },
        { name: "TUE", label: "TUE", field: "TUE" },
        { name: "WEN", label: "WEN", field: "WEN" },
        { name: "THU", label: "THU", field: "THU" },
        { name: "FRI", label: "FRI", field: "FRI" },
        { name: "SAT", label: "SAT", field: "SAT" },
        { name: "SUN", label: "SUN", field: "SUN" },
        { name: "HOLIDAY", label: "HOLIDAY", field: "HOLIDAY" },
        {
          name: "SUBINV_STATUS",
          label: "SUBINV_STATUS",
          field: "SUBINV_STATUS",
        },
        { name: "REASON", label: "REASON", field: "REASON" },
      ],
      data: [
        //placeholder value
        {
          RM_PRS_NO: "AAA",
          RM_NAME: "AAA",
          SUBINV_CODE: "AAA",
          AM_PRS_NO: "AAA",
          AM_NAME: "AAA",
          BRANCH_NAME: "AAA",
          MON: "AAA",
          TUE: "AAA",
          WEN: "AAA",
          THU: "AAA",
          FRI: "AAA",
          SAT: "AAA",
          SUN: "AAA",
          HOLIDAY: "AAA",
          SUBINV_STATUS: "AAA",
          REASON: "AAA",
        },
        {
          RM_PRS_NO: "BBB",
          RM_NAME: "BBB",
          SUBINV_CODE: "BBB",
          AM_PRS_NO: "BBB",
          AM_NAME: "BBB",
          BRANCH_NAME: "BBB",
          MON: "BBB",
          TUE: "BBB",
          WEN: "BBB",
          THU: "BBB",
          FRI: "BBB",
          SAT: "BBB",
          SUN: "BBB",
          HOLIDAY: "BBB",
          SUBINV_STATUS: "BBB",
          REASON: "BBB",
        },
        {
          RM_PRS_NO: "CCC",
          RM_NAME: "CCC",
          SUBINV_CODE: "CCC",
          AM_PRS_NO: "CCC",
          AM_NAME: "CCC",
          BRANCH_NAME: "CCC",
          MON: "CCC",
          TUE: "CCC",
          WEN: "CCC",
          THU: "CCC",
          FRI: "CCC",
          SAT: "CCC",
          SUN: "CCC",
          HOLIDAY: "CCC",
          SUBINV_STATUS: "CCC",
          REASON: "CCC",
        },
      ],

      //   comcode: null,
    };
  },

  async mounted() {
    this.subinvCODE = await this.e_subinvCODE;
    await this.getJtable();
    console.log("mounted in jtable.vue");
    console.log(this.subinvCODE);
  },

  methods: {
    async getJtable() {
      console.log("getJtable in jtable.vue");
      var postdata = {
        selectedSUBINV: this.subinvCODE,
      };

      console.log(this.apiurl);

      await axios.post(`${this.apiurl}/api/getsubinv`, postdata).then((res) => {
        this.data = res.data.data;
      });
    },
  },
};
</script>

<style></style>
