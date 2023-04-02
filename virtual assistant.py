
from datetime import datetime
import pyttsx3  # pip install pyttsx3
import datetime  # module
import speech_recognition as sr
import os
import webbrowser
import cv2
import getpass
import random
import psutil
from selenium import webdriver
import smtplib
import wikipedia


engine = pyttsx3.init()
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 100)


# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # speak(query)
        print(query)
    except:
        
        print("ready to help")

        return "None"

    return query


def voicechange():

    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', 100)


def weather():
    path = "C:\\Users\\91630\\Desktop\\all in one\\chromedriver.exe"
    driver = webdriver.Chrome(path)  # Open Google Chrome
    driver.get("https://www.google.com/search?q=weather&sxsrf=ALeKk03QvWqZoIFHP_fatDwmGN_Aqg4WOQ%3A1621845691674&ei=u2arYPHQKK2Z4-EP27-4KA&oq=weather&gs_lcp=Cgdnd3Mtd2l6EAMyDAgjECcQnQIQRhCAAjIECCMQJzIECCMQJzINCAAQsQMQgwEQyQMQQzIFCAAQkgMyCggAELEDEIMBEEMyCggAELEDEIMBEEMyBAgAEEMyCggAELEDEIMBEEMyCggAELEDEIMBEEM6BwgAEEcQsAM6BwgAELADEEM6CggAEIcCELEDEBQ6BQgAELEDOgIIADoICAAQsQMQgwE6BwgjEOoCECc6CgguEMcBEKMCEENQ8kpYmnBg3HNoAnACeASAAfcEiAGpF5IBCTAuOC40LjUtMZgBAKABAaoBB2d3cy13aXqwAQrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwixmtSC9uHwAhWtzDgGHdsfDgUQ4dUDCA4&uact=5")
    element = driver.find_element_by_class_name("wob_t TVtOme")
    print(int(element.text), 'degree Celsius')
    speak(element.text + 'degree Celsius')



# sleep(2)
# # driver.find_element_by_class_name("navbar-toggle").click()
# # sleep(2)

# driver.find_element_by_xpath(
#     "/html/body/header/nav/div[2]/div/ul/li[2]/a").click()

    elements = driver.find_element_by_id('ContentPlaceHolder1_lblpercent')
    print(int(elements.text), "%")
    speak(elements.text)

    driver.close()


def snap():

    Time = datetime.datetime.now().strftime("%H %M")
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        quit()
    cv2.imshow('',frame)
    img_name = "snap{}.png".format(Time)
    cv2.imwrite(img_name, frame)
    
def cam_using():
    
    Time = datetime.datetime.now().strftime("%H %M")
    cam = cv2.VideoCapture(0)
    ret , frame = cam.read()
    if not ret:
        print("failed to grab frame")
        quit()
    cv2.imshow('',frame)
    img_name = "opencv_frame_{}.png".format(Time)
    cv2.imwrite(img_name, frame)
    speak('shuting down computer')
    # os.system("shutdown /s /t 0")
    quit()
    

    


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage+"percent sir")
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("and Battery is at")
    speak(battery.percent)
    speak("percent sir")
    print("battery is at:" + str(battery.percent) + "percent sir")
    if battery.percent <= 30:
        speak("charge it now")


def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("TODAY IS")
    print(date)
    print(month)
    print(year)
    speak(date)
    speak(month)
    speak(year)


def time():
    Time = datetime.datetime.now().strftime("%H")
    timetwo = datetime.datetime.now().strftime("%M")
    # c = int(timetwo)
    b = int(Time)
    if b >= 13:
        print(b - 12, end=':')
        print(timetwo, end=' ')
        print("pm")
        speak(b - 12)
        speak(timetwo)
        speak("pm")
    else:
        print(Time + timetwo + "am")
        speak(Time)
        speak(timetwo)


def password():
    print('password plz sir')
    speak('hi there')
    code = int(getpass.getpass())
    if code == 9441:
        print('login successful sir')
        speak('login successful sir')

    else:
        speak('wrong password ')
        print('wrong password')
        cam_using()


def relax():
    while (True):

        query = takeCommand().lower()
        if 'come on' in query or 'wake up' in query or 'jarvis' in query or 'hai' in query or 'hey jarvis' in query:
            speak('ya am ready for you')
            jarvis()
        else:
            relax()


# welcome function
def wishme():
    speak("Welcome Back ")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('volume', 1)

    speak("I AM at your service")





def jarvis():
    

    while (True):

        query = takeCommand().lower()

        if ('cpu' in query or 'pc' in query or "battery" in query):
            try:
                voicechange()
                cpu()
            except:
                jarvis()

        elif("time" in query):
            voicechange()
            time()


        elif("date" in query or "day" in query):
            voicechange()
            date()



        elif('my attendance' in query or 'attendance' in query):
            try:
                voicechange()
                attendance()
            except:
                jarvis()



        elif ('send' in query or 'mail' in query):
            try:
                voicechange()
                sendingmail()
            except:
                jarvis()



        elif('bomb' in query or 'bomb it' in query):
            voicechange()
            smsbomber()



        elif("off" in query or 'bye' in query or 'relax' in query or 'go off' in query):
            voicechange()
            speak("bye bye")
            speak('take care')
            voicechange()
            relax()



        elif("take a snap" in query or "snap" in query):
            try:
                snap()
            except:
                jarvis()
            
            
        elif("close my math class" in query or "class" in query):
            time.sleep(2700)
            os.system("shutdown /s /t 0")



        elif ('wikipedia' in query or 'what' in query or 'who' in query or 'when' in query or 'where' in query):
            voicechange()
            speak("searching... in wikipedia...")
            try:
                result = wikipedia.summary(query, sentences=1)
                print(query)
                print(result)
                speak(result)
            except:
                voicechange()
                speak('cannot find in wikipedia')
                jarvis()
                
        elif('love you' in query or 'good' in query or 'very good' in query or 'your are smart' in query):
            voicechange()
            speak("thank you")
            speak("its all because of you ")
            speak('love you')

        elif ("developer" in query or "tell me about your developer" in query or "father" in query or "who develop you" in query or "developer" in query):
            voicechange()
            speak(
                "WE ARE ASSISTANTS OF CHARAN  created by charan in 2020 our names are  CHTHERINE,  JAMES , LINDA , RICHARD,  HEERA ,  RAVI,  MARK  , HEMANTH , KALPANA , CORTANA ,HAZEL, DAVID, ZIRA, WE all belongs to CHARAN'S family")

        elif 'open my search' in query:
            voicechange()
            speak("opening...")
            path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave'
            os.startfile(path)


        elif 'open google' in query:
            voicechange()
            speak('opening google')
            webbrowser.open_new("https://www.google.com")


        elif 'open youtube' in query:
            voicechange()
            speak('opening youtube')
            webbrowser.open_new("https://www.youtube.com")


        elif ('open group' in query or 'open whatsapp' in query):
            voicechange()
            speak('opening whatsapp')
            path = "C:\\Users\\91630\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(path)


        elif ('open vs code' in query):
            voicechange()
            speak('opening v s code')
            path = "C:\\Users\\91630\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        
        elif ("search" in query or "google" in query):
            webbrowser.open_new(query)
            
            
            
        elif ("open my website" in query or "my site" in query):
            webbrowser.open("C:\\Users\\91630\\Desktop\\unschool full stack\\bootstarp4")
            
            
if __name__ == '__main__':
    password()
    wishme()
    jarvis()
