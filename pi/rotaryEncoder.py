from time import sleep
from RPi import GPIO

clk = 2
dt = 3
sw = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class Callback:
    def next(self):
        pass

    def prev(self):
        pass

    def press(self):
        pass


class RotaryInput:
    def __init__(self, callback):
        self.callback = callback
        self.counter = 0
        self.clkLastState = GPIO.input(clk)
        self.swLastState = 0
        self.dtState = None
        self.clkState = None
        self.swState = None

    def run(self):
        try:
            while True:
                self.clkState = GPIO.input(clk)

                if self.clkState != self.clkLastState:
                    self.dtState = GPIO.input(dt)
                    if self.dtState != self.clkState:
                        self.counter -= 1
                        if self.counter % 2 == 0:
                            self.callback.prev()
                    else:
                        if self.counter % 2 == 1:
                            self.callback.next()
                        self.counter += 1
                self.clkLastState = self.clkState

                self.swState = GPIO.input(sw)
                if self.swLastState != self.swState:
                    self.swLastState = self.swState
                    if self.swState == 0:
                        self.callback.press()

                sleep(0.001)
        finally:
            GPIO.cleanup()
