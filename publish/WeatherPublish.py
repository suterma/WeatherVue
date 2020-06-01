# WeatherVue - A simple, Raspberry Pi based weather station, that posts
# to an MQTT topic.
# ------------------------------------------------------------------------------

import time
import Si7021
import pigpio

pi = pigpio.pi()
s = Si7021.sensor(pi)

# set the resolution
# 0 denotes the maxium available: Humidity 12 bits, Temperature 14 bits
# See the documentation for more details
s.set_resolution(0)

# get the environment data
temperature = s.temperature()
humidity = s.humidity()

print("{:.3f} °C".format(temperature) + " | {:.3f} %rH".format(humidity))

s.cancel()
pi.stop()

# Post the data to an MQTT topic
import paho.mqtt.publish as publish

print('preparing message publication...')

import yaml
with open("WeatherPublish.config.yml", "r") as configFile:
    config = yaml.safe_load(configFile)

topic = config['MqttBroker']['topic'];
host = config['MqttBroker']['host'];
output = config['MqttBroker']['output'];
# currently not supported username = config['MqttBroker']['username'];
# currently not supported password = config['MqttBroker']['password'];

# text is default output
textHumidity = "%.2f %%rH" %humidity
textTemperature = "%.2f °C" %temperature
data = textTemperature + ' ' + textHumidity

# output json on request
if (output == 'json'):
    data = '{  "measurement": {    "timestamp": ' + str(round(time.time() * 1000))+ ', "temperature": {0:.1f}, "relhumidity": {1:.1f}'.format(temperature, humidity) + ' } } '

print('publishing...')

# post to an application specific topic, with the location as a subtopic
# The payload contains the data
publish.single(topic, payload=data, qos=0, retain=True, hostname=host);

# Report success
print(data + ' publicly published to ' + topic + '@' + host)
