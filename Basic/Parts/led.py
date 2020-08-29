import RPi.GPIO as GPIO


class LedManager:
    """LED Manager
    """

    def __init__(self, target_port):
        self._target_port = target_port

    def switch_on_off_led(self, state):
        GPIO.output(self._target_port, state)
