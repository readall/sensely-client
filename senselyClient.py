
import pulsar

SERVER_URL= 'pulsar://cec164b0-e2b4-4d40-9992-38b8c1db3409.pub.cloud.scaleway.com:6650'
SERVER_TOIPC='energypdu'


def sendToSenselyStr(data:str, srvurl:str=SERVER_URL , topic:str= SERVER_TOIPC, numSample:int=0):
    import sys
    client = pulsar.Client(srvurl)
    producer = client.create_producer(topic)

    try:
        print('INFO: start sending')
        sendBuf = data.to_json()
        producer.send(str(sendBuf).encode('utf-8'))
        #print(index , sendBuf)

    except:
        print('INFO: exception forcing close', sys.exc_info()[0])
        producer.close()
        client.close()
        return

    producer.close()
    client.close()
    print("INFO: Sending complete")


def sendToSenselyJSON(data:str, srvurl:str=SERVER_URL , topic:str= SERVER_TOIPC, numSample:int=0):
    import sys
    client = pulsar.Client(srvurl)
    producer = client.create_producer(topic)

    try:
        print('INFO: start sending')
        #sendBuf = data.to_json()
        producer.send(str(data).encode('utf-8'))
        #print(index , sendBuf)

    except:
        print('INFO: exception forcing close', sys.exc_info()[0])
        producer.close()
        client.close()
        return

    producer.close()
    client.close()
    print("INFO: Sending complete")


