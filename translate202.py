from tkinter import *
from tkinter import ttk, messagebox
import speech_recognition as sr


r = sr.Recognizer()
m = sr.Microphone()

def Audio_input():
    while True:
        with m as source: r.adjust_for_ambient_noise(source)
        with m as source: audio = r.listen(source)
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"{}".format(value).encode("utf-8"))

            else:  # this version of Python uses unicode for strings (Python 3+)
                # print(format(value))
                print("You:", value)
                return value


        except sr.UnknownValueError:
            print("Phantom L", "Didn't catch that.Please try again")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

