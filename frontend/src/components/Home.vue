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
export default {
  data() {
    return {
      search: ""
    };
  },
  methods: {
    submit() {
      console.log(this.search);
    }
  }
};
</script>

