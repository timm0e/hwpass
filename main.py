from pykeepass import PyKeePass

from pi.rotaryEncoder import RotaryInput
from pi.test import Nav

kp = PyKeePass("Database.kdbx", password="aysxdc456")
nav = Nav(kp=kp)

inputProcessor = RotaryInput(nav)
inputProcessor.run()