import time
import RPi.GPIO as GPIO
from pushbullet import Pushbullet

# Constants
TRIG = 16
ECHO = 18
BUZZER = 7
LED = 3

# Pushbullet access token
PUSHBULLET_TOKEN = "o.kdLrCNyYmtDoDnO7ytqm9YklHOB2PRyx"

# Modes
SILENT_MODE = 0
BUZZER_MODE = 1

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

# Set up Pushbullet
pb = Pushbullet(PUSHBULLET_TOKEN)

# Set mode
mode = BUZZER_MODE

def send_notification():
    # Send a notification to the device named ‘Mobile Phone’
    device = pb.get_device(‘Mobile Phone’)
    device.push_note("Your alarm has been triggered. There is a person in your building.")
    time.sleep(1)

def motion_detection(mode):
    # Detect motion and act based on the current mode
    while True:
        i = GPIO.input(ECHO)
        if i == 0:  # Idle
            print("Idle")
            GPIO.output(BUZZER, GPIO.LOW)
            GPIO.output(LED, GPIO.LOW)
        elif i == 1:  # Motion Detected
            if mode == BUZZER_MODE:
                print("Motion has been detected. There is a person in your building.")
                GPIO.output(BUZZER, GPIO.HIGH)
                GPIO.output(LED, GPIO.HIGH)
            elif mode == SILENT_MODE:
                send_notification()

# Main loop
while True:
    GPIO.output(TRIG, False)
    motion_detection(mode)
