import random
import json
import torch
from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
from googletrans import Translator
import speech_recognition as sr
from translate202 import Audio_input


from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)


FILE = "data.pth"
data = torch.load(FILE)

p = 1

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()



language = googletrans.LANGUAGES
languageV = list(language.values())
langl = language.keys()


def translate_now():
    value = Audio_input()
    t1 = Translator()
    trans_text = t1.translate(value, src="english", dest=language1)
    trans_text = trans_text.text
    print(trans_text)
    return value


key = ord('f')

bot_name = "Phantom"
print("Let's chat! (say 'goodbye' to exit)")



while True:

    # sentence = "do you use credit cards?"
    # sentence = input("You: ")
    print("You: ... ")
    sentence = Audio_input()
    if sentence == "goodbye":
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
        break
    elif sentence == "phantom language":
            print("!!!! You have entered the translation Module !!!!!")
            print("\t \t To exit say EXIT")
            print("\t \t To change language just say Phantom")
            print("To which language would you like to translate?")
            language1 = Audio_input()
            while p == 1:
                if translate_now() == "Phantom":
                    print("To which language would you like to translate?")
                    language1 = Audio_input()
                if translate_now() == "exit exit":
                    break
                translate_now()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")