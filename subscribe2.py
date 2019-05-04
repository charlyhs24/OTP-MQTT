import paho.mqtt.client as mqtt
import pyaes
import hashlib
import configparser
import time
import pyotp

config = configparser.RawConfigParser()
config.read('config/config-subscriber.txt')
username = config.get('credential','username')
password = config.get('credential','password')
topic = config.get('credential','topic')
server = config.get('host','server')
port = config.getint('host','port')
keepalive = config.getint('host','keep-alive')



def on_connect( client, userdata, flags, rc):
    client.subscribe(topic)

def on_message( client, userdata, msg):

    msg = msg.payload
    totp = pyotp.TOTP("azwarfatwagmailcom")
    otp = totp.now()


    otpin = msg[:6]
    datamessage = msg[6:]

    if otpin==otp:
        print(datamessage)
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(server, port, keepalive)

client.loop_forever()
