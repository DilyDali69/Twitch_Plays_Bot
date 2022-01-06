import socket
import logging
import emoji
import pandas
import time
import pyautogui
import os

from emoji import demojize
from pynput.keyboard import Key, Controller as KeyboardController, KeyCode
from pynput.mouse import Button, Controller as MouseController
from dotenv import load_dotenv
from dotenv import dotenv_values
from pathlib import Path

config = list(dotenv_values('.env').values())[0]

"""
Get token here: https://twitchapps.com/tmi/
"""

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'dily_dali'
token = config
channel = '#dily_dali'

def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)

def main():
    sock = socket.socket()
    keyboard = KeyboardController()
    mouse = MouseController
    key = Key
    dotenv_path = Path(r'C:\Users\morge\Desktop\Twitch_Plays_Bot\.env')
    load_dotenv(dotenv_path=dotenv_path)
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\r\n".encode('utf-8'))

    try:
        while True:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                # sock.send("PONG :tmi.twitch.tv\n".encode('utf-8')) | sock.send("PONG\n".encode('utf-8'))
                sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
            elif len(resp) > 0:
                
                logging.info(demojize(resp))
                print(resp)
                
                #hold key look like this
                
                #if "jump" in resp:
                   # hold_key('a',1)
                   # print("simulate key") #for testing purposes
                
                #press key look like this
                
                #a-z keys done like this
                #elif "fart" in resp:
                    #keyboard.press('b')


                #############################
                ###general#chat#commands###

                if "left" in resp:
                    keyboard.press(key.left)

                elif "right" in resp:
                    keyboard.press(key.right)

                elif "go" in resp or "run" in resp:
                    keyboard.press(key.up)

                elif "back" in resp:
                    keyboard.press(key.down)

                elif "enter" in resp:
                    keyboard.press(key.enter)
                
                elif "crouch" in resp:
                    keyboard.press('c')

                elif "interact" in resp:
                    keyboard.press('e')

                elif "jump" in resp:
                    keyboard.press(key.space)


    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    main()