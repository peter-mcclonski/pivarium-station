import json
import os

from celery_instance import celery as app

from celerybeatmongo.models import PeriodicTask
import settings

from Api import *
import SenseTask
import Util


def registerNewSensor(cfgFileName):
    cfg = Util.loadConfig(cfgFileName)
    if "stationID" not in cfg:
        cfg['stationID'] = Util.stationID

    if 'uuid' in cfg.keys():
        print(f"Registering Sensor: {cfg['uuid']}")
    else:
        print("Registering New Sensor")
    remote_cfg = registerSensor(cfg)
    if not Util.cfgEqual(cfg, remote_cfg):
        Util.updateCfg(remote_cfg, cfgFileName)
    return remote_cfg


def registerNewStation(cfg):
    remote_cfg = registerStation(cfg)
    if not Util.cfgEqual(remote_cfg, cfg):
        Util.updateCfg(remote_cfg, os.path.join(os.getcwd(), 'station.json'))
    return remote_cfg


def setup_periodic_tasks(station_cfg):
    for filename in os.listdir(os.path.join(os.getcwd(), station_cfg['extensionPath'])):
        if not filename.endswith(".json"):
            continue
        print("In here")
        cfg = registerNewSensor(os.path.join(os.getcwd(), station_cfg['extensionPath'], filename))

        task_settings = {
            'name': f"{cfg['uuid']}_periodic",
            'task': "SenseTask.sense",
            'args': [cfg],
            'interval': PeriodicTask.Interval(every=10, period="seconds"),
            #'crontab': Util.to_utc_crontab(PeriodicTask.Crontab(minute='10', hour='1', day_of_week='*', day_of_month='*', month_of_year='*')),
            'enabled': True
        }
        PeriodicTask.objects(name=f"{cfg['uuid']}_periodic").update(upsert=True, **task_settings)


def __main__():
    station_cfg = Util.loadConfig('station.json')

    station_cfg = registerNewStation(station_cfg)
    Util.stationID = station_cfg['uuid']

    setup_periodic_tasks(station_cfg)


__main__()
