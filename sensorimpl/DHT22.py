import adafruit_dht
import board

from Sensor import Sensor


class DHT22(Sensor):
    dht_device: adafruit_dht.DHT22

    def __init__(self, uuid, stype, connType, hwAddress):
        Sensor.__init__(self, uuid, stype, connType, hwAddress)
        self.dht_device = adafruit_dht.DHT22(board.D4, use_pulseio=False)

    def getStatus(self):
        try:
            return {
                'humidity': self.dht_device.humidity,
                'temperature': self.dht_device.temperature
            }
        except Exception as e:
            return {}

