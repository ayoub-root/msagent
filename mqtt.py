import threading
import time
import paho.mqtt.client as mqtt

import json
topic="data"
broker="test.mosquitto.org"
port=1883
def on_connect(client, userdata, flags, rc):
    print("CONNECTED")
    print("Connected with result code: ", str(rc))
    client.subscribe("data")
    client.subscribe("data2")
    print("subscribing to topic : "+topic)
   # print(client.__dir__())


def on_message(client, userdata, message):
    print("Data requested "+str(message.payload)+"  "+str(message.topic))

def control(client, userdata, message):
    print("received new cmd "+str(message.payload)+"  "+str(message.topic))

def data(client, userdata, message):
    print("received new data "+str(message.payload)+"  "+str(message.topic))


def main():
    print("WAIT for max: ",2)
    while True:
        time.sleep(1)
        client.publish("data2","ddddddddddddd")
        client.publish(topic,"fffffffffff")

### MQTT ###
client = mqtt.Client()
client.connect(broker, port)
client.on_connect = on_connect

#client.on_disconnect = on_disconnect
def subscribing():
    #client.on_message = on_message
    client.message_callback_add("control", control)
    client.message_callback_add("data", ff)

    client.loop_forever()
sub=threading.Thread(target=subscribing)
pub=threading.Thread(target=main)

### Start MAIN ###

sub.start()
pub.start()

