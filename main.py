'''
SKY IS THE LIMIT
Author  : Sarfaraz
Date    : 12/05/2021
Purpose : First Project
ZORO - ONE PIECE
pip install pyttsx3
pip install speechRecognition
pyaudio : pip install pipwin
          pipwin install pyaudio
pip install wikipedia
write your email password in place of passw
For email, turn on Less secure app access on your gmail account
'''


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sarfaraz")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sarfaraz")

    else:
        speak("Good Evening Sarfaraz")

    speak("I am Zoro, your assistant. Please tell me how may I help you")


def takeCommand():
    ''' It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sarfaraz said: {query}\n")

    except Exception as e:
        print("Say that again please...\n")
        return "None"
    return query


def sendEmail(toEmail, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    fromEmail = 'googoldkhan@gmail.com'
    server.login(fromEmail , 'passw')
    server.sendmail(fromEmail , toEmail, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\khans\Downloads\Top100Singles' # write your music directory path here
            songs = os.listdir(music_dir)
            print(songs)
            randIndex = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[randIndex]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sarfaraz, the time is {strTime}")

        elif 'open python programs' in query:
            folderPath = 'C:\\Users\khans\Downloads\PROGRAMS\Python' # write any folder or file you wish to open
            os.startfile(folderPath)

        elif 'send email to my friend' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                toEmail = "khansarfaraz2141@gmail.com"
                sendEmail(toEmail, content)
                speak("Email sent! Sarfaraz")
            except Exception as e:
                speak("Sorry Sarfaraz. I am not able to send this email at this moment")
                print(e)
