import RPi.GPIO as GPIO
import time

class Relay:
    def __init__(self):
        # Initialize relay pins
        self.PIN_RELAY_1 = 12 # GPIO12
        self.PIN_RELAY_2 = 16 # GPIO16
        self.PIN_RELAY_3 = 20 # GPIO20
        self.PIN_RELAY_4 = 21 # GPIO21
        self.relay_states = {1: GPIO.LOW, 2: GPIO.LOW, 3: GPIO.LOW, 4: GPIO.LOW}

    def setup_relays(self):
        # Set GPIO mode
        GPIO.setmode(GPIO.BCM)
        # Setup GPIO pins as output
        GPIO.setup(self.PIN_RELAY_1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.PIN_RELAY_2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.PIN_RELAY_3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.PIN_RELAY_4, GPIO.OUT, initial=GPIO.LOW)

    def relay_on(self, relay_number):
        print(f"Turn on relay {relay_number}")
        pin = getattr(self, f'PIN_RELAY_{relay_number}')
        GPIO.output(pin, GPIO.HIGH)
        self.relay_states[relay_number] = GPIO.HIGH

    def relay_off(self, relay_number):
        print(f"Turn off relay {relay_number}")
        pin = getattr(self, f'PIN_RELAY_{relay_number}')
        GPIO.output(pin, GPIO.LOW)
        self.relay_states[relay_number] = GPIO.LOW

    def toggle_relay(self, relay_number):
        current_state = self.relay_states[relay_number]
        new_state = GPIO.LOW if current_state == GPIO.HIGH else GPIO.HIGH
        GPIO.output(getattr(self, f'PIN_RELAY_{relay_number}'), new_state)
        self.relay_states[relay_number] = new_state
        print(f"Toggled relay {relay_number} to {'ON' if new_state == GPIO.HIGH else 'OFF'}")

# Example usage:
relay_control = Relay()
relay_control.setup_relays()
relay_control.toggle_relay(1)  # This will turn the relay 1 ON if it was OFF
time.sleep(1)
relay_control.toggle_relay(1)  # This will turn the relay 1 OFF if it was ON
GPIO.cleanup()  # Clean up at the end of the program
