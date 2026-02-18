# Justin Liu, 2/17/26
# Python-console version of the arcade game Quick Drop

# Notes:
# Implement basic ball dropping first (listen for space key input, drop until all 50 dropped) ✅
 
# Randomize chance that a ball gets into a bucket/doesn't get into one ✅
# Print result ("Ball went in!" or "Ball missed!") on each line ✅
    # next to countdown? 

import threading # Allows for multithreaded processes (countdown(), listener())
import time # Imports time module for countdown
import random # Imports random for randomization 
from pynput import keyboard

countTime = 50 # Game duration in seconds
numBalls = 50 # Number of balls
gameScore = 0 # Game score


# Countdown method to track time
def countdown (seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds", end = "\r") #\r overwrites the line each countdown (carriage return character)
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
    print("Time's up!")


def dropBall(key): 
    # On space press, randomize ball went in/ball missed ✅
    # time.sleep(1)/something similar to prevent stacked inputs
    # Keeps running until all balls are dropped. 

    # How to run in tandem with timer? -> listener.join() "blocks", countdown() takes priority before dropBall() can be printed
            
    global numBalls
    if key == keyboard.Key.space and numBalls > 0:
        result = random.randint(1,5)
        if result > 3:
            numBalls -= 1
            print("A ball went in!", numBalls)
        else:
            numBalls -= 1
            print("Ball missed!", numBalls)
    elif numBalls == 0:
        print("Game over!")
        return False # Return false to stop the Listener


def main():
    global numBalls
    countThread = threading.Thread(target=countdown, args=(50,))
    ballThread = threading.Thread(target=dropBall, args=())

    print("Welcome to QuickDrop! The main objective of this game is to land all 50 balls within the buckets in a certain amount of time!")
    print("Your time for this session is 50 seconds") # Adjust countdown based on user-selected difficulty (reduce time)
    
    playReady = input("Are you ready?[y/n]: ").lower()

    playStatus = True # Tracks T/F to keep game active or pause game
    while playStatus == True:
        if playReady == 'y' or playReady == "yes":
            print("Let's begin!", numBalls)
            #countdown(countTime)

            with keyboard.Listener(on_press= dropBall) as listener:
                listener.join()
        else:
            print("Loop ended!")
            
        playStatus = False
            

main()