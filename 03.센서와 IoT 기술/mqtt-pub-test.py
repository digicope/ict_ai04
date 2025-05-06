# mqtt-pub-test.py

'''
# MQTT 환경 설정
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
pip install paho-mqtt
'''

import time
import json
import paho.mqtt.client as mqtt

broker = "localhost"  
port = 1883
topic = "test/topic"

client = mqtt.Client()
client.connect(broker, port)

while True:
    payload = {
        "timestamp": int(time.time()),
        "value": round(25 + time.time() % 5, 2)
    }
    client.publish(topic, json.dumps(payload))
    print("Published:", payload)
    time.sleep(2)
