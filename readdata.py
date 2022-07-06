
# -*- coding: utf-8 -*-


import time
import serial

import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


def read_IAQ(PORT,ID):
    
    IAQ_Value = [0,0,0,0,0]
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        master.set_timeout(5.0)
        master.set_verbose(True)
        IAQ = master.execute(ID, cst.READ_HOLDING_REGISTERS, 0, 5)
        
        
        IAQ_Value[0] =  IAQ[0]
        IAQ_Value[1] =  IAQ[1]
        IAQ_Value[2] =  IAQ[2]
        IAQ_Value[3] =  IAQ[3] * 0.01
        IAQ_Value[4] =  IAQ[4] * 0.01
        
        master.close()
        time.sleep(0.5)
        return (IAQ_Value)

    except:
        IAQ_Value[0] =  0
        IAQ_Value[1] =  0
        IAQ_Value[2] =  0
        IAQ_Value[3] =  0
        IAQ_Value[4] =  0
        
        master.close()
        time.sleep(0.5)
        return (IAQ_Value) 
     
    
if __name__ == '__main__':
    while True:
        PORT = '/dev/ttyS1'
        ID = 1
        
        AC_IAQ = read_IAQ(PORT,ID)
        print (AC_IAQ)