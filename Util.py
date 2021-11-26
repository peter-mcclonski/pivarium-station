import json

from sensorimpl.DHT22 import DHT22


stationID = ""


def loadConfig(fName):
    with open(fName, 'r') as cfgFile:
        cfg = json.load(cfgFile)
    return cfg


def updateCfg(cfg, fName):
    print(f"Updating {fName} from remote host.")
    print(f"Updated configuration: ")
    print(json.dumps(cfg, indent=4))

    with open(fName, 'w') as cfgFile:
        json.dump(cfg, cfgFile, indent=4)


def orderDict(json):
    if isinstance(json, dict):
        return sorted((k, orderDict(v)) for k, v in json.items())
    if isinstance(json, list):
        return sorted(orderDict(x) for x in json)
    else:
        return json


def cfgEqual(json1, json2):
    return orderDict(json1) == orderDict(json2)


def extFromConfig(cfg: dict):
    ctype = cfg['connType'].lower()

    if ctype == 'dht22':
        return DHT22(cfg)
