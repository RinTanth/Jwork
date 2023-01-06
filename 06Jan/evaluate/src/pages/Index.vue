<template>
  <q-page class="flex flex-center">
    <shop-filter-component :e_com="comcode" :key="componentKey">
    </shop-filter-component>
  </q-page>
</template>

<script>
import shopFilterComponent from "../components/shopFilterComponent.vue";
export default {
  components: { shopFilterComponent },
  name: "PageIndex",
};
</script>
