import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, os
import subprocess as sub

name = 'isa'
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
sites = {
    'google': 'google.com',
    'youtube': 'youtube.com',
    'facebook': 'facebook',
    'whastapp': 'web.whatsapp.com'
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = None
    try:
        with sr.Microphone() as source:
            print("Listening ...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="en-US")
            rec = rec.lower()
            if name in rec:
                print(name)
                rec = rec.replace(name, '')
    except:
        pass
    return rec

def run():
    while True:
        rec = listen()
        try:
            if 'play' in rec:
                music = rec.replace('play', '')
                print("Playing " + music)
                talk("Playing " + music)
                pywhatkit.playonyt(music)

            elif 'search' in rec:
                search = rec.replace('search', '')
                wikipedia.set_lang('en')
                wiki = wikipedia.summary(search, 1)
                print(search + ": " + wiki)
                talk(wiki)

            elif 'open' in rec:
                for site in sites:
                    if site in rec:
                        sub.call(f'start chrome.exe {sites[site]}', shell=True)
                        talk(f'Opening {sites[site]}')
        except:
            talk("I dont understand, please try again...")

if __name__ == '__main__':
    run()