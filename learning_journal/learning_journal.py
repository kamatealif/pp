"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""
from datetime import datetime

if __name__ == "__main__":
    learning_entry = input("What did you learn today?: ")
    try:
        productivity_rating = int(input("Rate your productivity today (1-5): "))
        if productivity_rating < 1 or productivity_rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
            productivity_rating = 0
    except ValueError as e:
        print(f"Invalid input for productivity rating: {e}")
        productivity_rating = 0

    
    date = datetime.now().strftime("%Y-%m-%d - %I:%M %p")

    journal_entry =   f"📅 {date}\n{learning_entry}\nProductivity Rating: {"⭐" * productivity_rating}\n\n"
    journal_entry += f"{"-----X" * 10}\n\n"
    with open("learning_journal.txt", "a", encoding="utf-8") as file:
        file.write(journal_entry)
        print("Your entry has been saved successfully!")
    
