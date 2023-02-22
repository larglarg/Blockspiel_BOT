import time

import pyautogui as pyautogui
import pynput.mouse
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import threading
import logging
from screeninfo import get_monitors


def auto_xp(time_set, schwert_slot):
    logging.info("LOG    :Skript wird gestarted")
    print(f"Program startet in {time_set}")
    time.sleep(time_set)
    slott = str(schwert_slot)
    keybord.press(Key.esc)
    keybord.release(Key.esc)
    while True:
        keybord.press(slott)
        keybord.release(slott)
        mouse.press(Button.left)
        time.sleep(0.0001)
        mouse.release(Button.left)
        time.sleep(3)
        keybord.press("d")
        time.sleep(1)
        keybord.release("d")
        time.sleep(1)
        keybord.press("a")
        time.sleep(0.3)
        keybord.release("a")
        time.sleep(3)


def eat(time_set, food_slott, x, y):
    print(f"eat startet in {time_set}")
    time.sleep(time_set)
    slott = str(food_slott)
    while True:
        time.sleep(5)
        color = [178, 46]
        im = pyautogui.screenshot()
        px = im.getpixel((x, y))
        print(px[0])
        if not px[0] == 178:
            keybord.press(slott)
            keybord.release(slott)
            mouse.press(Button.right)
            time.sleep(1.61)
            mouse.release(Button.right)
        if not px[0] == 46:
            keybord.press(slott)
            keybord.release(slott)
            mouse.press(Button.right)
            time.sleep(1.61)
            mouse.release(Button.right)



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
                eat_thread.kill()
                auto_xp_thread.kill()
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
                auto_xp_thread = threading.Thread(target=auto_xp, args=(time_set, schwert_slot))
                auto_xp_thread.daemon = True
                logging.info("LOG   : Skript wurde gestarted")
                auto_xp_thread.start()
                print("auto_xp wurde gestarted")

        for monitor in get_monitors():

            if monitor.is_primary:
                x = int(monitor.width * 0.5420085971)
                y = int(monitor.height * 0.9263377345)
                eat_thread = threading.Thread(target=eat, args=(time_set, food_slott, x, y))
                eat_thread.daemon = True
                eat_thread.start()
                print("eat wurde gestarted")
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
            auto_xp_thread.terminate()
            eat_thread.terminate()

            if command[1] == "autoXP":
                print("Bot wurde gestopt")
    if command[0] == "kill ":
        if not skript_is_running:
            logging.info("ERROR    :Es läuft grade kein skript")
            print("Es läuft grade kein skript")
        else:
            if command[1] == "autoXP":
                auto_xp_thread.kill()
                eat_thread.kill()
