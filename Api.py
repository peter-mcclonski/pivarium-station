import requests
import json

server = "http://192.168.1.182:8080"


def putSensorList(stationID: str, sensorDict):
    for sid in sensorDict.keys():
        sensor = sensorDict[sid]
        print(f"Registering Sensor: {sensor.uuid}")
        r = requests.put(f"{server}/sensor/register", json={
            "stationID": stationID,
            "stype": sensor.stype,
            "uuid": sensor.uuid
        })
        print(r)

    return r.json()


def registerStation(stationID: str):
    print(f"Registering station: {stationID}")
    r = requests.put(f"{server}/station/register", json={
        "uuid": stationID
    })
    print(r)

    return r.json()


def requestUUID():
    r = requests.get(f"{server}/reqUuid")
    return r.json()['uuid']
