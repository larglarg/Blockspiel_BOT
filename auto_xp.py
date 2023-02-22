import threading

import time
import pynput
from pynput.keyboard import Key
from pynput.mouse import Button


class auto_xp():

    def __init__(self):
        self.slott = None
        self.keyboard = pynput.keyboard.Controller()
        self.mouse = pynput.mouse.Controller()
        self.time_set = 10
        self.break_time = 5
        self.schwert_slot = 1
        print("autoXP wurde erstellt")
        self.to_stop = False
        self.is_running = False
        self.thread = threading.Thread(target=self.thread, args=())



    def start(self):
        self.thread.daemon = True
        self.thread.start()

    def thread(self):
        print(f"bot autoXP startet in {self.time_set} Sekunden")
        time.sleep(self.time_set)
        self.slott = str(self.schwert_slot)
        self.keyboard.press(Key.esc)
        self.keyboard.release(Key.esc)
        self.to_stop = False
        self.is_running = True
        i = 0
        print("auto_xp wurde gestarted")
        while True:
            i = i + 1
            print(f"schleife {i}")
            self.keyboard.press(self.slott)
            self.keyboard.release(self.slott)
            self.mouse.press(Button.left)
            time.sleep(0.0001)
            self.mouse.release(Button.left)
            time.sleep(self.break_time)
            self.keyboard.press("d")
            time.sleep(1)
            self.keyboard.release("d")
            time.sleep(1)
            self.keyboard.press("a")
            time.sleep(0.3)
            self.keyboard.release("a")
            if self.to_stop:
                self.to_stop = False
                self.is_running = False
                break
    def stop(self):
        self.to_stop = True
        print("autoXP wurde gestoppt")

    def stopped(self):
        return reversed(self.is_running)
