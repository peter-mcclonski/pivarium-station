import json

from local_crontab import Converter
from celerybeatmongo.models import PeriodicTask

from src.app.DHT22 import DHT22


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


def to_utc_crontab(crontab: PeriodicTask.Crontab) -> PeriodicTask.Crontab:
    ct_str = f"{crontab.minute} {crontab.hour} {crontab.day_of_month} {crontab.month_of_year} {crontab.day_of_week}"
    utc_ct = Converter(ct_str, 'America/New_York').to_utc_cron().split(' ')
    return PeriodicTask.Crontab(
        minute=utc_ct[0],
        hour=utc_ct[1],
        day_of_month=utc_ct[2],
        month_of_year=utc_ct[3],
        day_of_week=utc_ct[4]
    )
