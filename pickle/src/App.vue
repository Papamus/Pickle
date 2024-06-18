<template>
  <div id="app">
    <PickleTimer />
  </div>
</template>

<script>
import PickleTimer from './components/PickleTimer.vue'

export default {
  name: 'App',
  components: {
    PickleTimer
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
