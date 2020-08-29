import RPi.GPIO as GPIO
import time


class BuzzerManager:
    """Buzzer Manager
    """

    def __init__(self, target_port):
        self._target_port = target_port

    def turn_on_buzzer(self):
        for i in range(2):
            GPIO.output(self._target_port, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(self._target_port, GPIO.LOW)
            time.sleep(0.1)

    def turn_off_buzzer(self):
        GPIO.output(self._target_port, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(self._target_port, GPIO.LOW)
