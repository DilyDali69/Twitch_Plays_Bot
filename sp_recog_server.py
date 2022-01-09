from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import speech_recognition as sr
import pyautogui
from pynput.keyboard import Key, Controller as KeyboardController, KeyCode
from pynput.mouse import Button, Controller as MouseController

hostName = "localhost"
serverPort = 8080

def main():
    keyboard = KeyboardController()
    mouse = MouseController()
    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            if __name__ == "__main__":        
            
                webServer = HTTPServer((hostName, serverPort), MyServer)
                print("Server started http://%s:%s" % (hostName, serverPort))

                with sr.Microphone() as source:
                        r = sr.Recognizer()
                        print("Talk")
                        audio_text = r.listen(source)
                            
                        try:
                        # using google speech recognition
                            text = r.recognize_google(audio_text)
                            print("Text: "+ text)
                            
                            #if I say "die", spam run, teabag, and flashlight button#
                            if "die" in text:
                                print ("get fuckt")
                                pyautogui.press('w')
                                pyautogui.press('c')
                                pyautogui.press('f')
                                #keyboard.press('w', 'c', 'f')
                                # keyboard.keyUp('w')
                                keyboard.press('c')
                                # keyboard.keyUp('c')
                                keyboard.press('c')
                                # keyboard.keyUp('c')
                                keyboard.press('f')
                                # keyboard.keyUp('f')
                                keyboard.press('f')
                                # keyboard.keyUp('f')
                            
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

                        try:
                            webServer.serve_forever()
                        except: webServer.server_close()
                        print("Server stopped.")
    MyServer.do_GET(BaseHTTPRequestHandler)
    
if __name__ == '__main__':
    main()