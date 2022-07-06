import schedule  
import time  
import readdata
  
def job():  
    indoor_IAQ = readdata.read_IAQ('/dev/ttyS1',1)
    print(indoor_IAQ)  
  
schedule.every(10).seconds.do(job)  
  
while True:  
    try:
        schedule.run_pending()  
        time.sleep(1) 
    except:
        print('error') 