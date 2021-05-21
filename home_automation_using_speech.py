import speech_recognition as sr
import serial
import time
ArduinoSerial=serial.Serial('com7',9600)
time.sleep(2)
r=sr.Recognizer()
while 1:
    with sr.Microphone() as source:
        print("wait..calibrating microphone")
        r.adjust_for_ambient_noise(source, duration=5)
        print("Speak")
        audio=r.listen(source)
    try:
        text = r.recognize_google(audio)
        if "lights on" in text:
            print("Led turned on")
            ArduinoSerial.write('1'.encode())
        if "lights off" in text:
            ArduinoSerial.write('0'.encode())
            print("Led turned off")
    except LookupError:                           
        print("Could not understand audio")  

