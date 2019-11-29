import threading
import time
import paho.mqtt.client as mqtt

import json




def on_connect(client, userdata, flags, rc):
    print("CONNECTED")


def on_message(client, userdata, message): # default arrived messege
    print("Data requested "+str(message.payload)+"  "+str(message.topic))

class mqttagent:

    def __init__(self,id,broker,port):
        self.dev_id = id
        self.clientpub = mqtt.Client(self.dev_id + "pub")
        self.clientpub.connect(broker, port)
    def __init__(self,id,broker,port,topics,callbacks):
        self.dev_id=id
        self.topics=topics
        self.callbacks=callbacks
        self.clientpub = mqtt.Client(self.dev_id+"pub")
        self.clientpub.connect(broker, port)
        threads=[]
        sub=[]
        for i,j in zip(self.topics,self.callbacks):
            #print(type(i))
            ss=mqtt.Client(self.dev_id + "sub"+i)
            ss.connect(broker, port)
            ss.subscribe(i)
            threads.append(threading.Thread(target=self.subscribing,args=(ss,i,j)))
        for th in threads:

            #th.join()
            th.start()

    def send_data(self,topic,data):
        #print("sending data")
        self.clientpub.publish(str(topic),data)
    def subscribing(self,sub,topic,callback):

        sub.message_callback_add(sub=topic,callback=callback)
        print("subscrbing to " + str(topic))

        sub.loop_forever()

##agent= mqttagent("dd")
#agent.send_data("control","doihoij")


