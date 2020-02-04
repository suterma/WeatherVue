import Vue from 'vue'
import App from './App.vue'
import VueMqtt from 'vue-mqtt'

//TODO Firefox can’t establish a connection to the server at ws://test.mosquitto.org/.
Vue.use(VueMqtt, 'ws://test.mosquitto.org:80', {clientId: 'WebClient-' + parseInt(Math.random() * 100000)})

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
