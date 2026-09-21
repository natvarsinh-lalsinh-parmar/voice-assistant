from speech import listen, speak

def detect_wake_word():
    print("Waiting for wake word: 'Hey Nakshi'...")

    while True:
        text = listen()

        if "hey nakshi" in text:
            speak("Yes? I am listening")
            return True
