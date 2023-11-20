import time
from threading import Thread

from src.app import Api, SenseTask
import Util
from src.app.Sensor import Sensor


class SensorAgent(Thread):
    sensor: Sensor
    config: dict
    cfgFileName: str

    def __init__(self, cfgFileName):
        Thread.__init__(self)
        self.config = Util.loadConfig(cfgFileName)
        self.cfgFileName = cfgFileName
        self.register()

    def register(self):
        if "stationID" not in self.config:
            self.config['stationID'] = Util.stationID

        if "uuid" in self.config.keys():
            print(f"Registering Sensor: {self.config['uuid']}")
        else:
            print("Registering New Sensor")
        remote_cfg = Api.registerSensor(self.config)
        if not Util.cfgEqual(self.config, remote_cfg):
            Util.updateCfg(remote_cfg, self.cfgFileName)
        self.config = remote_cfg

    def run(self):
        while True:
            SenseTask.sense.delay(self.config)
            time.sleep(self.config['frequency'])
