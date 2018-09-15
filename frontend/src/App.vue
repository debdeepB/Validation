<template>
  <v-app>
    <NavBar></NavBar>
    <v-content>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-content>
    <router-view/>
  </v-app>
</template>
<script>
import NavBar from "@/components/NavBar";
export default {
  components: {
    NavBar
  }
};
</script>