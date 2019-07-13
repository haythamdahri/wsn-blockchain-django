from django.apps import AppConfig


class WirelesssensornetworkConfig(AppConfig):
    name = 'WirelessSensorNetwork'

    def ready(self):
        print('HELLO WORLD!')
