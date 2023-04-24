import json
import mido

mido.set_backend("mido.backends.portmidi")
from jsonparser import Root


read_json = open("emptyconfig.json", "r").read()

# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)

jsonstring = json.loads(read_json)

root = Root.from_dict(jsonstring)

print(root.ipAddress)
print(root.port)
print(root.Layers.A.Buttons[0].press_event)

print(mido.get_input_names())
print(mido.get_output_names())
