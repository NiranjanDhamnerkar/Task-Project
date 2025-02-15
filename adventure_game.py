import time

# Introduction
def intro():
    print("\nWelcome to the Mysterious Forest Adventure!")
    print("You wake up in a dark forest. You have no memory of how you got here.")
    print("You see a path leading forward and a small bag on the ground.")
    time.sleep(2)
    first_choice()

# Inventory System
inventory = []

# First Choice
def first_choice():
    print("\nWhat do you do?")
    print("1. Pick up the bag.")
    print("2. Ignore the bag and walk forward.")

    choice = input("> ")
    if choice == "1":
        inventory.append("Mysterious Bag")
        print("\nYou picked up the bag. It might be useful later!")
    elif choice == "2":
        print("\nYou decide to ignore the bag and move forward.")
    else:
        print("\nInvalid choice! Try again.")
        first_choice()

    second_choice()

# Second Choice
def second_choice():
    print("\nYou continue walking and reach a fork in the road.")
    print("1. Take the left path (Dark Cave).")
    print("2. Take the right path (Old Cabin).")

    choice = input("> ")
    if choice == "1":
        dark_cave()
    elif choice == "2":
        old_cabin()
    else:
        print("\nInvalid choice! Try again.")
        second_choice()

# Dark Cave Scenario
def dark_cave():
    print("\nYou enter a dark cave. It's too dark to see anything.")
    if "Mysterious Bag" in inventory:
        print("\nYou open the bag and find a flashlight inside!")
        print("With the light, you find a hidden treasure chest!")
        print("Congratulations! You found the treasure and won the game! 🎉")
    else:
        print("\nYou stumble in the dark and fall into a deep pit. Game over! 😢")

# Old Cabin Scenario
def old_cabin():
    print("\nYou reach an old abandoned cabin.")
    print("Inside, you find a map and a locked door.")
    print("1. Try to open the locked door.")
    print("2. Take the map and leave.")

    choice = input("> ")
    if choice == "1":
        print("\nThe door is locked! You hear strange noises behind it... You run away!")
        print("Game over! 😢")
    elif choice == "2":
        print("\nYou take the map and leave the cabin safely.")
        print("The map shows a way out of the forest!")
        print("Congratulations! You found the escape route and won the game! 🎉")
    else:
        print("\nInvalid choice! Try again.")
        old_cabin()

# Start the game
intro()
