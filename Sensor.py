import time
from typing import Literal


class Sensor:
    uuid: str
    stype: list
    connType: Literal["dht22"]
    hwAddress: str
    frequency: int

    def __init__(self, cfg):
        self.uuid = cfg['uuid']
        self.stype = cfg['stype']
        self.connType = cfg['connType']
        self.hwAddress = cfg['hwAddress']
        self.frequency = cfg['frequency']

    def getStatus(self):
        return {
            'sensor_id': self.uuid,
            'utime': time.time()
        }

    def __str__(self):
        return f"Sensor[uuid={self.uuid},stype={self.stype},connType={self.connType},hwAddress={self.hwAddress},frequency={self.frequency}]"