from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class MoveEvent:
    type: str
    control: int

    @staticmethod
    def from_dict(obj: Any) -> "MoveEvent":
        _type = str(obj.get("type"))
        _control = int(obj.get("control"))
        return MoveEvent(_type, _control)


@dataclass
class PressEvent:
    type: str
    note: int
    value: int

    @staticmethod
    def from_dict(obj: Any) -> "PressEvent":
        _type = str(obj.get("type"))
        _note = int(obj.get("note"))
        _value = int(obj.get("value"))
        return PressEvent(_type, _note, _value)


@dataclass
class ReleaseEvent:
    type: str
    note: int
    value: int

    @staticmethod
    def from_dict(obj: Any) -> "ReleaseEvent":
        _type = str(obj.get("type"))
        _note = int(obj.get("note"))
        _value = int(obj.get("value"))
        return ReleaseEvent(_type, _note, _value)


@dataclass
class RotateEvent:
    type: str
    control: int
    middle: int

    @staticmethod
    def from_dict(obj: Any) -> "RotateEvent":
        _type = str(obj.get("type"))
        _control = int(obj.get("control"))
        _middle = int(obj.get("middle"))
        return RotateEvent(_type, _control, _middle)


@dataclass
class Button:
    name: str
    layer: str
    press_event: PressEvent
    release_event: ReleaseEvent

    @staticmethod
    def from_dict(obj: Any) -> "Button":
        _name = str(obj.get("name"))
        _layer = str(obj.get("layer"))
        _press_event = PressEvent.from_dict(obj.get("press_event"))
        _release_event = ReleaseEvent.from_dict(obj.get("release_event"))
        return Button(_name, _layer, _press_event, _release_event)


@dataclass
class Encoder:
    name: str
    layer: str
    press_event: PressEvent
    release_event: ReleaseEvent
    rotate_event: RotateEvent

    @staticmethod
    def from_dict(obj: Any) -> "Encoder":
        _name = str(obj.get("name"))
        _layer = str(obj.get("layer"))
        _press_event = PressEvent.from_dict(obj.get("press_event"))
        _release_event = ReleaseEvent.from_dict(obj.get("release_event"))
        _rotate_event = RotateEvent.from_dict(obj.get("rotate_event"))
        return Encoder(_name, _layer, _press_event, _release_event, _rotate_event)


@dataclass
class Fader:
    name: str
    layer: str
    move_event: MoveEvent

    @staticmethod
    def from_dict(obj: Any) -> "Fader":
        _name = str(obj.get("name"))
        _layer = str(obj.get("layer"))
        _move_event = MoveEvent.from_dict(obj.get("move_event"))
        return Fader(_name, _layer, _move_event)


@dataclass
class MidiMap:
    startup: list[str]
    Encoders: List[Encoder]
    Buttons: List[Button]
    Faders: List[Fader]

    @staticmethod
    def from_dict(obj: Any) -> "MidiMap":
        _startup = [str(x) for x in obj.get("startup")]
        _Encoders = [Encoder.from_dict(y) for y in obj.get("Encoders")]
        _Buttons = [Button.from_dict(y) for y in obj.get("Buttons")]
        _Faders = [Fader.from_dict(y) for y in obj.get("Faders")]
        return MidiMap(_startup, _Encoders, _Buttons, _Faders)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
