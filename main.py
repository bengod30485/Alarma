#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pyttsx3",
# ]
# ///

"""pyttsx3 examples."""

import pyttsx3
import time

engine = pyttsx3.init()  # object creation

# RATE
def rate_change(rate):
    engine.setProperty("rate", rate)  # setting up new voice rate
    rate = engine.getProperty("rate")  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    ratebyuser = int(input("Enter the rate you want to set: "))  # taking user input for rate
    engine.setProperty("rate", ratebyuser)  # setting up new voice rate


# VOLUME
def volume_change(volume):
    engine.setProperty("volume", volume)  # setting up volume level  between 0 and 1
    volume = engine.getProperty("volume")  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    volumebyuser = float(input("Enter the volume you want to set: "))  # taking user input for volume
    engine.setProperty("volume", volumebyuser)  # setting up volume level  between 0 and 1

# VOICE
def voice_change(voice):
    engine.setProperty("voice", voice)  # changing index, changes voices. 0 for male
    voice = engine.getProperty("voice")  # getting details of current voice
    print(voice)  # printing current voice
    voices = engine.getProperty("voices")  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male
    engine.setProperty("voice", voices[1].id)  # changing index, changes voices. 1 for female

# PITCH
def pitch_change(pitch):
    engine.setProperty("pitch", pitch)  # setting up new voice pitch
    pitch = engine.getProperty("pitch")  # getting details of current speaking pitch
    print(pitch)  # printing current voice pitch
    pitchbyuser = int(input("Enter the pitch you want to set: "))  # taking user input for pitch
    engine.setProperty("pitch", pitchbyuser)  # setting up new voice pitch

def contador_alarma(count):
    countdown = int(input("Enter the countdown time in seconds: "))

    while countdown > 0:
        print(countdown)
        time.sleep(1)
        countdown -= 1

    print("¡Tiempo terminado!")

    engine.say("Time to wake up!")
    engine.runAndWait()
        


def main():
    rate_change(125)
    volume_change(1.0)
    voice_change(1)
    pitch_change(100)
    contador_alarma(10)


# Saving Voice to a file
# On linux make sure that 'espeak' is installed
def save_to_file():
    engine.save_to_file("Hello World", "test.mp3")

main()
save_to_file()
