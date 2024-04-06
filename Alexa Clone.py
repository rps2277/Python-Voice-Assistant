import os
import webbrowser
import threading
import subprocess
import speech_recognition as sr 
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache.')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open' in command:
        if 'file' in command:
            file_name = command.replace('open File', '').strip()
            os.startfile(CN)
        elif 'application' in command:
            app_name = command.replace('open Application', '').strip()
            os.startfile( chrome)
        elif 'folder' in command:
            folder_name = command.replace('open folder', '').strip()
            subprocess.Popen(f'explorer {folder_name}')
        else:
            talk('I am not sure what you want me to open.')
    else:
        talk('Please say the command again.')

while True:
    run_alexa()

# Modify run_alexa to run in a separate thread
def run_alexa_in_thread():
    while True:
        run_alexa()

# Start the thread
alexa_thread = threading.Thread(target=run_alexa_in_thread)
alexa_thread.start()

# Main thread continues to execute other tasks or commands
while True:
    # Your main program logic here
    pass
