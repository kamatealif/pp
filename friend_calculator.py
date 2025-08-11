"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""
def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')

    # Shared letters
    score += len(shared_letters) * 5

    # Vowels in shared letters
    score += len(vowels & shared_letters) * 10

    # Consonants in shared letters
    score += len(consonants & shared_letters) * 3
    
 
    # Character position matching
    for i in range(min(len(name1), len(name2))):
        if name1[i] == name2[i]:
            score += 2

    # Bonus for same length names
    if len(name1) == len(name2):
        score += 10

    return min(score, 100)

def get_compatibility_message(score):
    if score >= 80:
        return "🔥 You're like chai and samosa — made for each other! 💕"
    elif score >= 60:
        return "😊 You're a great match! 👫"
    elif score >= 40:
        return "🤔 You're okay, but there's room for improvement! 😐"
    else:
        return "😐 Well... opposites attract, maybe? 🤷‍♀️"

def get_advice(score):
    if score >= 80:
        return "Keep being your amazing selves! 💖"
    elif score >= 60:
        return "Communicate openly and honestly to strengthen your bond! 💬"
    elif score >= 40:
        return "Make time for each other and prioritize your friendship! 🕒"
    else:
        return "Don't worry, friendships can grow with effort! 💪"

def run_friendship_calculator():
    print("❤️ Friendship Compatibility calculator ❤️")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)
    message = get_compatibility_message(score)
    advice = get_advice(score)

    print("\n" + "="*40)
    print(f" Compatibility Score: {score}% ".center(40, " "))
    print("="*40)
    print(message)
    print(advice)
    print("="*40 + "\n")

if __name__ == "__main__":
    run_friendship_calculator()