import json
import os

import Api
import Util
from SensorAgent import SensorAgent


station_cfg = {}


def registerStation(cfg):
    remote_cfg = Api.registerStation(cfg)
    if not Util.cfgEqual(remote_cfg, cfg):
        Util.updateCfg(remote_cfg, './station.json')
    return remote_cfg


with open('./station.json', 'r') as cfgFile:
    station_cfg = json.load(cfgFile)

station_cfg = registerStation(station_cfg)
Util.stationID = station_cfg['uuid']

for filename in os.listdir(station_cfg['extensionPath']):
    if not filename.endswith(".json"):
        continue
    SensorAgent(os.path.join(station_cfg['extensionPath'], filename)).start()

