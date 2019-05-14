
import websocket
import base64
import json
import sys
import os
import time
from datetime import datetime, timedelta
import numpy as np

#SERVER_NAME="cec164b0-e2b4-4d40-9992-38b8c1db3409.pub.cloud.scaleway.com"
SERVER_NAME="51.15.237.55"
PROTO="ws://"
PORT=":8080"

TOPIC = '/ws/v2/producer/persistent/public/default/energypdu'

def senselyWebSocket(uri:str, 
                            deviceID:str,
                            channelID:np.long,
                            voltage:np.float,
                            current:np.float,
                            temperature:np.float,
                            timestamp:np.long):

    paramDict = {"deviceId":deviceID,
            "channel":channelID,
            "timestamp":timestamp,
            "voltage":voltage,
            "current":current,
            "temperature":temperature}



    print(uri)
    
    websock =  websocket.create_connection(uri)



    nDict = {
                "payload":base64.b64encode(json.dumps(paramDict).encode('utf-8')).decode('utf-8')
            }

    buf = str(json.dumps(nDict)).encode('utf-8')
    #buf = str(nDict)
    print(buf)
    
    websock.send(buf)

    resp = json.loads(websock.recv())

    if resp['result'] == 'ok':
        print('Message published successfully', resp)
    else:
        print( 'Failed to publish message:', resp)


def senselySendREST( deviceID:str,
                     channelID:np.long,
                     voltage:np.float,
                     current:np.float,
                     temperature:np.float,
                     timestamp:np.long):


    uri = PROTO+SERVER_NAME+PORT+TOPIC

    senselyWebSocket(uri, 
            deviceID=deviceID,
            channelID=channelID
            voltage=voltage
            current=current
            temperature=temperature
            timestamp=timestamp
            )


if __name__=="__main__":
    uri = PROTO+SERVER_NAME+PORT+TOPIC
    #senselyWebSocket(uri, "sen-pdu-r-0010", 5, -48, 15.89, 55.98, int(round(time.time())))
    #time.sleep(10)
    for i in range(1,10):
        senselySendREST(
                deviceID="sen-pdu-r-0010", 
                channelID=i,
                voltage=-i, 
                current=round((-15.89+i),2), 
                temperature=round((i/10+5.98),2), 
                timestamp=int(round(time.time(),0))
                )
        #time.sleep(1)


