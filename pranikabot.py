import time
import random

# User name
user_name = "Akhil"

# Chatbot name
bot_name = "Pranika"

# List of random GIF links
gif_links = [
    "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif",
    "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif",
    "https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif"
]

# Wait 4 seconds before greeting
time.sleep(5)
print(f"{bot_name}: Hie 👋")
print("Facing issue in gitlab pipeline build issue\n")
time.sleep(2)

# Simulate user response
user_response = ""  # empty string simulates no response from Akhil

# Check if Akhil responds
if user_response == "":
    print(f"\nNo response from {user_name}...")
    time.sleep(3)
    print(f"{bot_name} becomes furious! 😤🔥\n")
    time.sleep(3)

    # Furious message printed vertically with bot name
    furious_message = "O y e H e l l o . . . ."
    print(f"{bot_name}:")
    for char in furious_message.replace(" ", ""):
        print(char)
        time.sleep(1)

    print()  # Line break before GIFs

    # Send 3 random GIFs with short delay
    for i in range(3):
        gif = random.choice(gif_links)
        print(f"{bot_name} sends GIF: {gif}")
        time.sleep(1)
        
  # Urgent message after GIFs
    print(f"\n{bot_name}: Its urgent!!!!!!!!!")
