from pyparsing import Word
import pyttsx3
from PyDictionary import PyDictionary

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)

engine.say("hello sir, enter the word ")
engine.runAndWait()

dict=PyDictionary()

while True:
    query = input("\nenter word: ")
    try:
        word = dict.meaning(query)
        for meaning in word:
            print(f"\nMeaning of {query} is {str(word[meaning])}\n")
            engine.say(f"\nMeaning of {query} is {str(word[meaning])}\n")
            engine.runAndWait()
            break
    except:
        print("\nSorry sir, please try again\n")
        engine.say("\nSorry sir, please try again")
        engine.runAndWait()