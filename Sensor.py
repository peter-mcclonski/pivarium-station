from typing import Literal


class Sensor:
    uuid: str
    stype: Literal["humidity", "temperature"]
    connType: Literal["dht22"]
    hwAddress: str

    def __init__(self, uuid: str, stype: Literal["humidity", "temperature"], connType: Literal["dht22"], hwAddress: str):
        self.uuid = uuid
        self.stype = stype
        self.connType = connType
        self.hwAddress = hwAddress
