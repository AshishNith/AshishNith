import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()333




while True :
    a = int(input("Enter the 1st number"))
    c = input("Enter the sign\n+ for sum\n- for difference\n* for multiplication\n/ for division\n % for remainder\n// for GIF of Quotient")
    b = int(input("Enter The 2nd number")) 
    
    if c == "+":
        speak(a+b)
        print(a+b)
    elif c == "-":
        speak(a-b)
        print(a+b)
    elif c == "*":
        speak(a*b)

    elif c == "/":
        speak(a/b)

    elif c == "%":
        speak(a%b)
    elif c == "//":
        speak(a//b)
    else :
        speak("Invalid Command")
        