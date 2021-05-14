import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', rate=20)

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 1 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour<18 :
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("Welcom Back!")
    
    speak("nancy is at your service !!, tell me how can i help you?") 

# wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that Again Please...")
        return "None"
    return query

# speak(takeCommand())

# if takeCommand == "exit":
#     speak("ok sir have a good a day!!")
# else:
#     for i in range(1,5):
#         speak(takeCommand())

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:/Aj Ay/myProject/Project3/screenshot.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' +usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if  'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("I am searching..your Query")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'open chrome' in query:
            speak("what should i search for you?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif 'logout the system' in query:
            os.system("shutdown -l")

        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart the system' in query:
            os.system("shutdown /r /t 1")
        
        elif 'play songs' in query:
            songs_dir = 'D:/Aj Ay/Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0])) 

        elif 'remember that' in query:
            speak('what should i remember?')
            data = takeCommand()
            speak('you said me to remember that'+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak('you said me to remember that' +remember.read())
        
        elif 'take screenshot' in query:
            screenshot()
            speak('screenshot done!!')
        
        elif 'cpu usage' in query:
            cpu()
        
        elif 'tell me some jokes' in query:
            print(jokes())

        elif 'who are you' in query:
            speak('i am Nancy')

        elif 'who invent you' in query:
            speak("i am created by Ajay")

        elif 'nancy' in query:
            speak('haa bool...kya kaam hai?')

        elif 'ok shut down' in query:
            quit()

        elif 'what is your age' in query:
            speak('aapne kaam Say kaam rhak')

        


