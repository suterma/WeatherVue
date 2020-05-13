# WeatherVue
 A simple, Raspberry Pi based weather station, that posts to a Vue.js app via MQTT. 
 
 ## Publish
 
The **publish** part is based on my other repository [WeatherPress](https://github.com/suterma/WeatherPress), which is described in detail in the corresponding [blog post](https://qrys.ch/a-raspberry-pi-based-weather-station-posting-to-wordpress/). The main difference is that the data is posted to a MQTT broker instead of a WordPress site.

### Output
Via configuration, the output can either be a text or a simple JSON object.

Example for Text: `21.408 °C 45.342 %rH`

Example for JSON:
~~~~
{
  "measurement": {
    # milliseconds since unix epoch
    "timestamp": 1589399663000,
    # a temperature value in degrees celsius
    "temperature": 22.3,
    # a humidity value in % rel. Humidity
    "relhumidity": 45.3
  }
}
~~~~

## Subscribe and Display

The subscribe and display part is done entirely in Vue.js, as a learning project. (Not yet implemented)

# Credits
 - [Vue.js](https://vuejs.org/): A Javascript framework, based on the MVVM principles (MIT License)
 - [Paho Python Client](https://github.com/eclipse/paho.mqtt.python), a MQTT Python Client (dual Eclipse License)
 - [Vue-Mqtt](https://github.com/nik-zp/vue-mqtt), an MQTT client for Vuejs2 (No License)
 - Additionally: See [WeatherPress](https://github.com/suterma/WeatherPress) (GPLv3 License)
