#!/usr/bin/env python3

import sys
import json
import random
import datetime
import os

import io
import requests
import socket
import re


def send_post_openhab(item,signal): 
    URL= 'http://192.168.1.36:8080/rest/items/'+item
    headers = {
        'Content-Type': 'text/plain',
        'Accept': 'application/json',
    }
    data = signal
    url_archivo_salida = 'response.xml'

    try:
        resp = requests.post( URL, headers = headers, data = data )

    except Exception as e:
        print( 'The exception >> ' + type(e).__name__ )
        raise e

    else:
        #requests.codes.ok = 200 => OK
        if( resp.status_code == requests.codes.ok ):
            with open( url_archivo_salida, 'w' ) as f:
                f.write( resp.text )
                f.close()
        else:
            out = 'resp.status_code >> ' + str(resp.status_code) + ' != ' + str(requests.codes.ok) 

def things_onoff(msg):

    if msg.find("lights")>=0 or msg.find("light")>=0:
        if msg.find("home")>=0 or msg.find("house")>=0 or msg.find("all")>=0:     
            if msg.find("on")>=0:          
                send_post_openhab("HueBulb_Color_OnOff", "ON")
                send_post_openhab("HueColorLamp1_Color_OnOff", "ON")
                send_post_openhab("HueColorLamp2_Color_OnOff", "ON")
            if msg.find("off")>=0:
                send_post_openhab("HueBulb_Color_OnOff", "OFF")
                send_post_openhab("HueColorLamp1_Color_OnOff", "OFF")
                send_post_openhab("HueColorLamp2_Color_OnOff", "OFF")          
        if msg.find("kitchen")>=0:
            if msg.find("table")>=0:
                if msg.find("on")>=0:          
                    send_post_openhab("Kueche1_KNX_Licht_Schalten", "ON") 
                if msg.find("off")>=0:
                    send_post_openhab("Kueche1_KNX_Licht_Schalten", "OFF")          
            elif msg.find("work")>=0:
                if msg.find("on")>=0:          
                    send_post_openhab("Kueche2_KNX_Licht_Schalten", "ON")  
                if msg.find("off")>=0:
                    send_post_openhab("Kueche2_KNX_Licht_Schalten", "OFF")          
            elif msg.find("ceiling")>=0:
                if msg.find("on")>=0:          
                    send_post_openhab("Kueche_LichtDimmer", "100")
                if msg.find("off")>=0:
                    send_post_openhab("Kueche_LichtDimmer", "0")          
            else:               
                if msg.find("on")>=0:          
                    send_post_openhab("HueColorLamp1_Color_OnOff", "ON")
                if msg.find("off")>=0:
                    send_post_openhab("HueColorLamp1_Color_OnOff", "OFF")                                                     
        if msg.find("living room")>=0:       
            if msg.find("center")>=0:
                if msg.find("on")>=0:          
                    send_post_openhab("WZ_KNX_Licht_Schalten", "ON")  
                if msg.find("off")>=0:
                    send_post_openhab("WZ_KNX_Licht_Schalten", "OFF")          
            elif msg.find("ceiling")>=0:   
                if msg.find("on")>=0:          
                    send_post_openhab("WZ_LichtDimmer", "100")
                if msg.find("off")>=0:
                    send_post_openhab("WZ_LichtDimmer", "0")           
            else:
                if msg.find("on")>=0:          
                    send_post_openhab("HueBulb_Color_OnOff", "ON")
                if msg.find("off")>=0:
                    send_post_openhab("HueBulb_Color_OnOff", "OFF")             
        elif msg.find("room")>=0 or msg.find("bedroom")>=0:       
            if msg.find("on")>=0:          
                send_post_openhab("HueColorLamp2_Color_OnOff", "ON")  
            if msg.find("off")>=0:
                send_post_openhab("HueColorLamp2_Color_OnOff", "OFF")

    if msg.find("hob")>=0:        
        if msg.find("on")>=0:          
            send_post_openhab("Kueche_Platte", "ON")  
        if msg.find("off")>=0:
            send_post_openhab("Kueche_Platte", "OFF") 

    if msg.find("oven")>=0:        
        if msg.find("on")>=0:          
            send_post_openhab("Kueche_Ofen", "ON")  
        if msg.find("off")>=0:
            send_post_openhab("Kueche_Ofen", "OFF")   
    
    if msg.find("music")>=0 or msg.find("stereo")>=0 or msg.find("yamaha")>=0 or msg.find("sound system")>=0: 

        if msg.find("on")>=0:                
            send_post_openhab("RXV685Main_Zone_Zone_channels_Power", "ON")
        if msg.find("off")>=0: 
            send_post_openhab("RXV685Main_Zone_Zone_channels_Power", "OFF")
                
