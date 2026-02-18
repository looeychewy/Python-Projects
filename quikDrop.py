# Justin Liu, 2/17/26
# Python-console version of the arcade game QuikDrop

# Notes:
# Adjust countdown based on user-selected difficulty (reduce time)


import threading  # Allows for multithreaded processes (countdown(), listener())
import time  # Imports time module for countdown
import random  # Imports random for randomization
from pynput import keyboard  # Tracks for keypresses

countTime = 50  # Game duration in seconds
numBalls = 50  # Number of balls
gameScore = 0  # Game score

ballsIn = 0  # Num balls that make it in
ballsMiss = 0  # Num balls that miss

canPress = True
timeUp = False


# Countdown method to track time
def countdown(seconds, listener):
    global timeUp
    while seconds >= 0:
        # end = "\r" overwrites the line each countdown (carriage return character)
        print(f"Time remaining: {seconds} seconds", end="\r")

        if seconds == 0:
            print("\nTime's up! Game over!")
            timeUp = True
            listener.stop()
            break
        time.sleep(1)  # Pause for 1 second
        seconds -= 1


# Unlocks key once released
def onRelease(key):
    global canPress
    if key == keyboard.Key.shift_l:
        canPress = True


# Drops ball based on userInput
def dropBall(key):
    global numBalls, ballsIn, ballsMiss, canPress, timeUp

    if key == keyboard.Key.shift_l and canPress and numBalls > 0 and not timeUp:
        result = random.randint(1, 5)
        if result > 2:
            numBalls -= 1
            ballsIn += 1
            print("-----------------------------")
            print("A ball went in!", "Score: ", ballsIn, "Balls left: ", numBalls)
            print("-----------------------------")
            canPress = False
        else:
            numBalls -= 1
            ballsMiss += 1
            print("-----------------------------")
            print("Ball missed! ", "Score: ", ballsIn, "Balls left: ", numBalls)
            print("-----------------------------")
            canPress = False
    elif key == keyboard.Key.shift_l and numBalls == 0:  # All balls dropped condition
        print("\nGame over!")
        return False  # Return false to stop the Listener


def main():

    print("Welcome to QuickDrop! The main objective of this game is to land all 50 balls in buckets within a certain amount of time!")
    print("Your time for this session is 50 seconds")

    playReady = input("Are you ready?[y/n]: ").lower()

    playStatus = True  # Tracks T/F to keep game active or pause game
    while playStatus == True:
        if playReady == 'y' or playReady == "yes":
            print("\nLet's begin!")

            listener = keyboard.Listener(on_press=dropBall, on_release=onRelease)
            listener.start()

            # Allocate countdown to a daemon thread, prioritize dropBall
            timeThread = threading.Thread(target=countdown, daemon=True, args=(countTime, listener))
            timeThread.start()

            listener.join()

            print("\nFinal score: ", ballsIn)
            print("Balls missed: ", ballsMiss)

        else:
            print("Loop ended!")

        playStatus = False


main()