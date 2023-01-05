<template>
  <div id="q-app">
    <router-view />
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'

export default {
  name: 'App',

  methods: { // Similar to JS Functions
    async getYear() {
      const response = await axios.get(`${this.apiurl}/api/getyear`)
      return await response.data
    },

    async getProcess() {//one async can have many await
      await axios
        .post(`${this.apiurl}/api/appflow/app_process_pr_all`)
        .then((res) => {
          this.sel_processs = res.data
      })
    },

    async view_invoice_detail_ora() {
      const postdata = {
        datasource: this.text,
      }

      await axios
        .post(`${this.apiurl}/api/company`, postdata)
        .then((res) => {
          console.log(res.data)
        })
    },
  },

  mounted() {
    console.log(this.apiurl);
  },
}

</script>
