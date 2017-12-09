import paho.mqtt.client as mqtt
import sys
from time import sleep

mqtt_broker="example.com"

client = mqtt.Client()
try:
	client.connect(mqtt_broker, 1883, 60)
	client.publish("tree",'{"mode":"on"}' )
	sleep(1)
	client.publish("tree",'{"mode":"off"}' )
	sleep(1)
	client.publish("tree",'{"mode":"blink"}' )
	sleep(1)
	client.publish("tree",'{"mode":"on"}' )
	client.disconnect()
except KeyboardInterrupt:
	client.disconnect()
	sys.exit()
