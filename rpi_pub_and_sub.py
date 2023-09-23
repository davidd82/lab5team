"""EE 250L Lab 04 Starter Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
from grovepi import *

led = 4
ultrasonic_ranger = 3

pinMode(led, "OUTPUT")

def custom_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print("custom_callback: " + message.topic + " " + "\"" + 
        str(message.payload, "utf-8") + "\"")
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload)))
    
    if (str(message.payload, "utf-8") == "LED_ON"):
        digitalWrite(led,1)
        print("Turned on LED")
    elif(str(message.payload, "utf-8") == "LED_OFF"):
        digitalWrite(led,0)
        print("Turned off LED")

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("davidd82/led")
    client.message_callback_add("davidd82/customCallback", custom_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = custom_callback
    client.on_connect = on_connect
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_start()

    time.sleep(1)
    while True:
        distance = ultrasonicRead(ultrasonic_ranger)
        client.publish("davidd82/ultrasonicRanger", distance)
        time.sleep(1)
            

