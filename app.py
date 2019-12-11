# GrovePi + Grove Ultrasonic Ranger
import time
import requests
from grovepi import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

PORT = 4
BOT_ID = '827686452:AAG5aeN-I1GdBWDOAggMTZS65iJJthm0pNU'
CHAT_ID = '-1001251595992'
MSG = 'Sensor has been triggered'
URL = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(BOT_ID, CHAT_ID, MSG)

while True:
    try:
        # Read distance value from Ultrasonic
        reading = ultrasonicRead(PORT)
        print(reading)
        if reading <= 150:
            req = requests.get(URL)
        time.sleep(1)

    except TypeError:
        print("Error")
    except IOError:
        print("Error")
