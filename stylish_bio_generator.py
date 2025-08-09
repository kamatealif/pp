"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""
import textwrap
def inputs():
    name = input("Enter your name: ").strip()
    profession = input("Enter your profession: ").strip()
    passion = input("Enter a one-liner about your passion or goal: ").strip()
    emoji = input("Enter your favorite emoji (optional): ").strip()
    website = input("Enter your website or handle (optional): ").strip()

    if not emoji:
        emoji = "✨"  # Default emoji if none provided
    if not website:
        website = "No website provided"  # Default message if no website is given

    return name, profession, passion, emoji, website

def show_templates(templates):
    print("\nAvailable Bio Templates:")
    for key, value in templates.items():
        print(f"{key}: {value}")
        print()
 
def generate_bio(name, profession, passion, emoji, website, template_choice,templates):
    bio = templates[template_choice].format(name=name, profession=profession, passion=passion, emoji=emoji, website=website)
    return textwrap.dedent(bio.strip())

def save_file(name, save_choice,bio):
    if save_choice.lower() == 'yes':
        filename = f"bio.text"
        with open(filename, 'a', encoding="utf-8") as file:
            file.write(f"\n{bio}\n")
        print(f"Bio saved to {filename}")
    else:
        print("Bio not Saved.")

if __name__ == "__main__":
    print("\nStylish Bio Generated:\n")
    name, profession, passion, emoji, website = inputs()
    

    templates ={ 
    1: f"👋 {name}\n{profession} by day, {passion} by heart ✨\nServing looks & chaos\nDM for collabs or bad life advice {emoji}\n🌐 {website}",
    2: f"👋 {name}\n{profession} with a side of {passion} 📱\nHere for memes, vibes, & Wi-Fi\nLife’s too short to fold fitted sheets {emoji}\n🌐 {website}",
    3: f"👋 {name}\n{profession} & full-time {passion} addict ☕\nMy life’s a sitcom, wanna guest star?\nLet’s make bad decisions together {emoji}\n🌐 {website}",
    4: f"✨ {name}\n{profession} by trade, {passion} for the soul 🌈\nSpilling tea & good vibes only\nSlide into my DMs for epic collabs {emoji}\n🔗 {website}",
    5: f"😜 {name}\n{profession} but make it fun, {passion} is my jam 🎉\nCatch me napping or slaying\nWant in on the chaos? DM me {emoji}\n🔗 {website}",
    6: f"🚀 {name}\n{profession} with a {passion} obsession 🔥\nLife’s too wild for boring plans\nJoin the adventure, hit me up {emoji}\n🔗 {website}"
    }
    show_templates(templates)
    template_choice = int(input("Choose a template 1-6}: "))

    while True:
        try:
            if template_choice in templates:
                break;
            else:
                print("Invalid choice. Please select a valid template number.")
                template_choice = int(input("Choose a template 1-6: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

    
    print("Your Stylish Bio:\n")
    print("*" * 50)
    bio =  generate_bio(name, profession, passion, emoji, website, template_choice, templates)
    print(bio)
    print("*" * 50)

    save_choice = input("Do you want to save this bio to a .txt file? (yes/no): ").strip().lower()

    save_file(name, save_choice,bio);