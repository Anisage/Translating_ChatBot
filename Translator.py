from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
from googletrans import Translator
import speech_recognition as sr
from translate202 import Audio_input
from TranslatorConn import combo2

value = Audio_input()


language = googletrans.LANGUAGES
languageV = list(language.values())
langl = language.keys()


root = Tk()
root.title("Translator")
root.geometry("1080x500")
root.configure(background="")


# def label_change():
#     c = combo1.get()
#     c1 = combo2.get()
#     label1.configure(text=c)
#     label2.configure(text=c1)
#     root.after(1000, label_change)


def translate_now():
    t1 = Translator()
    trans_text = t1.translate(value, src="en", dest=combo2)
    trans_text = trans_text.text
    print(trans_text)




# first combobox
#
# combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="")
# combo1.place(x=-1000, y=0)
# combo1.set("ENGLISH")
#
# label1 = Label(root, text="", font="segoe 30 bold", bg="white", width=0, bd=5, relief=GROOVE)
# label1.place(x=-1000, y=0)
#
# #first frame
#
# f = Frame(root, bg="green", bd=5)
# f.place(x=0, y=0, width=0, height=0)
#
# text1 = Text(f, font="Robote 20", bg="yellow", relief=GROOVE, wrap=WORD)
# text1.place(x=0, y=0, width=0, height=0)
#
# scrollbar1 = Scrollbar(f)
# scrollbar1.pack(side="right", fill="y")
#
# scrollbar1.configure(command=text1.yview)
# text1.configure(yscrollcommand=scrollbar1.set)
#
# #second combobox
#
# combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
# combo2.place(x=430, y=20)
# combo2.set("SELECT LANGUAGE")
#
# label2 = Label(root, text="English", font="segoe 30 bold", bg="blue", width=18, bd=5, relief=GROOVE)
# label2.place(x=320, y=50)
#
# #second frame
#
# f1 = Frame(root, bg="green", bd=5)
# f1.place(x=320, y=118, width=440, height=210)
#
# text2 = Text(f1, font="Robote 20", bg="yellow", relief=GROOVE, wrap=WORD)
# text2.place(x=0, y=0, width=430, height=200)
#
# scrollbar2 = Scrollbar(f1)
# scrollbar2.pack(side="right", fill="y")
#
# scrollbar2.configure(command=text2.yview)
# text2.configure(yscrollcommand=scrollbar2.set)

# # translate button
# translate = Button(root, text="Translate", font=("Roboto", 15),  activebackground="purple", cursor="hand2",
#                    bd=1, width=10, height=2,  bg='red', fg="white", command=translate_now)
# translate.place(x=476, y =350)


# label_change()
# translate_now()

