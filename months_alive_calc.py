"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""

def calculate_age(age):
    DAY_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    
    total_days = DAY_IN_YEAR * age
    total_hours = HOURS_IN_DAY * total_days
    total_minutes = MINUTES_IN_HOUR * total_hours

    return round(total_days,2), round(total_hours), round(total_minutes)

def show_info(days, hours, minutes):
    print(f"{days} days old")
    print(f"{hours} hours old")
    print(f"{minutes} minutes old")



if __name__ == "__main__":

    while True:
        try:
            age = float(input("Enter the age: "))
            days,hours,minutes = calculate_age(age)

            show_info(days,hours,minutes)

            is_again = input("Would you like to Calculate age again[y/n]")
            if is_again != 'y':
                print("👋🏼 Good Bye!")
                break;

        except:
            print("Please Enter a Valid number ")