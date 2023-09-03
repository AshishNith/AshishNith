import pyttsx3
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
import speech_recognition as sr


# def take_command():
#     r = sr.Recognizer()
#     print("Listening....")
#     with sr.Microphone() as source:
#         # r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language="en-in")
#         return query  # Return the recognized query on success
#     except Exception as e:
#         print("Some error occurred:", e)
#         return "Some error occurred"  # Return an error message

def whatsapp_msg(name,message):
    # name = take_command()
    # if name :
    #     print("Name : ",name)
    # else:
    #     print("Some error occured in name , Please try again")
    # message = take_command()
    # if name :
    #     print("Message : ",message)
    # else:
    #     print("Some error occured in message , Please try again")
    startfile("C:\\Users\\ranja\\OneDrive\\Desktop\\WhatsApp.lnk")
    sleep(2)
    write(name)
    sleep(1)
    click(x=346, y=246)
    sleep(0.5)
    write(message)
    press('enter')
# name = take_command()

def whatsapp_Call(Name):
    
    print(Name)
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



# whatsapp_msg('ajitesh', 'hello this is a test message')
whatsapp_Call("satvik")

# whatsapp_Call(name)



















