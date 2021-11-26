#import adafruit_dht
#import board
from Sensor import Sensor


class DHT22(Sensor):
    #dht_device: adafruit_dht.DHT22

    def __init__(self, cfg):
        super().__init__(cfg)
        #self.dht_device = adafruit_dht.DHT22(board.D4, use_pulseio=False)

    def getStatus(self):
        base = super().getStatus()
        try:
            base['status'] = {
                'humidity': 40.2,
                'temperature': 32.1
                #'humidity': self.dht_device.humidity,
                #'temperature': self.dht_device.temperature
            }
            return base
        except Exception as e:
            return None