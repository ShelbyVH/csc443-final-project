from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Button:
    name: str
    press_event: str
    release_event: str

    @staticmethod
    def from_dict(obj: Any) -> 'Button':
        _name = str(obj.get("name"))
        _press_event = str(obj.get("press_event"))
        _release_event = str(obj.get("release_event"))
        return Button(_name, _press_event, _release_event)

@dataclass
class RotateEvent:
    left_slow: str
    left_fast: str
    right_slow: str
    right_fast: str

    @staticmethod
    def from_dict(obj: Any) -> 'RotateEvent':
        _left_slow = str(obj.get("left_slow"))
        _left_fast = str(obj.get("left_fast"))
        _right_slow = str(obj.get("right_slow"))
        _right_fast = str(obj.get("right_fast"))
        return RotateEvent(_left_slow, _left_fast, _right_slow, _right_fast)

@dataclass
class Encoder:
    name: str
    press_event: str
    release_event: str
    rotate_event: RotateEvent

    @staticmethod
    def from_dict(obj: Any) -> 'Encoder':
        _name = str(obj.get("name"))
        _press_event = str(obj.get("press_event"))
        _release_event = str(obj.get("release_event"))
        _rotate_event = RotateEvent.from_dict(obj.get("rotate_event"))
        return Encoder(_name, _press_event, _release_event, _rotate_event)

@dataclass
class Fader:
    name: str
    move_event: str

    @staticmethod
    def from_dict(obj: Any) -> 'Fader':
        _name = str(obj.get("name"))
        _move_event = str(obj.get("move_event"))
        return Fader(_name,_move_event)

@dataclass
class A:
    Encoders: List[Encoder]
    Buttons: List[Button]
    Fader: Fader

    @staticmethod
    def from_dict(obj: Any) -> 'A':
        _Encoders = [Encoder.from_dict(y) for y in obj.get("Encoders")]
        _Buttons = [Button.from_dict(y) for y in obj.get("Buttons")]
        _Fader = Fader.from_dict(obj.get("Fader"))
        return A(_Encoders, _Buttons, _Fader)

@dataclass
class B:
    Encoders: List[Encoder]
    Buttons: List[Button]
    Fader: Fader

    @staticmethod
    def from_dict(obj: Any) -> 'B':
        _Encoders = [Encoder.from_dict(y) for y in obj.get("Encoders")]
        _Buttons = [Button.from_dict(y) for y in obj.get("Buttons")]
        _Fader = Fader.from_dict(obj.get("Fader"))
        return B(_Encoders, _Buttons, _Fader)

@dataclass
class Layers:
    A: A
    B: B

    @staticmethod
    def from_dict(obj: Any) -> 'Layers':
        _A = A.from_dict(obj.get("A"))
        _B = B.from_dict(obj.get("B"))
        return Layers(_A, _B)

@dataclass
class OSCMap:
    ipAddress: str
    port: int
    midiDevice: str
    startup: list[str]
    Layers: Layers

    @staticmethod
    def from_dict(obj: Any) -> 'OSCMap':
        _ipAddress = str(obj.get("ipAddress"))
        _port = int(obj.get("port"))
        _midiDevice = str(obj.get("midiDevice"))
        _startup = [str(x) for x in obj.get("startup")]
        _Layers = Layers.from_dict(obj.get("Layers"))
        return OSCMap(_ipAddress, _port, _midiDevice, _startup, _Layers)



# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
