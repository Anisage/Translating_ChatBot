from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
from googletrans import Translator
import speech_recognition as sr
from translate202 import Audio_input
# from chat import language1

language = googletrans.LANGUAGES
languageV = list(language.values())
langl = language.keys()


def translate_now():
    value = Audio_input()
    t1 = Translator()
    trans_text = t1.translate(value, src="english", dest="spanish")
    trans_text = trans_text.text
    print(trans_text)
