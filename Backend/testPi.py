import RPi.GPIO as GPIO
import time

class Relay:
    def __init__(self):
        self.PIN_RELAY_1 = 12  # GPIO12
        self.PIN_RELAY_2 = 16  # GPIO16
        self.PIN_RELAY_3 = 20  # GPIO20
        self.PIN_RELAY_4 = 21  # GPIO21

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_RELAY_1, GPIO.OUT)
        GPIO.setup(self.PIN_RELAY_2, GPIO.OUT)
        GPIO.setup(self.PIN_RELAY_3, GPIO.OUT)
        GPIO.setup(self.PIN_RELAY_4, GPIO.OUT)

    def relay_on(self, relay_number):
        pin = getattr(self, f'PIN_RELAY_{relay_number}')
        GPIO.output(pin, GPIO.HIGH)
        print(f"Turn on relay {relay_number}")
        time.sleep(0.5)

    def relay_off(self, relay_number):
        pin = getattr(self, f'PIN_RELAY_{relay_number}')
        GPIO.output(pin, GPIO.LOW)
        print(f"Turn off relay {relay_number}")
        time.sleep(1)

    def cleanup(self):
        GPIO.cleanup()
        print("Cleaned up all GPIO settings.")

# Example usage:
# relay_control = Relay()
# relay_control.setup()
# #relay_control.relay_on(1)
# relay_control.relay_off(1)
# time.sleep(5)
#relay_control.cleanup()
