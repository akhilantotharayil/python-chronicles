import random

# Step 1: Computer randomly picks -1, 0, or 1
computer = random.choice([-1, 0, 1])

# Step 2: You enter your choice
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

# Step 3: Dictionaries to map letters and numbers
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Step 4: Convert your choice letter into number
you = youDict[youstr]

# ⚠️ You had a small typo here: should be reverseDict, not reverse
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Step 5: Compare results
if computer == you:
    print("It's a draw!")

else:
    if computer == -1 and you == 1:
        print("You win!")  # Snake drinks water
    elif computer == -1 and you == 0:
        print("You lose!")  # Gun sinks in water
    elif computer == 1 and you == -1:
        print("You lose!")  # Snake drinks water (you had water)
    elif computer == 1 and you == 0:
        print("You win!")  # Gun kills snake
    elif computer == 0 and you == -1:
        print("You win!")  # Water sinks gun
    elif computer == 0 and you == 1:
        print("You lose!")  # Gun kills snake
    else:
        print("Something went wrong!")
