import speech_recognition as sr
import pyttsx3
import serial
import time
import re

# Arduino Serial setup
arduino = serial.Serial('COM20', 9600)  # Change COM port if needed
time.sleep(2)

# TTS setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("Google:", text)
    engine.say(text)
    engine.runAndWait()

# Speech recognition
recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand.")
        except sr.RequestError:
            print("Speech service unavailable.")
        return ""

# Extract number of seconds
def extract_seconds(command):
    match = re.search(r'(\d+)\s*second', command)
    return int(match.group(1)) if match else None

# Main loop
while True:
    command = listen_command()

    if "google" in command:
        seconds = extract_seconds(command)

        if "led on" in command:
            arduino.write(b"ON\n")
            if seconds:
                speak(f"Turning LED on for {seconds} seconds")
                time.sleep(seconds)
                arduino.write(b"OFF\n")
                speak("Turning LED off")
            else:
                speak("Turning LED on")

        elif "led off" in command:
            arduino.write(b"OFF\n")
            if seconds:
                speak(f"Turning LED off for {seconds} seconds")
                time.sleep(seconds)
                arduino.write(b"ON\n")
                speak("Turning LED on")
            else:
                speak("Turning LED off")

        elif "blink" in command:
            blink_count = 10  # default blink times
            speak(f"Blinking LED {blink_count} times")
            for _ in range(blink_count):
                arduino.write(b"ON\n")
                time.sleep(0.5)
                arduino.write(b"OFF\n")
                time.sleep(0.5)
            speak("Blinking complete")

        elif "shutdown" in command or "exit" in command:
            speak("Shutting down. Goodbye.")
            break

arduino.close()
