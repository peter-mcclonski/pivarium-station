import requests

server = "http://192.168.1.182:8080"


def registerSensor(cfg: dict):
    r = requests.put(f"{server}/sensor/register", json=cfg)

    return r.json()


def registerStation(cfg: dict):
    r = requests.put(f"{server}/station/register", json=cfg)
    return r.json()


def sendStatus(statusData: dict):
    r = requests.put(f"{server}/sensor/status", json=statusData)
    return r.json()


def requestUUID():
    r = requests.get(f"{server}/reqUuid")
    return r.json()['uuid']
