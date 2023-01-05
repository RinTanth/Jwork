<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    >
    <q-avatar color="green" text-color="white" icon="directions" />

     <q-input outlined v-model="text" label="Outlined" @input="func_test()" />

     <br>

     <q-input outlined v-model="text2" label="Outlined"  />

     {{text}} <!-- Direct Output -->
     {{text2}}

     <q-btn color="black" label="Black" @click="view_invoice_detail_ora"/>
     <div class="q-pa-md">
        <q-table
          title="J Companies"
          :data="data"
          :columns="columns"
          row-key="name"
        />
      </div>

  </q-page>
</template>

<script>

import Vue from 'vue'
import axios from 'axios'

export default {
  name: 'PageIndex',

  data () {
    return { // Components
      text: '',
      text2: '',
      tvalue: [],
      columns: [
        {
          name: 'COMCODE',
          required: true,
          label: 'CODE',
          align: 'left',
          field: row => row.COMCODE,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'COMPANY', label:'COMPANY', align: 'center', field: 'COMPANY'},
        { name: 'index', label: 'INDEX', field: 'index'}
      ],
      data: [
        {
          COMCODE: 'AAA',
          COMPANY: 'aaaaaaaaaaaa',
          index: 0
        },
        {
          COMCODE: 'BB',
          COMPANY: 'bbbbbbbbbbb',
          index: 1
        },
        {
          COMCODE: 'C',
          COMPANY: 'ccccc',
          index: 2
        }
      ]
    }
  },

  mounted() {

  },

  created() {

  },

  watch: { // Watch all the changing variables
    text(newval, oldval) {
    console.log(newval, oldval); 
    }
  },

  

  methods: { // Similar to JS Functions

    //or we can use
    //func_test(){}
    func_test: function () {
      this.text2 = this.text;
    },

    async view_invoice_detail_ora() {
      const postdata = {
        datasource: this.text,
      }

      await axios
        .post(`${this.apiurl}/api/company`, postdata)
        .then((res) => {
          this.tvalue = res.data.data
          console.log('----------------')
          console.log(this.tvalue)
          this.data = res.data.data
          
          console.log(res.data)
        })
    },
  }
}
</script>
