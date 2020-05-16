# Control of IoT devices using an openHAB server controlled by Rhasspy as a voice assistant

Skill created manually based on sending POST requests from the Rhasspy Voice Assistant (OpenSource) to an openHAB server. This particular code includes the control of different devices such as blinds, lights (like Google Hue), a music device and some extra devices but is easily configurable according to the infrastructure of each following the basic structure of the skill.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To be able to use the next skill the following prerequisites are needed.

* Raspberry Pi 3 or 3B+
* An SD card
* The following image (https://github.com/MycroftAI/enclosure-picroft/)
* openHAB server (https://www.openhab.org/docs/installation/) -> Java platforms

There are other alternatives for installing the Mycroft system as indicated in the official documentation (https://mycroft.ai/get-started/)

It should be noted that to be able to use the openHAB server the corresponding device must be able to be switched on all the time and must be able to connect to the WiFi network. In this case it has been verified that it works both with a dedicated server and with the openHAB server installed on a laptop.


### Installing

A step by step series of examples that tell you how to get a development env running

The openHAB server and the device where is the voice assistant installed must be configured in the same WiFi network.

The next step in this case is to obtain the IP address of the server, which can be easily obtained by writing the ifconfig (Linux) or ipconfig (Windows) command in a terminal of the device where the server is located. Other common alternatives can be considered depending on the O.S. of the device. After obtaining this address, the IP address should be changed in the ex12.py and ex12g.py file in line of code 16 to the one obtained in this case, this will allow the commands collected by the Rhasspy system to be sent directly to the openHAB server for execution.


This is where, depending on the previous configuration of the openHAB server according to the devices you have, you will have to set up the POST requests according to the names you have configured the different IoT elements of your network with. In order to make this task easier, it is recommended to look for the following URL in a browser: http://server_ip:8080/rest/items/ and be able to see the exact name of each one of the devices configured in the server so that you can later replace them in the Python code.

To make this task easier and to facilitate the configuration of the code, we recommend the option of editing the code on a computer using some editor (VisualStudio) and then copying the whole folder to the Raspbian system using the Windows scp command or the equivalent on each operating system.

The next step for the configuration of the system is to open a browser in Rhasspy with the following URL: http://localhost:12101 where a website will open with different tabs that will allow us to configure the system.

The first thing to do in this part is to go to the settings tab and make the necessary adjustments according to the microphone being used so that the system detects both the commands and the wake word (there are also different options to configure the wake word according to the characteristics of each user, https://rhasspy.readthedocs.io/en/latest/wake-word/)

When you check that everything is detected correctly, you must configure the sentences, which are the different options that the user sets so that the different commands can be said. After setting all the desired options, the system must be trained to work properly with these commands. As, for example, the next sentences:



´´´
[GetTime]
what time is it
tell me the time

[GetTemperature]
whats the temperature
how (hot | cold) is it

[PercentageControl]
device_name = ((light | lights) {name})
blind_name = ((blind | blinds | shutters) {name})  
music_name = ((music | stereo | sound system | yamaha) {name}) 
place_name = ((kitchen | living room | all | house | home | room | bedroom ) {name}) 
color_state = (green | red | blue | yellow | orange| white | pink | purple) {color}
source_state = (radio | tuner | usb | net radio | auxiliar | aux | bluetooth | cd) {source}
blind_state = (up | down) {state}

turn on [the] <place_name> <device_name> [to] <color_state> [color]
put [the] <place_name> <device_name> [to] <color_state>
set <place_name> <device_name> [to] <color_state>
adjust <color_state> <place_name> <device_name>
adjust to (0..100) percent <place_name> <device_name> 
regulate to (0..100) percent <place_name> <device_name> 
adjust <place_name> <device_name> to (0..100) [percent]
tune <place_name> <device_name> to (0..100) [percent]
regulate <place_name> <device_name> to (0..100) [percent] 
draw <blind_state> [the] <place_name> <blind_name> 
regulate to (0..100) [percent] [the] <music_name> volume
adjust to (0..100) [percent] [the] <music_name> volume
set to (0..100) [percent] [the] <music_name> volume
regulate to (0..100) [percent] [the] <music_name> volume
change [the] <music_name> to scene (0..10)
adjust [the] <music_name> to scene (0..10)
set [the] <music_name> to scene (0..10)

[ChangeState]
light_name = ((light | lights) {name}) 
space_name = ((ceiling | center | table) {name}) 
thing_name = ((music | stereo | sound system | hob | oven | radio) {name}) 
place_name = ((kitchen | living room | all | house | home | room | bedroom ) {name}) 
the_state = (on | off) {state}

turn <the_state> [the] <place_name> <light_name>
turn [the] <place_name> <the_state>
switch <the_state> [the] <place_name> <light_name>
switch [the] <place_name> <space_name> <light_name> <the_state> 

[MusicControl]
music_name = ((music | stereo | sound system | device | song | equipment | radio) {name}) 

play [the] <music_name>
pause [the] <music_name>
next <music_name>
previous <music_name>
mute [the] <music_name>
active [the] sound [again]
active [the] volume [again]  


´´´

Finally the system must be configured to run the Python code we have created. We will have to copy the Python file ex12.py in the folder /home/pi/.config/rhasspy/profiles/en and the ex12g.py in /home/pi/.config/rhasspy/profiles/de. Each code based on each language with the respective profile settings in the same language.

You should edit the file profile.json until you have something similar to this, with the respective settings of the wake word and the audio input according to each case, you can also change this from the advanced section of the website.

´´´
{
    "handle": {
        "command": {
            "program": "$RHASSPY_PROFILE_DIR/ex12.py"
        },
        "forward_to_hass": true,
        "system": "command"
    },
    "microphone": {
        "pyaudio": {
            "device": "5"
        }
    },
    "speech_to_text": {
        "system": "kaldi"
    },
´´´
After rebooting the system, everything will be ready to go.

It should be noted that the Rhasspy system allows us to configure different tools for different phases of the process. As in the case of the Speech to Text, different options are allowed (Pocketsphinx or Kaldi are recommended) which allows the user to choose the system he wants to use depending on which one provides better results. If you want to test both systems you simply have to choose between the different options in the settings tab and restart the system.



## Commands examples

There are avaliable different options to execute the same order (more variability so more natural).

```
(Turn/Switch) (on/off) the (kitchen/living room/bedroom) lights
(Adjust/Regulate/..) (kitchen/living room/bedroom) lights to ("color")
(Adjust/Regulate/..) (kitchen/living room/bedroom) lights to ("number") percent
(Raise/Lower/Roll up...) (kitchen/living room/bedroom) blinds
(Adjust/Regulate/..) (kitchen/living room/bedroom) blinds to ("number") percent
(Turn/Switch) (on/off) the (oven/hob/stereo)
(Play/Pause/Next/Previous/Mute) (Music/Song)

```

Similar commands also avaliable in German.