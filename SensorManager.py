import Api
from Sensor import Sensor


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
        self.sensors[uuid] = Sensor(uuid, stype, connType, hwAddress)
