from wake_word import detect_wake_word
from speech import listen, speak
from commands import handle_command

def start_assistant():
    speak("Hey, I'm Nakshi. I'm listening.")

    while True:
        detect_wake_word()

        while True:
            command = listen()

            if command == "":
                continue

            if "stop" in command or "sleep" in command:
                speak("Going back to sleep mode")
                break

            handle_command(command)


if __name__ == "__main__":
    start_assistant()
