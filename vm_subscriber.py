"""EE 250L Lab 04 Starter Code

Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time

#Custom callbacks need to be structured with three args like on_message()
def message_from_ultrasonic(client, userdata, message):
    print("VM: " + str(message.payload.decode("utf-8")) + " cm")

def message_from_button(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("davidd82/ultrasonicRanger")
    client.message_callback_add("davidd82/customCallback", message_from_ultrasonic)
    client.subscribe("davidd82/button")
    client.message_callback_add("davidd82/customCallback", message_from_button)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = message_from_button
    client.on_connect = on_connect
    client.connect(host= "test.mosquitto.org", port= 1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)        