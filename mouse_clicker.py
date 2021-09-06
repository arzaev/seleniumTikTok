from pynput.mouse import Button, Controller
import time

mouse = Controller()


while True:
    time.sleep(2)
    mouse.position = (1125, 266)
    mouse.click(Button.left, 10)