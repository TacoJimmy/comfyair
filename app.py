import schedule  
import time  
import paho.mqtt.client as mqtt
import json  
import time
import readdata
  
client = mqtt.Client()
client.username_pw_set("CuOkY4nZsqUmIfBkD6Eo","xxx")
client.connect("thingsboard.cloud", 1883, 60)

def job():  
    indoor_IAQ = readdata.read_IAQ('/dev/ttyS1',1)
    payload = {'CO2' : indoor_IAQ[0],'pm2_5' : indoor_IAQ[1],
               'pm10' : indoor_IAQ[2],'temp' : indoor_IAQ[3],
               'humid' : indoor_IAQ[4] }
    print (json.dumps(payload))
    client.publish("v1/devices/me/telemetry", json.dumps(payload))
     
  
schedule.every(5).minutes.do(job)  
  
while True:  
    try:
        schedule.run_pending()  
        time.sleep(1) 
    except:
        print('error') 