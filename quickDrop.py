import time


COUNTTIME = 120 # Game duration in seconds

# test countdown method
def countdown (seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds", end ='')
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
    print("Time's up!")

# Start a 5-second countdown
# countdown(5)


def main():
    print("Welcome to QuickDrop! The main objective of this game is to land all 50 balls within the buckets in a certain amount of time!")
    print("Your time for this session is two minutes") # Randomize or hard set countdown?
    
    playReady = input("Are you ready?[y/n]: ").lower()

    playStatus = True
    while playStatus == True:
        if playReady == 'y' or playReady == "yes":
            print("Let's begin!")
            print(countdown(COUNTTIME))
        else:
            print("Loop ended!")
            
        playStatus = False
            

main()