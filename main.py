import time

import pyautogui as pyautogui
import pynput.mouse
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import threading
import logging
from screeninfo import get_monitors


def auto_xp(time_set, schwert_slot):
    print(f"Program startet in {time_set}")
    logging.info("LOG    :Skript wird gestarted")
    time.sleep(time_set)
    slott = str(schwert_slot)
    while True:
        keybord.press(slott)
        keybord.release(slott)
        mouse.press(Button.left)
        time.sleep(0.0001)
        mouse.release(Button.left)
        time.sleep(10)
        keybord.press("d")
        time.sleep(1)
        keybord.release("d")
        keybord.press("a")
        time.sleep(0.3)
        keybord.release("a")
        time.sleep(10)


def eat(food_slott, x, y):
    slott = str(food_slott)
    while True:
        color = [178, 46]
        im = pyautogui.screenshot()
        px = im.getpixel((x, y))
        if not px[0] == 178 or px[0] == 46:
            keybord.press(slott)
            keybord.release(slott)
            mouse.press(Button.right)
            time.sleep(5)
            mouse.release(Button.right)
        time.sleep(60)


logging.basicConfig(filename='main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.debug('program wird gestartet')
# keyboard und mouse erstellen
keybord = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
if keybord:
    logging.debug("Keyboard wurde gestarted")
else:
    logging.debug("Keyboard konnte nicht gestarted werden.")

time_set = 30
skript_is_running = False
food_slott = 9
print("Wilkommen beim Blockspiel BOT")
schwert_slot = 1
while True:
    inputs = input("$")
    command = inputs.split(" ")
    if command[0] == "exit":
        if skript_is_running:
            try:
                eat.kill()
                auto_xp.kill()
            except:
                print("kill thread error")

        print("ok bye")
        break

    if command[0] == "start":
        if command[2]:
            time_set = int(command[2])
        if command[1] == "autoXP":
            logging.debug("die zeit ist auf %s gesetzt", time_set)

            if skript_is_running:
                logging.info("ERROR    :es läuft bereits ein skript")
                print("es läuft bereits ein skript")
            else:
                skript_is_running = True
                thread = threading.Thread(target=auto_xp(time_set, schwert_slot), args=(1,))
                logging.info("LOG   : Skript wurde gestarted")
                thread.start()

        for monitor in get_monitors():

            if monitor.is_primary:
                x = int(monitor.width * 0.5420085971)
                y = int(monitor.height * 0.9263377345)
                eat = threading.Thread(target=eat(food_slott, x, y), args=(1,))
                eat.start()
    if command[0] == "set":
        if command[1] == "starttime":
            time_set = command[2]
        if command[1] == "food_slott":
            food_slott = command[2]
        if command[1] == "schwert_slot":
            schwert_slot = command[2]
    if command[0] == "help":
        print("exit  -> program benden")
    if command[0] == "stop":
        if not skript_is_running:
            logging.info("ERROR    :Es läuft grade kein skript")
            print("Es läuft grade kein skript")
        else:
            auto_xp.terminate()
            eat.terminate()

            if command[1] == "autoXP":
                print("Bot wurde gestopt")
    if command[0] == "kill ":
        if not skript_is_running:
            logging.info("ERROR    :Es läuft grade kein skript")
            print("Es läuft grade kein skript")
        else:
            if command[1] == "autoXP":
                auto_xp.kill()
                eat.kill()
