import RPi.GPIO as GPIO


class SwitchManager:
    """Switch Manager
    """

    def __init__(self, target_port):
        self._target_port = target_port
        GPIO.setup(target_port, GPIO.IN)

    def get_switch_status(self):
        """Fix to Add event
        :return: Switch status
        """
        return GPIO.input(self._target_port)
