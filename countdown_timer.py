"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time
import platform
import os
def get_seconds():
    seconds = 1;
    while True:
        try:
            seconds = int(input("Enter the number of seconds:"))
            if seconds < 1:
                print("Invalid input. Please enter a positive integer.")
                continue
            else:
                return seconds
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
        return seconds
    
def remaining_time(seconds):
    for i in range(seconds, 0, -1):
        minutes, secs = divmod(i, 60)
        print(f"{minutes:02d}:{secs:02d}", end="\r")
        time.sleep(1)

    print("Time's up!")

    # play a beep sound 
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(4000, 1000) # 1000hz frequency for 1000 ms
    elif platform.system() == "Linux":
        os.system("beep -f 1000 -l 1000") # linux based systems
    else:
        print("\a") # unix based systems


if __name__ == "__main__":
   seconds = get_seconds()
   remaining_time(seconds)