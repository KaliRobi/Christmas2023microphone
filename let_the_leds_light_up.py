import RPi.GPIO as GPIO
import time


LED_PIN = 17
MICROPHONE_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(MICROPHONE_PIN, GPIO.IN)


def sound_detected(channel):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)


GPIO.add_event_detect(MICROPHONE_PIN, GPIO.RISING, callback=sound_detected)


try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()