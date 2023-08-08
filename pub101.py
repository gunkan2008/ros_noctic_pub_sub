import paho.mqtt.client as mqtt
host = "broker.hivemq.com"
port = 1883
client = mqtt.Client()
client.connect(host)
client.publish("PUB/MQTT","HELLO MQTT")

