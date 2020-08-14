import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice ', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Shreya")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Shreya")
    else:
        speak("Good Evening Shreya")
    speak("I am your Assistant , how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'watch video' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        
        elif 'I want to chat' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'play music ' in query:
           music_dir = 'D:\\gaana' 
           songs= os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Shreya, the time is ")
            speak(strTime)

        elif 'apologize' in query:
            speak("I am really Sorry")

        elif 'open code' in query:
            codePath = "C:\\Users\\91870\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to shreya' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to = "shreya2209sinha1234@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Shreya, email cant be sent at the moment.")

        elif 'quit' in query:
            exit()



        


    
