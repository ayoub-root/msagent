
# mqttagent("id_of client",broker_url=test.mosquitto.org,port=1883,list of topic to subscribe ={'a'},
# list of callbacks which should be created before for each topic={on})
# send_data(name of topic='a',message to publish ="ccccc")
from httpagent import httpagent
from mqttagent import mqttagent

#broker = "test.mosquitto.org"
broker = "127.0.0.1"
port = 1883


def control(client, userdata, message):
    print(str(message.payload.decode('utf_8'))+"   "+str(message.topic))



ss = mqttagent("dddd", broker, port, ["control","b"], [control,control])
#threading.Thread(targe
for i in range(1,10):
    ss.send_data("control","{'endpoint:'www.google.Com'}")
                 #).start()
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
def print_response(response):
    print((response))

s=httpagent()
s.post_async('http://localhost:8000',None, callback=print_response)


#threading.Thread(target=
#ss.send_data("b","sssqsssoijiojisojo")
#).start()
#threading.Thread(target=ss.send_data,args=("b","ssoihoihoihsoijiojisojo")).start()
