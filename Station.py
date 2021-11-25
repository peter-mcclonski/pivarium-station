import json
import sys
import os

import Api
from SensorManager import SensorManager

sensorMngr = SensorManager()
with open('./station.json', 'r') as cfgFile:
    station_cfg = json.load(cfgFile)

if 'uuid' not in station_cfg.keys():
    station_cfg['uuid'] = Api.requestUUID()
    with open('./station.json', 'w') as cfgFile:
        json.dump(station_cfg, cfgFile, indent=4)

Api.registerStation(station_cfg['uuid'])

for filename in os.listdir('extensions'):
    if not filename.endswith(".json"):
        continue
    with open(os.path.join("extensions", filename), 'r') as confFile:
        cfg = json.load(confFile)

    uuidPresent = 'uuid' in cfg.keys()

    if cfg['ext'] == 'sensor':
        sensorMngr.registerSensor(cfg)

    if not uuidPresent:
        with open(os.path.join("extensions", filename), 'w') as confFile:
            json.dump(cfg, confFile, indent=4)

Api.putSensorList(station_cfg['uuid'], sensorMngr.sensors)
