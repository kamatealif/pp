"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

# get dictionary 
def emoji_enhance(message, emoji_dict):
    enhanced_string = []

    for word in message.split():
        cleaned_word = word.lower().strip(".,?!")
        if cleaned_word in emoji_dict:
            enhanced_string.append(f"{cleaned_word} {emoji_dict[cleaned_word]}")
        else:
            enhanced_string.append(f"{cleaned_word}")
        
    return enhanced_string


if __name__ == "__main__":
    heading = "Welcome to emoji Enhancer"
    print(heading.center(50,"#"))
    emoji_dict = {
        "happy": "😊",
        "sad": "😢",
        "love": "❤️",
        "angry": "😠",
        "laugh": "😂",
        "cry": "😭",
        "thumbs_up": "👍",
        "thumbs_down": "👎",
        "clap": "👏",
        "fire": "🔥",
        "star": "⭐",
        "sun": "☀️",
        "moon": "🌙",
        "heart": "💖",
        "cool": "😎",
        "ok": "👌",
        "wow": "😲",
        "sleep": "😴",
        "party": "🥳",
        "food": "🍔",
        "drink": "🥤",
        "coffee": "☕",
        "tea": "🫖",           # Added
        "dog": "🐶",
        "cat": "🐱",
        "car": "🚗",
        "bike": "🚲",
        "airplane": "✈️",
        "train": "🚆",
        "school": "🏫",
        "book": "📚",
        "computer": "💻",
        "laptop": "💻",         # Added (same as computer)
        "phone": "📱",
        "money": "💰",
        "shopping": "🛍️",
        "music": "🎵",
        "camera": "📷",
        "gift": "🎁",
        "rain": "🌧️",
        "snow": "❄️",
        "tree": "🌳",
        "flower": "🌸",
        "mountain": "⛰️",
        "beach": "🏖️",
        "rocket": "🚀",
        "globe": "🌍",
        "light": "💡",
        "clock": "⏰",
        "code": "💻",          # Added
        "warning": "⚠️",       # Added
        "info": "ℹ️"           # Added
    }

    input_message = input("Enter your message: ")

    emojizised_string = emoji_enhance(input_message, emoji_dict)
    print(" ".join(emojizised_string))

