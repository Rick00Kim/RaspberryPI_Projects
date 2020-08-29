import RPi.GPIO as GPIO

""" Define All ports
"""
LED_RED_PORT = 16
BUZZER_PORT = 19
SWITCH_1_PORT = 13

""" Define GPIO Base settings
"""
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
""" Define GPIO I/O Settings
"""
