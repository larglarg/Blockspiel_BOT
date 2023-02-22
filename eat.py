import time
import pyautogui as pyautogui
import pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import threading
from screeninfo import get_monitors


class eat(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
        regularly for the stopped() condition."""

    def __init__(self):
        self.run = None
        self.runs = None
        super().__init__()
        self.color = None
        self.slott = None
        print("eat wurde erstellt")
        self.time_set = 1
        self.break_time = 50
        self.food_slott = 9
        self.x = 0
        self.y = 0
        self._stop_event = threading.Event()
        self.to_stop = False
        self.eat_main_tread = threading.Thread(target=self.threads, args=())
        self.thread = threading.Thread(target=self.thread, args=())
        self.in_progress = False

    def start(self):
        self.eat_main_tread.daemon = True
        self.eat_main_tread.start()

    def threads(self):
        while True:
            time.sleep(2)


            self.thread.start()
            self.in_progress = True
            while self.thread:
                time.sleep(2)






    def thread(self):
        self.keybord = pynput.keyboard.Controller()
        self.mouse = pynput.mouse.Controller()
        print(f"eat startet in {self.time_set}")
        print("eat wurde gestarted")
        time.sleep(self.time_set)
        self.slott = str(self.food_slott)
        self.color = [178, 46]

        time.sleep(1)
        im = pyautogui.screenshot()
        px = im.getpixel((self.x, self.y))
        print(px[0])#r
        print(px[1])#g
        print(px[2])#b
        if not px[0] == self.color[0]:
            if not px[0] == self.color[1]:
                self.keybord.press(self.slott)
                self.keybord.release(self.slott)
                self.mouse.press(Button.right)
                time.sleep(1.61)
                self.mouse.release(Button.right)
            else:
                print("genug essen 46")
        else:
            print("genug essen 178")
            if self.to_stop:
                self.to_stop = False
        self.in_progress = False





    def stop(self):
        self.to_stop
        print("eat wurde gestopt")

    def stopped(self):
        return reversed(self.to_stop)
