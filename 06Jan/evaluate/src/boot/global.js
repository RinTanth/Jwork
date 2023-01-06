//to declair apiurl
//simply change the url from here if needed

import Vue from "vue";

Vue.mixin({
  data: function () {
    return {
      apiurl: "http://127.0.0.1:9999",
    };
  },
});
