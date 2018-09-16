<template>
  <div class="home">
    <v-text-field
      v-model="search"
      append-icon="search"
      label="Search"
      single-line
      v-on:keyup.13="submit"
    ></v-text-field>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      search: ""
    };
  },
  methods: {
    submit() {
      this.fetchSearchResults();
    },

    async fetchSearchResults() {
      console.log({
        query: this.search
      });
      var qs = require("qs");
      const { data } = await axios.post(
        "http://localhost:8002/search/",
        qs.stringify({
          query: this.search
        })
      );
      console.log(data);
    }
  }
};
</script>

