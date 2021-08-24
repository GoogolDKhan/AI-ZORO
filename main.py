import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

# Environment variables
from dotenv import load_dotenv

load_dotenv()

# Setting engine voice
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to wish the user according the time of the day
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

    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"Sarfaraz said: {query}\n")

    except Exception as e:
        print("Say that again please...\n")
        return "None"
    return query


# Function for sending email from one account to other using smtplib
def sendEmail(toEmail, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    fromEmail = os.getenv("SENDER_EMAIL")
    server.login(fromEmail, os.getenv("PASSWORD"))
    server.sendmail(fromEmail, toEmail, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Seaching query on wikipedia
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open github" in query:
            webbrowser.open("github.com")

        elif "play music" in query:

            # give your own music directory path here
            music_dir = "C:\\Users\khans\Downloads\Top100Singles"
            songs = os.listdir(music_dir)
            print(songs)
            randIndex = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[randIndex]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sarfaraz, the time is {strTime}")

        # give any folder or file path here which you wish to open
        elif "open python programs" in query:
            folderPath = "C:\\Users\khans\Downloads\PROGRAMS\Python"
            os.startfile(folderPath)

        elif "send email to my friend" in query:
            try:
                speak("What should I say")
                content = takeCommand()
                toEmail = os.getenv("RECEIVER_EMAIL")
                sendEmail(toEmail, content)
                speak("Email sent! Sarfaraz")
            except Exception as e:
                speak("Sorry Sarfaraz. I am not able to send this email at this moment")
                print(e)
