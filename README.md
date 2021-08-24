# ZORO

- User can use this program for opening applications such as google chrome, VS Code or any folder on their machine.
- One can open any url such as google, youtube, github etc and search their query in wikipedia.
- An email can be easily sent to your friend from your account using this application.
- This application also speaks the current time and plays music on their system.

## Running

### Installation of dependencies

#### To install required modules run

```bash
  pip install pyttsx3
  pip install speechRecognition
  pip install wikipedia
  pip install python-dotenv
```
for using pyaudio
```bash
  pip install pipwin
  pipwin install pyaudio
```
### Note

- write your email password in place of passw
- To use email, turn on Less secure app access on your gmail account

## Know more about project

#### What is pyttsx3?

- A python library that will help us to convert text to speech. In short, it is a text-to-speech library.
- It works offline, and it is compatible with Python 2 as well as Python 3.

#### What is sapi5?

- Microsoft developed speech API.
- Helps in synthesis and recognition of voice.

#### What Is VoiceId?

- Voice id helps us to select different voices.
- voice[0].id = Male voice 
- voice[1].id = Female voice

#### What is smtplib?

- Simple Mail Transfer Protocol (SMTP) is a protocol that allows us to send emails and route emails between mail servers. An instance method called sendmail is present in the SMTP module. This instance method allows us to send an email.  It takes 3 parameters:
- The sender: Email address of the sender.
- The receiver: T Email of the receiver.
- The message: A string message which needs to be sent to one or more than one recipient.

## Author

- This project is inspired by [CodeWithHarry](https://youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME)

- Dated : 12-05-2021
