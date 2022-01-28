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
from playsound import playsound

config = list(dotenv_values('.env').values())[0]

"""
Get token here: https://twitchapps.com/tmi/
"""

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'dily_dali'
token = config
channel = '#dily_dali'
pyautogui.FAILSAFE= False

def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)

def main():
    sock = socket.socket()
    keyboard = KeyboardController()
    mouse = MouseController()
    key = Key
    button = Button
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

                # if "left" in resp:
                #     keyboard.press(key.left)

                # elif "right" in resp:
                #     keyboard.press(key.right)

                # elif "go" in resp or "run" in resp:
                #     keyboard.press(key.up)

                # elif "back" in resp:
                #     keyboard.press(key.down)

                # elif "enter" in resp:
                #     keyboard.press(key.enter)
                
                # elif "crouch" in resp:
                #     keyboard.press('c')

                # elif "interact" in resp:
                #     keyboard.press('e')

                # elif "jump" in resp:
                #     keyboard.press(key.space)



                ############### 7 days to die block ##########################
                
            # if "left" in resp:
            #     playsound('./assets/Left.mp3')
            #     hold_key('a',10)

            # elif "right" in resp:
            #     playsound('./assets/Right.mp3')
            #     hold_key('d',10)

            # elif "fast" in resp:
            #     playsound('./assets/Fast.mp3')
            #     with keyboard.pressed(Key.shift):
            #         hold_key('w',15)

            # elif "walk" in resp:
            #     playsound('./assets/Walk.mp3')
            #     hold_key('w',15)

            # elif "back" in resp:
            #     # playsound('./assets/Back.mp3')
            #     hold_key('s',10)

            # elif "enter" in resp:
            #     keyboard.press(key.enter)
            
            # elif "crouch" in resp:
            #     playsound('./assets/Crouch.mp3')
            #     hold_key('c',10)

            # elif "do" in resp:
            #     playsound('./assets/Do.mp3')
            #     keyboard.press('e')
            #     keyboard.release('e')

            # elif "jump" in resp:
            #     playsound('./assets/Jump.mp3')
            #     keyboard.press(key.space)

            # elif "wallop" in resp:
            #     playsound('./assets/Wallop.mp3')
            #     mouse.press(Button.left)
            #     time.sleep(15)
            #     mouse.release(Button.left)



            ############### Super Smash Bros block ##########################

            if "left" in resp:
                playsound('./assets/Left.mp3')
                keyboard.press(key.left)
                time.sleep(.5)
                keyboard.release(key.left)

            elif "right" in resp:
                playsound('./assets/Right.mp3')
                keyboard.press(key.right)
                time.sleep(.5)
                keyboard.release(key.right)

            elif "jump" in resp:
                playsound('./assets/Jump.mp3')
                keyboard.press(key.up)
                time.sleep(.5)
                keyboard.release(key.up)

            elif "2j" in resp:
                playsound('./assets/Double Jump.mp3')
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.release(key.up)

            elif "rjmp" in resp:
                playsound('./assets/Right Jump.mp3')
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.press(key.right)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.release(key.right)
            
            elif "ljmp" in resp:
                playsound('./assets/Left Jump.mp3')
                keyboard.press(key.up)
                time.sleep(.1)
                keyboard.press(key.left)
                time.sleep(.1)
                keyboard.release(key.up)
                time.sleep(.1)
                keyboard.release(key.left)

            elif "whack" in resp:
                playsound('./assets/Wack.mp3')
                keyboard.press('x')
                time.sleep(.1)
                keyboard.release('x')

            elif "wallop" in resp:
                playsound('./assets/Wallop.mp3')
                keyboard.press('x')
                time.sleep(.1)
                keyboard.release('x')
                time.sleep(.1)
                keyboard.press('x')
                time.sleep(.1)
                keyboard.release('x')
                time.sleep(.1)
                keyboard.press('x')
                time.sleep(.1)
                keyboard.release('x')
                time.sleep(.1)
                keyboard.press('x')
                time.sleep(.1)
                keyboard.release('x')
                time.sleep(.1)

            elif "AHH" in resp:
                playsound('./assets/AHH.mp3')
                keyboard.press('z')
                time.sleep(1)
                keyboard.release('z')


                

    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    main()