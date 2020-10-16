import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install SpeechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib

# pip install pyaudio
# google "unofficial python binaries", if "pyaudio" installation shows error

# voice setup
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your A I Assistant Sir. Please tell me how may I help you")

# taking voice input
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# for emails
def sendEmail(to, content):
    server = smtplib.SMPT('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourEmail@gmail.com', 'yourPassword')
    server.sendmail('yourEmail@gmail.com', to, content)
    server.close()


# main function 
if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Writing query inputs and Function Outputs


        if 'wikipedia' in query:
            speak('Searching WikiPedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'github' in query:
            webbrowser.open("github.com")

        elif 'music' in query:
            music_dir = 'F:\\songs\\my Playlist'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'code' in query:
            codePath = "E:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to yourName' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")


        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'my github' in query:
            webbrowser.open("github.com/youUserName")

        elif 'blog' in query:
            webbrowser.open("blogger.com")

        elif 'my blog' in query:
             webbrowser.open("yourBlog.blogspot.com")
