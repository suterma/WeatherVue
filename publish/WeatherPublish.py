# WeatherPress.py - A simple, Raspberry Pi based weather station, that posts
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

textHumidity = "Relative Humidity is : %.3f %%rH" %humidity
textTemperature = "Temperature in Celsius is : %.3f °C" %temperature

print('preparing message publication...')

import yaml
with open("WeatherPublish.config.yml", "r") as configFile:
    config = yaml.safe_load(configFile)

topic = config['MqttBroker']['topic'];
host = config['MqttBroker']['host'];
# currently not supported username = config['MqttBroker']['username'];
# currently not supported password = config['MqttBroker']['password'];
data = textTemperature + ' ' + textHumidity


print('publishing...')

# post to an application specific topic, with the location as a subtopic
# The payload contains the data
publish.single(topic, payload=data, hostname=host);

# Report success
print(data + ' publicly published to ' + topic + '@' + host)