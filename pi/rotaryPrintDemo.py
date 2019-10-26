from pi.display import *
from pi.rotaryEncoder import *


class Printer(Callback):
    def next(self):
        print_first_line('next')

    def prev(self):
        print_first_line('prev')

    def press(self):
        print_first_line('press')


runner = RotaryInput(Printer())
runner.run()
