from tkinter import *
from tkinter import simpledialog
from info import name, age, discipline, hunger, health, happiness
import time
import sys

# main window
window = Tk()
window.geometry("300x600")
window.title("Tamagotchi Pet")

# Info Window Testing
def show_info():
    info_window = Toplevel(window)
    info_window.geometry("300x150")
    info_window.title("Pet Info")

    # Show all stats:
    name_label = Label(info_window, text=f"Name: {name}")
    name_label.pack()

    age_label = Label(info_window, text=f"Age: {age}")
    age_label.pack()

    discipline_label = Label(info_window, text=f"Discipline: {discipline}")
    discipline_label.pack()

    hunger_label = Label(info_window, text=f"Hunger: {hunger}")
    hunger_label.pack()

    health_label = Label(info_window, text=f"Health: {health}")
    health_label.pack()

    happiness_label = Label(info_window, text=f"Happiness: {happiness}")
    happiness_label.pack()

# Button to show info
info_button = Button(window, text="Show Info", command=show_info)
info_button.pack(pady=20)

# Adding the different ways to interact with your pet:
# Rename Button
def rename():
    user_input = simpledialog.askstring("Input", "What would you like to name your pet?")
    global name
    name = user_input
    label = Label(window, text = "You renamed your pet!")
    label.pack()
rename_button = Button(window, text = "Rename", command = rename)
rename_button.pack(pady = 20)

# Feed Button
def feed():
    label = Label(window, text = "You fed your pet!")
    global hunger, happiness
    hunger = hunger + 5
    happiness = happiness + 5
    label.pack()
feed_button = Button(window, text = "Feed", command = feed)
feed_button.pack(pady = 20)

# Play Button
def play():
    label = Label(window, text = "You played with your pet!")
    global hunger, happiness
    hunger = hunger - 10
    happiness = happiness + 5
    label.pack()
play_button = Button(window, text = "Play", command = play)
play_button.pack(pady = 20)

# Train Button
def train():
    label = Label(window, text = "You worked on training your pet!")
    global discipline, happiness
    discipline = discipline + 5
    happiness = happiness - 5
    label.pack()
train_button = Button(window, text = "Train", command = train)
train_button.pack(pady = 20)

# Exit Button
def exit_program():
    sys.exit(0)
exit_button = Button(window, text = "Exit", command = exit_program)
exit_button.pack(pady = 20)

window.mainloop() #display window


# Temporarily Commented out to test GUI
'''
from info import name, age, hunger

print("Welcome!")
pet_name = input("What is your pet's name? ")
name = pet_name
print(f"Great! Your pet's name is {name}.")

# While loop to ask user for stuff:
while True:
    print("\nWhat would you like to do?")
    print("1. Feed your pet")
    print("2. Play with your pet")
    print("3. Check your pet's status")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        hunger -= 10
        print(f"You fed {name}. Hunger is now {hunger}.")
    elif choice == '2':
        hunger += 5
        print(f"You played with {name}. Hunger is now {hunger}.")
    elif choice == '3':
        print(f"{name}'s status: Age: {age}, Hunger: {hunger}")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

'''