# WeatherVue
 A simple, Raspberry Pi based weather station, that posts to a Vue.js app via MQTT. See my [blog post](https://qrys.ch/a-raspberry-pi-based-weather-station-publishing-to-an-mqtt-topic/) on how to install it.
 
 ## Publish
 
The **publish** part is based on my other repository [WeatherPress](https://github.com/suterma/WeatherPress), which is described in detail in the corresponding [blog post](https://qrys.ch/a-raspberry-pi-based-weather-station-posting-to-wordpress/) there. The main difference is that the data is posted to a MQTT broker instead of a WordPress site.

### Output
Via configuration, the output can either be a text or a simple JSON object.

Example for Text: `21.408 °C 45.342 %rH`

Example for JSON (minus comments):
~~~~
{
  "measurement": {
    "timestamp": 1589399663000,    // milliseconds since unix epoch
    "temperature": 22.3,    // a temperature value in degrees celsius
    "relhumidity": 45.3     // a humidity value in % rel. Humidity
  }
}
~~~~

## Subscribe and Display

The subscribe and display part is done, at least partially, in Vue.js, as a learning project. You can statically serve it from any web server. A live instance is available at https://weathervue.qrys.ch.

# Credits
 - [Vue.js](https://vuejs.org/): A Javascript framework, based on the MVVM principles (MIT License)
 - [Paho Python Client](https://github.com/eclipse/paho.mqtt.python), a MQTT Python Client (dual Eclipse License)
 - [mqtt.js](https://github.com/mqttjs/MQTT.js), an MQTT client in JavaScript (MIT License)
 - [Eclipse Mosquitto](https://mosquitto.org/), a free and open source MQTT broker
 - [Full screen clock](https://www.nayuki.io/page/full-screen-clock-javascript), a Full screen clock in JavaScript (no license specified)
 - Additionally: See [WeatherPress](https://github.com/suterma/WeatherPress) (GPLv3 License)
