from time import sleep
import webbrowser,os
import psutil
import pyttsx3,pyjokes
import speech_recognition as sr



engine = pyttsx3.init('sapi5')
voice = engine.getProperty("voices")
engine.setProperty('voice',voice[0].id)


def is_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == task:
            return True
    return False

def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
        
    
    
    try:
        print("Recognizing.....")
        
        query = r.recognize_google(audio,language="en-in")
        print(f"user said {query}")
       
        speak(query)
        sleep(2)
       

    except Exception as e: 
        return ''
    return query.lower()



while True:
    print('HELLO I AM JARVIS')
    speak('HELLO I AM JARVIS')

    query = takecommand()
    if "open notepad" in query:
        speak("Opening Notepad ")
        path="C:\\Windows\\System32\\notepad.exe"
        os.startfile(path)
    elif "close notepad" in query:
        task = 'notepad.exe'
        if is_running():
            speak("closing notepad ")
            os.system('taskkill /f /im notepad.exe')
            
        else:
            speak("Notepad is already closed")
    elif "open youtube" in query:
        speak("Opening Youtube ")
        webbrowser.open("www.youtube.com")
    elif "open google" in query:
        speak("Opening Google ")
        webbrowser.open("www.google.com")
    elif "tell me a joke" in query:
        speak("Here is a joke for you ")
        joke = pyjokes.get_joke(category="all")
        speak(joke)
        print(joke)
    elif 'sleep' in query:
        print('good bye')
        speak('good bye')
        break
    sleep(3)
