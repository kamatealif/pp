"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""
def inputs ():
    num_people = int(input("Enter the number of people in the group: "))
    names = []
    for i in range(num_people):
        i = input(f"Enter the name of person {i + 1}: ").strip()
        names.append(i)
    total_bill = float(input("Enter the total bill amount: ₹").strip())
    return num_people, names, total_bill

def calculate_share(total_bill, num_people):
    share  = total_bill /num_people
    return round(share,2)

def display_bill(names,share):
    for name in names:
        print(f"{name}: {share}")

if __name__ == "__main__":
    welcome_message = "Welcome to the Bill splitter"
    print(welcome_message.center(50,"#"),end="\n")
    print()
    num_people, names, total_bill = inputs()

    share_per_each = calculate_share(total_bill= total_bill, num_people=num_people)

    display_bill(names=names, share=share_per_each)
