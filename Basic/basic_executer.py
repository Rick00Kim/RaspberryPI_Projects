import RPi.GPIO as GPIO
import initialize as initializer
from Parts.buzzer import BuzzerManager
from Parts.led import LedManager
from Parts.switch import SwitchManager


def call_main_module():
    """Main Module
    """
    state = False
    buzzer_manager = BuzzerManager(initializer.BUZZER_PORT)
    led_manager = LedManager(initializer.LED_RED_PORT)
    switch_manager = SwitchManager(initializer.SWITCH_1_PORT)

    try:
        while True:
            switch_io = switch_manager.get_switch_status()
            if switch_io == 1:
                state = not state
                led_manager.switch_on_off_led(state)
                if state is True:
                    buzzer_manager.turn_on_buzzer()
                else:
                    buzzer_manager.turn_off_buzzer()

    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    call_main_module()
