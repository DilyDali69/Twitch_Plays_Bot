from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import speech_recognition as sr

hostName = "localhost"
serverPort = 8080

def main():
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
                            if "but" in text:
                                print ("haha you said butt")
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