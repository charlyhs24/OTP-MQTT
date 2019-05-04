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
    #totp = pyotp.TOTP("azwarfatwagmailcom")
    #otp = totp.now()
    #otpin = input("otp : ")
    #msg = msg.payload
    #otpM = msg[:6]
    #otpMdec = otpin.decode("utf-8")
    #data = msg[6:]
    #message = data.decode("utf-8")
    
    #print(otpM)
    #print(otpin)
    #print(otpMdec)
    
    #if otpMdec==otpin:
     #   print(message)
     
    msg = msg.payload
    otpinput = input("otp : ")
    #print("your otp : ",otpinput)
    
    otpin = msg[:6]
    datamessage = msg[6:]
    
    #tampil data aja
    #print("otp : ",otpin)
    #print("msg : ",datamessage)
    
    #decoding
    otpinD = otpin.decode('utf-8')
    datamessageD = datamessage.decode('utf-8')
    
    #tampil data decoded
    #print(otpinD)
   # print(datamessageD)
    
    if otpinput == otpinD:
        print(datamessageD)
    else:
        print("invalid otp")
        exit()
        
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(server, port, keepalive)

client.loop_forever()
