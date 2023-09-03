import win32com.client
import speech_recognition as sr
import webbrowser
import openai
import datetime
import pyttsx3
import os
from os import startfile
from keyboard import press
from keyboard import write
from time import sleep
from pyautogui import click


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

'''these are the extra code which are not much important'''
# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# def say(text):
#     speaker.speak(text)

'''This is the function to take input from microphone and store it'''

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured , sorry from jarvis"



def whatsapp_msg(name,message):
    name = take_command()
    if name :
        print("Name : ",name)
    else:
        print("Some error occured in name , Please try again")
    message = take_command()
    if name :
        print("Message : ",message)
    else:
        print("Some error occured in message , Please try again")
    startfile("C:\\Users\\ranja\\OneDrive\\Desktop\\WhatsApp.lnk")
    sleep(2)
    write(name)
    sleep(1)
    click(x=346, y=246)
    sleep(0.5)
    write(message)
    press('enter')
name = take_command()


def whatsapp_Call(Name):
    
    print(name)
    startfile("C:\\Users\\ranja\\OneDrive\\Desktop\\WhatsApp.lnk")
    sleep(2)
    write(Name)
    sleep(1)
    click(x=346, y=246)
    sleep(0.5)
    click(x=1806, y=95)


def whatsapp_OpenChat(Name):
    startfile("C:\\Users\\ranja\\OneDrive\\Desktop\\WhatsApp.lnk")
    sleep(2)
    write(Name)
    sleep(1)
    click(x=346, y=246)


def greetings():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour <= 12:
        say("Good Morning Sir")

    elif hour >12 and hour<18:
        say("Good Afternoon Sir")

    else :
        ("Good Evening Sir")

   
greetings()


say("I'm listening ")


while True:
    
    print("Listening...")
    query = take_command()
    sites = [["YouTube","youtube.com"],["Instagram","instagram.com"],
             ["Wikipedia","wikipedia.org/"],["Google","google.com"]]
    for site in sites: 
        if f"open {site[0]}" in query:
            say(f"Opening {site[0]} sir...")
            webbrowser.open(f"https://{site[1]}")
        


    if "are you there" in query:
        say("Always for you sir")

    if "give me your details" in query:
        say('''Hi my name is Luna . I am a A.I. assistant made by
             Ashish Ranjan , in python
            version 3.9 , I am based on Open A.I.''')

    if "open brave".lower() in query.lower() :
        open("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")


    if "open word" in query:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

    if "quit" in query.lower():
        quit

    



