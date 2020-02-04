<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <sub1></sub1>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Sub1 from './components/Sub1'

export default {
  name: 'app',
  components: {
    HelloWorld,
    Sub1
  },
  mounted () {
    this.$mqtt.subscribe('testtopic/1')
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.sub {
  width: 31%;
  float: left;
  border: 1px solid #ccc;
  margin: 20px 1%;
  padding: 20px 0;
}
button {
  padding: 10px 20px;
}
</style>
