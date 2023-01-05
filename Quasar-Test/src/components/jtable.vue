<template>
  <div class="q-pa-md">
    <q-table
      title="J Companies"
      :data="data"
      :columns="columns"
      row-key="index"
    />
  </div>
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

      comcode: null,
    };
  },

  async mounted() {
    this.comcode = await this.e_comcode;
    await this.getJtable();
  },

  methods: {
    async getJtable() {
      var postdata = {
        datasource: this.comcode,
      };

      await axios
        .post(`${this.apiurl}/api/company_sub`, postdata)
        .then((res) => {
          this.data = res.data.data;
        });
    },
  },
};
</script>

<style></style>
