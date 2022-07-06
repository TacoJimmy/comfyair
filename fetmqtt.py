import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time




client = mqtt.Client()


client.username_pw_set("CuOkY4nZsqUmIfBkD6Eo","xxxx")

# 設定連線資訊(IP, Port, 連線時間)
client.connect("thingsboard.cloud", 1883, 60)

while True:
    
    payload = {'Temp' : 20}
    print (json.dumps(payload))
    #要發布的主題和內容
    client.publish("Try/MQTT", json.dumps(payload))
    time.sleep(5)