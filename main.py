import pynput
import threading
import logging
from screeninfo import get_monitors
import auto_xp
import eat

from auto_xp import *
from eat import *

logging.basicConfig(filename='main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.debug('program wird gestartet')

# keyboard und mouse erstellen
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
if keyboard:
    logging.debug("Keyboard wurde gestartet")
else:
    logging.debug("Keyboard konnte nicht gestartet werden.")

skript_is_running = False
print("Wilkommen beim Blockspiel BOT")

while True:
    inputs = input("$")
    command = inputs.split(" ")
    if command[0] == "exit":
        if skript_is_running:
            eatx.stop()
            auto_XP_x.stop()

        print("ok bye")
        break

    if command[0] == "start":
        if command[2]:
            time_set = int(command[2])
        if command[1] == "autoXP":
            auto_XP_x = None
            logging.debug("die zeit ist auf %s gesetzt", time_set)

            if skript_is_running:
                logging.info("ERROR    :es läuft bereits ein skript")
                print("es läuft bereits ein skript")
            else:
                skript_is_running = True
                auto_XP_x = auto_xp()
                auto_XP_x.start()

                logging.info("LOG   : Skript wurde gestarted")

        for monitor in get_monitors():

            if monitor.is_primary:
                eatx = eat()
                auto_XP_x.x = int(monitor.width * 0.5420085971)
                auto_XP_x.y = int(monitor.height * 0.9263377345)
                eatx.start()

    if command[0] == "list":
        print(eatx.is_running)
        print(auto_XP_x.is_running)

    if command[0] == "set":
        if command[1] == "starttime":
            eatx.time_set = int(command[2])
            logging.info("LOG   : Startzeit wurde geändert auf %s Sekunden", command[2])
