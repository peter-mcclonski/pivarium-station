import adafruit_dht
import board

from Sensor import Sensor

boardLookup = {
    '0': board.GPIO0,
    '1': board.GPIO1,
    '2': board.GPIO2,
    '3': board.GPIO3,
    '4': board.GPIO4,
}


class DHT22(Sensor):
    dht_device: adafruit_dht.DHT22

    def __init__(self, uuid, stype, connType, hwAddress):
        super.__init__(self, uuid, stype, connType, hwAddress)
        self.dht_device = adafruit_dht.DHT22(boardLookup[self.hwAddress])

    def getStatus(self):
        if self.stype == 'humidity':
            return self.dht_device.humidity
        else:
            return self.dht_device.temperature