def things_control(msg):

    if msg.find("to")>=0 or msg.find("light")>=0:
        if msg.find("green")>=0:           
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Color", "0,100,100")
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Color", "0,100,100")
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Color", "0,100,100")          
        if msg.find("red")>=0:           
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Color", "0,100,100")
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Color", "0,100,100")
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Color", "0,100,100")
        if msg.find("blue")>=0:           
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Color", "202,100,100")
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Color", "202,100,100")
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Color", "202,100,100")
        if msg.find("yellow")>=0:           
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Color", "46,99,100")
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Color", "46,99,100")
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Color", "46,99,100")
        if msg.find("orange")>=0:           
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Color", "27,100,100")
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Color", "27,100,100")
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Color", "27,100,100")
        if msg.find("pink")>=0:           
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Color", "326,100,100")
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Color", "326,100,100")
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Color", "326,100,100")                       
        if msg.find("purple")>=0:           
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Color", "263,78,100")
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Color", "263,78,100")
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Color", "263,78,100")  
        if msg.find("white")>=0:           
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Color", "191,1,100")
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Color", "191,1,100")
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Color", "191,1,100")                                        
        elif msg.find("percent")>=0:
            numberint = re.findall("\d+", msg)[0]
            number = str(numberint)
            if msg.find("kitchen")>=0:
                send_post_openhab("HueColorLamp1_Color_Dimmer", number)
            if msg.find("living room")>=0:
                send_post_openhab("HueBulb_Color_Dimmer", number)
            elif msg.find("room")>=0:                
                send_post_openhab("HueColorLamp2_Color_Dimmer", number)          
    if msg.find("blinds")>=0 or msg.find("blind")>=0 or msg.find("shutters")>=0:
        if msg.find("kitchen")>=0:
            if msg.find("up")>=0 or msg.find("raise")>=0:
                send_post_openhab("Kuche_Jalousie1", "0")
                send_post_openhab("Kuche_Jalousie2", "0")
            if msg.find("down")>=0 or msg.find("lower")>=0:
                send_post_openhab("Kuche_Jalousie1", "100")
                send_post_openhab("Kuche_Jalousie2", "100")            
            elif msg.find(" to ")>=0 or msg.find(" as ")>=0:
                numberint = re.findall("\d+", msg)[0]
                number = str(numberint)
                send_post_openhab("Kuche_Jalousie1", number)
                send_post_openhab("Kuche_Jalousie2", number)                                   

        if msg.find("living room")>=0:
            if msg.find("up")>=0 or msg.find("raise")>=0:
                send_post_openhab("WZ_Jalousien", "0")
            if msg.find("down")>=0 or msg.find("lower")>=0:
                send_post_openhab("WZ_Jalousien", "100")         
            elif msg.find(" to ")>=0 or msg.find(" as ")>=0:
                numberint = re.findall("\d+", msg)[0]
                number = str(numberint)
                send_post_openhab("WZ_Jalousien", number)                

        if msg.find("all")>=0 or msg.find("home")>=0 or msg.find("house")>=0:
            if msg.find("up")>=0 or msg.find("raise")>=0:
                send_post_openhab("Wohnung_Jalousien", "0")
            if msg.find("down")>=0 or msg.find("lower")>=0:
                send_post_openhab("Wohnung_Jalousien", "100")           
            elif msg.find(" to ")>=0 or msg.find(" as ")>=0:
                numberint = re.findall("\d+", msg)[0]
                number = str(numberint)
                send_post_openhab("Wohnung_Jalousien", number)    
    
    if msg.find("music")>=0 or msg.find("stereo")>=0 or msg.find("yamaha")>=0 or msg.find("sound system")>=0:                          
        if msg.find("source")>=0 or msg.find("mode")>=0: 
            if msg.find("bluetooth")>=0: 
                send_post_openhab("RXV685Main_Zone_Zone_channels_", "Bluetooth")
            if msg.find("tuner")>=0 or msg.find("radio")>=0: 
                send_post_openhab("RXV685Main_Zone_Zone_channels_", "Tuner")
            if msg.find("auxiliar")>=0 or msg.find("aux")>=0:   
                send_post_openhab("RXV685Main_Zone_Zone_channels_", "aux")
            if msg.find("net radio")>=0:   
                send_post_openhab("RXV685Main_Zone_Zone_channels_", "NET RADIO")
        if msg.find("volume")>=0: 
                numberint = re.findall("\d+", msg)[0]
                number = str(numberint)
                send_post_openhab("RXV685Main_Zone_Zone_channels_Volume", number)
        if msg.find("scene")>=0: 
                numberint = re.findall("\d+", msg)[0]
                number = str(numberint)
                send_post_openhab("RXV685Main_Zone_Zone_channels_Scene", "Scene "+number)

def music_control(msg):
    print("in")
    if msg.find("play")>=0:
        print("sda")
        send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Play")
    if msg.find("pause")>=0: 
        send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Pause")
    if msg.find("next")>=0:
        send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Next")                             
    if msg.find("previous")>=0:
        send_post_openhab("RXV685Main_Zone_Playback_channels_PlaybackControl", "Previous")
    if msg.find("scene")>=0 or msg.find("silence")>=0:
        if msg.find("off")>=0 or msg.find("active")>=0:  
            send_post_openhab("RXV685Main_Zone_Zone_channels_Mute", "OFF")            
        else:  
            send_post_openhab("RXV685Main_Zone_Zone_channels_Mute", "ON")            

def speech(text):
    global o
    o["speech"] = {"text": text}


# get json from stdin and load into python dict
#o = json.loads(sys.stdin.read())

intent = o["intent"]["name"]
msg = o["text"]
#intent = "MusicControl"
#msg = "play music"

if intent == "GetTime":
    now = datetime.datetime.now()
    speech("Charles It's %s %d %s." % (now.strftime('%H'), now.minute, now.strftime('%p')))
    send_post_openhab("HueBulb_Color_Color", "27,100,100")

    
elif intent == "Hello":
    replies = ['Hi!', 'Hello!', 'Hey there!', 'Greetings.']
    speech(random.choice(replies))
    
elif intent == "PercentageControl":
    things_control(msg)
    replies = ['Okey', 'Done!', 'Adjusted as your like']
    speech(random.choice(replies))
    speech(msg)

elif intent == "ChangeState":
    things_onoff(msg)
    replies = ['Okey', 'Done!', 'Adjusted as your like']
    speech(random.choice(replies))

elif intent == "MusicControl":
    music_control(msg)
    replies = ['Okey', 'Done!', 'Adjusted as your like']
    speech(random.choice(replies))

# convert dict to json and print to stdout
print(json.dumps(o))
