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

# Chatbot greets
print(f"{bot_name}: Hie")
print("Facing issue in gitlab pipeline build issue\n")  # Added line

# Simulate user response
user_response = ""  # empty string simulates no response from Akhil

# Check if Akhil responds
if user_response == "":
    print(f"\nNo response from {user_name}...")
    print(f"{bot_name} becomes furious!\n")
    
    # Furious message: vertical spelling of "O y e H e l l o . . . ."
    furious_message = "O y e H e l l o . . . ."
    for char in furious_message.replace(" ", ""):  # Remove spaces to print each character vertically
        print(char)
        time.sleep(0.2)
    
    # Send 3 random GIFs with a delay
    for i in range(3):
        gif = random.choice(gif_links)
        print(f"{bot_name} sends GIF: {gif}")
        time.sleep(1)
