import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyaudio
import os
from translate import Translator
import pyjokes
import pyautogui
import tkinter as tk
from PIL import Image, ImageTk

engine = pyttsx3.init('sapi5')

T = Translator(from_lang="English", to_lang="Hindi")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def screenshot():
    pic = pyautogui.screenshot()
    pic.save('screenshot.png')

def wishMe():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 6:
        speak("Hey Owl")

    elif 6 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Hello sir")

    speak("I'm your Personal Voice Assistant Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail@gmail.com', 'your-password')
    server.sendmail('yourgmail@gmail.co', to, content)
    server.close()

def joke():
    speak(pyjokes.get_joke(language='en', category='all'))

def main():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            speak(results)
            print(results)

        elif 'open college website' in query:
            webbrowser.open("http://mydy.dypatil.edu/rait/my/")

        elif 'start youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")

        elif 'open dashboard' in query:
            webbrowser.open("http://mydy.dypatil.edu/rait/my/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to omkar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourgmail@gmail.co"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'shutdown' in query:
            print("Shutting down...")
            speak("Shutting down")
            quit()

        elif 'translate' in query:
            query = query.replace('translate', '')
            translation = T.translate(query)
            speak(translation)
            print(translation)

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            screenshot()

        elif 'search youtube' in query:
            speak("Kya dekhna pasand karoge boss")
            search = takeCommand().lower()
            speak('Muje ye videos mili')
            webbrowser.open(f'https://www.youtube.com/results?search_query={search}')

        elif 'search google' in query:
            speak("Kya search karu janab?")
            search = takeCommand().lower()
            speak('Wahh kya smart hu mein ye lijiye')
            webbrowser.open(f'https://www.google.com/search?q={search}')

def create_gui():
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("700x600")

    # Load and process the GIF frames
    gif_frames = []
    gif_path = "C:/Users/lithi/PycharmProjects/JARVIS_ASSISTANT/Images/ass.gif"
    gif = Image.open(gif_path)
    gif_width, gif_height = gif.size

    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.copy().resize((gif_width, gif_height), Image.LANCZOS)
        frame_photo = ImageTk.PhotoImage(frame_image)
        gif_frames.append(frame_photo)

    # Display the GIF frames on a label widget
    gif_label = tk.Label(root)
    gif_label.pack()

    def update_gif(frame_index):
        frame_photo = gif_frames[frame_index]
        gif_label.config(image=frame_photo)
        gif_label.image = frame_photo
        frame_index = (frame_index + 1) % len(gif_frames)
        root.after(100, update_gif, frame_index)

    # Start updating the GIF frames
    update_gif(0)

    lbl1 = tk.Label(root, text="Welcome to Voice Assistant App\n", wraplength=300)
    lbl1.pack()

    but1 = tk.Button(root, text="Run the Assistant", command=main)
    but1.pack(padx=10, pady=10)

    quit4 = tk.Button(root, text="EXIT", command=root.destroy)
    quit4.pack(padx=10, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()