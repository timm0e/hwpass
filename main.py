import os

# Force RPI3 since it isn't detected automatically on ubuntu
os.environ["BLINKA_FORCECHIP"] = "BCM2XXX"
os.environ["BLINKA_FORCEBOARD"] = "RASPBERRY_PI_3B"

from pykeepass import PyKeePass

from pi.rotaryEncoder import RotaryInput
from pi.view import Nav

kp = PyKeePass("Database.kdbx", password="aysxdc456")
nav = Nav(kp=kp)

inputProcessor = RotaryInput(nav)
inputProcessor.run()
