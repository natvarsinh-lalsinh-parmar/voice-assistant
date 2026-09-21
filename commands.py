import datetime
import webbrowser
import wikipedia
from speech import speak
from brain import ask_ai

def handle_command(command):

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {date}")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        speak("What should I search?")
        query = input("Search: ")
        webbrowser.open(f"https://google.com/search?q={query}")

    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    else:
        speak("Thinking...")
        answer = ask_ai(command)
        speak(answer)
