import json
from math import floor
from pathlib import Path
from mido import Message, open_input, open_output
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


def oscSender(oscCommand: str):
    if len(oscCommand) != 0:
        if "," in oscCommand:
            oscCommand, oscValue = oscCommand.split(",", 1)
            oscClient.send_message(oscCommand, oscValue)
        elif "=" in oscCommand:  # For faders
            oscCommand, oscValue = oscCommand.split("=", 1)
            oscClient.send_message(oscCommand, oscValue)
        else:
            oscValue = 1
            oscClient.send_message(oscCommand, oscValue)


# Excute startup commands
for command in oscmap.startup:
    oscSender(command)

print(f'Connected to {oscmap.ipAddress}:{oscmap.port}')
print(f'Using {oscmap.midiDevice} as MIDI Device')

# with open_output(oscmap.midiDevice) as outport:
    # outport.send(Message('control_change', control=1, value=0))
    

# Select the correct input port for X-TOUCH MINI
with open_input(oscmap.midiDevice) as inport:
    print("Waiting for messages from X-TOUCH MINI")
    msg: Message
    for msg in inport:
        if msg.type == "control_change":
            # print(f'CC {msg.control} {msg.value}')
            for encoder in midimap.Encoders:
                if encoder.rotate_event.control == msg.control:
                    # print(f'OSC {encoder.rotate_event.control} {msg.value}')
                    if encoder.layer == "A":
                        for enc in oscmap.Layers.A.Encoders:
                            if enc.name == encoder.name:
                                # print(enc)
                                if msg.value > encoder.rotate_event.middle + 2:
                                    oscSender(enc.rotate_event.right_fast)
                                elif msg.value > encoder.rotate_event.middle:
                                    oscSender(enc.rotate_event.right_slow)
                                elif msg.value < encoder.rotate_event.middle - 2:
                                    oscSender(enc.rotate_event.left_fast)
                                elif msg.value < encoder.rotate_event.middle:
                                    oscSender(enc.rotate_event.left_slow)

                    elif encoder.layer == "B":
                        for enc in oscmap.Layers.B.Encoders:
                            if enc.name == encoder.name:
                                if msg.value > encoder.rotate_event.middle + 2:
                                    oscSender(enc.rotate_event.right_fast)
                                elif msg.value > encoder.rotate_event.middle:
                                    oscSender(enc.rotate_event.right_slow)
                                elif msg.value < encoder.rotate_event.middle - 2:
                                    oscSender(enc.rotate_event.left_fast)
                                elif msg.value < encoder.rotate_event.middle:
                                    oscSender(enc.rotate_event.left_slow)

                for fader in midimap.Faders:
                    if fader.move_event.control == msg.control:
                        # print(f'OSC {fader.move_event.control} {msg.value}')
                        if fader.layer == "A":
                            fad = oscmap.Layers.A.Fader
                            if fad.name == fader.name:
                                if fad.move_event[-1] == "=":
                                    # print(floor(msg.value/127*100))
                                    oscSender(
                                        fad.move_event
                                        + str(floor(msg.value / 127 * 100))
                                    )
                                else:
                                    oscSender(fad.move_event)
                        elif fader.layer == "B":
                            fad = oscmap.Layers.B.Fader
                            if fad.name == fader.name:
                                if fad.move_event[-1] == "=":
                                    # print(floor(msg.value/127*256))
                                    oscSender(
                                        fad.move_event
                                        + str(floor(msg.value / 127 * 256))
                                    )
                                else:
                                    oscSender(fad.move_event)

        elif msg.type == "note_on":
            for button in midimap.Buttons:
                if button.press_event.note == msg.note:
                    # print(f'OSC {button.press_event.note} {msg.velocity}')
                    if button.layer == "A":
                        for btn in oscmap.Layers.A.Buttons:
                            if btn.name == button.name:
                                oscSender(btn.press_event)
                    elif button.layer == "B":
                        for btn in oscmap.Layers.B.Buttons:
                            if btn.name == button.name:
                                oscSender(btn.press_event)

            for encoder in midimap.Encoders:
                if encoder.press_event.note == msg.note:
                    # print(f'OSC {encoder.press_event.note} {msg.velocity}')
                    if encoder.layer == "A":
                        for enc in oscmap.Layers.A.Encoders:
                            if enc.name == encoder.name:
                                oscSender(enc.press_event)
                    elif encoder.layer == "B":
                        for enc in oscmap.Layers.B.Encoders:
                            if enc.name == encoder.name:
                                oscSender(enc.press_event)

        elif msg.type == "note_off":
            for button in midimap.Buttons:
                if button.release_event.note == msg.note:
                    # print(f'OSC {button.press_event.note} {msg.velocity}')
                    if button.layer == "A":
                        for btn in oscmap.Layers.A.Buttons:
                            if btn.name == button.name:
                                oscSender(btn.release_event)
                    elif button.layer == "B":
                        for btn in oscmap.Layers.B.Buttons:
                            if btn.name == button.name:
                                oscSender(btn.release_event)

            for encoder in midimap.Encoders:
                if encoder.release_event.note == msg.note:
                    # print(f'OSC {encoder.press_event.note} {msg.velocity}')
                    if encoder.layer == "A":
                        for enc in oscmap.Layers.A.Encoders:
                            if enc.name == encoder.name:
                                oscSender(enc.release_event)
                    elif encoder.layer == "B":
                        for enc in oscmap.Layers.B.Encoders:
                            if enc.name == encoder.name:
                                oscSender(enc.release_event)
