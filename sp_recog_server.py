import time
import speech_recognition as sr
import pyautogui
from pynput.keyboard import Key, Controller as KeyboardController, KeyCode
from pynput.mouse import Button, Controller as MouseController
import ctypes
from ctypes import wintypes


def main():
    keyboard = KeyboardController()
    mouse = MouseController()
    class MyServer():
        def do_GET():
            if __name__ == "__main__":        

                with sr.Microphone() as source:
                        r = sr.Recognizer()
                        print("Talk")
                        audio_text = r.listen(source)
                            
                        try:
                        # using google speech recognition
                            text = r.recognize_google(audio_text)
                            print("Text: "+ text)
                            
                            #if I say "die", spam run, teabag, and flashlight button#
                            if "s***" in text or "die" in text:
                                print('get fuckt')
                                keyboard.press('w')
                                time.sleep(6)
                                keyboard.release('w')
                                time.sleep(.2)
                                keyboard.press('c')
                                time.sleep(.2)
                                keyboard.release('c')
                                time.sleep(.2)
                                keyboard.press('c')
                                time.sleep(.2)
                                keyboard.release('c')
                                time.sleep(.2)
                                keyboard.press('c')
                                time.sleep(.2)
                                keyboard.release('c')
                                time.sleep(.2)
                                keyboard.press('c')
                                time.sleep(.2)
                                keyboard.release('c')
                                print('idiot')

                            if "stop" in text or "hi" in text or "high" in text:
                                mouse.scroll(0,1)
                                time.sleep(.5)
                                keyboard.press('g')
                                time.sleep(.5)
                                keyboard.release('g')
                                time.sleep(.5)
                                mouse.scroll(0,1)
                                time.sleep(.5)
                                keyboard.press('g')
                                time.sleep(.5)
                                keyboard.release('g')
                                time.sleep(.3)
                                mouse.scroll(0,1)
                                time.sleep(.3)
                                keyboard.press('g')
                                time.sleep(.3)
                                keyboard.release('g')
                                time.sleep(.3)
                                mouse.scroll(0,1)
                                time.sleep(.3)
                                keyboard.press('g')
                                time.sleep(.3)
                                keyboard.release('g')
                                time.sleep(.3)
                                mouse.scroll(0,1)
                                time.sleep(.3)
                                keyboard.press('g')
                                time.sleep(.3)
                                keyboard.release('g')
                                time.sleep(.3)
                                mouse.scroll(0,1)
                                time.sleep(.3)
                                keyboard.press('g')
                                time.sleep(.3)
                                keyboard.release('g')
                                time.sleep(.3)
                                mouse.scroll(0,1)
                                time.sleep(.3)
                                keyboard.press('g')
                                time.sleep(.3)
                                keyboard.release('g')
                                time.sleep(.3)
                                mouse.scroll(0,1)
                                time.sleep(.3)
                                keyboard.press('g')
                                time.sleep(.3)
                                keyboard.release('g')
                                time.sleep(.3)
                                mouse.scroll(0,1)
                                time.sleep(.3)
                                keyboard.press('g')
                                time.sleep(.3)
                                keyboard.release('g')
                                time.sleep(.3)
                                mouse.scroll(0,1)
                                time.sleep(.3)
                                keyboard.press('g')
                                time.sleep(.3)
                                keyboard.release('g')
                                time.sleep(.3)
                                print ('I hate you')

                            if "happy" in text:
                                print('no u')
                                keyboard.press(Key.space)
                                time.sleep(.5)
                                keyboard.release(Key.space)
                                time.sleep(.5)
                                keyboard.press(Key.space)
                                time.sleep(.5)
                                keyboard.release(Key.space)
                                time.sleep(.5)
                                keyboard.press(Key.space)
                                time.sleep(.5)
                                keyboard.release(Key.space)
                                time.sleep(.5)
                                keyboard.press(Key.space)
                                time.sleep(.5)
                                keyboard.release(Key.space)
                                time.sleep(.5)
                                keyboard.press(Key.space)
                                time.sleep(.5)
                                keyboard.release(Key.space)
                                print('ok srsly')
                                
                            
                            # #elif "journal" in text:
                            #     print ("nurd")
                            #     keyboard.press('j')
                                #Event().wait(5)
                                #time.sleep(5)
                                #print ("just checkin")
                            main()
                        except:
                            print("Sorry, I did not get that")
                            main()

    MyServer.do_GET()
    
if __name__ == '__main__':
    main()