import Api
from Sensor import Sensor
from sensorimpl.DHT22 import DHT22


class SensorManager:
    sensors = {}

    def __init__(self):
        pass

    def registerSensor(self, config):
        stype = config['type']
        connType = config['connType']
        hwAddress = config['hwAddress']
        if 'uuid' in config.keys():
            uuid = config['uuid']
        else:
            uuid = Api.requestUUID()
            config['uuid'] = uuid

        if connType == 'DHT22':
            self.sensors[uuid] = DHT22(uuid, stype, connType, hwAddress)
        else:
            self.sensors[uuid] = Sensor(uuid, stype, connType, hwAddress)
