# import paho.mqtt.client as mqtt  # import the client1
# import time
# from random import uniform
#
# client = mqtt.Client("Anton")  # создание клиента
# print("Подключение к брокеру")
# client.connect("127.0.0.1", 1883, 60)  # подключение к брокеру
# client.loop_start()  # start the loop
# print("Отправка сообщений в топик", "arconoid")
# while True:
#     temperature_value = uniform(-30.0, 30.0)    # создание рандомных значений температуры
#     client.publish("arconoid", temperature_value)    # отправка значений температуры в топик
#     print(temperature_value)
#     time.sleep(4)

# import paho.mqtt.client as mqtt    #import client library
#
# client = mqtt.Client("python")
# client.connect("127.0.0.1", 1883, 60) #connect to broker
# client.publish("house/main-light","OFF")#publish
# def on_connect(client, userdata, flags, rc):
#    if rc == 0:
#       print("connected ok")

# client.on_connect=onconnect  #bind call back function
# client.connect(broker_address)               #connect to broker
# client.loop_start()  #Start loop
# time.sleep(4) # Wait for connection setup to complete
# client.loop_stop()    #Stop loop


import paho.mqtt.client as mqtt  #import the client1
import time
import json

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)

mqtt.Client.connected_flag=False#create flag in class

client = mqtt.Client("python1")             #create new instance
client.on_connect=on_connect  #bind call back function
client.on_message=on_message

# client.loop_start()
print("Connecting to broker ")
client.connect("127.0.0.1", 1883)      #connect to broker
# while not client.connected_flag: #wait in loop
#     print("In wait loop")
#     time.sleep(1)
# print("in Main Loop")
# client.subscribe("arconoid")
# payload = "x,location=ru recx="+str(10)
dict_msg = {
    "contact": True,
    "something": 1.5,
    "temperature": 20.5,
    "my_field": "awesome",
}
msg = json.dumps(dict_msg)
client.publish("arconoid", msg)
time.sleep(4)
client.loop_forever()
# client.loop_stop()    #Stop loop
# client.disconnect() # disconnect
