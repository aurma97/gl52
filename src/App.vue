<template>
  <div id="app">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.materialdesignicons.com/2.5.94/css/materialdesignicons.min.css">
    <app-header></app-header>
    
    <router-view></router-view>
  </div>
</template>

<script>
import Header from './components/headfoot/Header.vue'
export default {
  components:{
    'app-header': Header
  }
}
</script>

<style>
@import "~@fortawesome/fontawesome-free/css/all.css";
@import "~bulma/css/bulma.css";
</style>
