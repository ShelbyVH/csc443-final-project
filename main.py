import json
from math import floor
from pathlib import Path
from mido import Message, open_input
from tap import Tap
from models.midiparser import MidiMap
from models.oscparser import OSCMap
from pythonosc.udp_client import SimpleUDPClient


class MyArgumentParser(Tap):
    config: Path = "defaultconfig.json"  # Path to config file
    
args = MyArgumentParser().parse_args()


oscjson = open(args.config, "r").read()
oscmap = OSCMap.from_dict(json.loads(oscjson))


# Check if json for midiDevice exists
midiPath = Path(f'./mididevices/{oscmap.midiDevice.replace(" ","-")}.json')
if not midiPath.exists():
    print(f'{oscmap.midiDevice.replace(" ","-")}.json does not exist')
    exit()
    
midijson = open(midiPath, "r").read()
midimap = MidiMap.from_dict(json.loads(midijson))

# Create OSC Client
oscClient = SimpleUDPClient(oscmap.ipAddress, oscmap.port)


# Select the correct input port for X-TOUCH MINI
with open_input(oscmap.midiDevice) as inport:
    print("Waiting for messages from X-TOUCH MINI")
    msg: Message
    for msg in inport:
        if (msg.type == "control_change"):
            # print(f'CC {msg.control} {msg.value}')
            for encoder in midimap.Encoders:
                if (encoder.rotate_event.control == msg.control):
                    # print(f'OSC {encoder.rotate_event.control} {msg.value}')
                    if (encoder.layer == "A"):
                        for enc in oscmap.Layers.A.Encoders:
                            if (enc.name == encoder.name):
                                # print(enc)    
                                if (msg.value > encoder.rotate_event.middle+2):
                                    oscClient.send_message(enc.rotate_event.right_fast, 1)
                                elif (msg.value > encoder.rotate_event.middle):
                                    oscClient.send_message(enc.rotate_event.right_slow, 1)                                    
                                elif (msg.value < encoder.rotate_event.middle-2):
                                    oscClient.send_message(enc.rotate_event.left_fast, 1)                                    
                                elif (msg.value < encoder.rotate_event.middle):
                                    oscClient.send_message(enc.rotate_event.left_slow, 1)
                                                                
                    elif (encoder.layer == "B"):
                        for enc in oscmap.Layers.B.Encoders:
                            if (enc.name == encoder.name):
                                if (msg.value > encoder.rotate_event.middle+2):
                                    oscClient.send_message(enc.rotate_event.right_fast, 1)
                                elif (msg.value > encoder.rotate_event.middle):
                                    oscClient.send_message(enc.rotate_event.right_slow, 1)                                    
                                elif (msg.value < encoder.rotate_event.middle-2):
                                    oscClient.send_message(enc.rotate_event.left_fast, 1)                                    
                                elif (msg.value < encoder.rotate_event.middle):
                                    oscClient.send_message(enc.rotate_event.left_slow, 1)
                                
                for fader in midimap.Faders:
                    if (fader.move_event.control == msg.control):
                        # print(f'OSC {fader.move_event.control} {msg.value}')
                        if (fader.layer == "A"):
                            fad = oscmap.Layers.A.Fader
                            if (fad.name == fader.name):
                                print(floor(msg.value/127*256))
                                # oscClient.send_message(fad.move_event., msg.value/127)
                        elif (fader.layer == "B"):
                            fad = oscmap.Layers.B.Fader
                            if (fad.name == fader.name):
                                print(floor(msg.value/127*256))
                                # oscClient.send_message(fad.move_event.address, msg.value/127)
                                
        elif (msg.type == "note_on"):
            for button in midimap.Buttons:
                if (button.press_event.note == msg.note):
                    # print(f'OSC {button.press_event.note} {msg.velocity}')
                    if (button.layer == "A"):
                        for btn in oscmap.Layers.A.Buttons:
                            if (btn.name == button.name):
                                print(btn.press_event)
                                oscClient.send_message(btn.press_event, 1)
                    elif (button.layer == "B"):
                        for btn in oscmap.Layers.B.Buttons:
                            if (btn.name == button.name):
                                oscClient.send_message(btn.press_event, 1)
                                
            for encoder in midimap.Encoders:
                if (encoder.press_event.note == msg.note):
                    # print(f'OSC {encoder.press_event.note} {msg.velocity}')
                    if (encoder.layer == "A"):
                        for enc in oscmap.Layers.A.Encoders:
                            if (enc.name == encoder.name):
                                oscClient.send_message(enc.press_event, 1)
                    elif (encoder.layer == "B"):
                        for enc in oscmap.Layers.B.Encoders:
                            if (enc.name == encoder.name):
                                oscClient.send_message(enc.press_event, 1)
                                
        elif (msg.type == "note_off"):
            for button in midimap.Buttons:
                if (button.release_event.note == msg.note):
                    # print(f'OSC {button.press_event.note} {msg.velocity}')
                    if (button.layer == "A"):
                        for btn in oscmap.Layers.A.Buttons:
                            if (btn.name == button.name):
                                oscClient.send_message(btn.release_event, 1)
                    elif (button.layer == "B"):
                        for btn in oscmap.Layers.B.Buttons:
                            if (btn.name == button.name):
                                oscClient.send_message(btn.release_event, 1)
                                
            for encoder in midimap.Encoders:
                if (encoder.release_event.note == msg.note):
                    # print(f'OSC {encoder.press_event.note} {msg.velocity}')
                    if (encoder.layer == "A"):
                        for enc in oscmap.Layers.A.Encoders:
                            if (enc.name == encoder.name):
                                oscClient.send_message(enc.release_event, 1)
                    elif (encoder.layer == "B"):
                        for enc in oscmap.Layers.B.Encoders:
                            if (enc.name == encoder.name):
                                oscClient.send_message(enc.release_event, 1)
                                