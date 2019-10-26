from RPi import GPIO
from time import sleep

clk = 2
dt = 3
sw = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
clkLastState = GPIO.input(clk)
swLastState = 0
try:
    while True:
        clkState = GPIO.input(clk)

        if clkState != clkLastState:
            dtState = GPIO.input(dt)
            if dtState != clkState:
                counter -= 1
                if counter % 2 == 0:
                        print("prev")
            else:
                if counter % 2 == 1:
                        print("next")
                counter += 1
        clkLastState = clkState

        swState = GPIO.input(sw)
        if swLastState != swState:
            swLastState = swState
            if swState == 0:
                print("down")

        sleep(0.001)
finally:
    GPIO.cleanup()


