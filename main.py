from tkinter import *
from tkinter import simpledialog
import sys

import json #for data storing

def load_stats():
    with open("info.json", "r") as f:
        return json.load(f)

def save_stats():
    data = {
        "name": name,
        "age": age,
        "discipline": discipline,
        "hunger": hunger,
        "health": health,
        "happiness": happiness
    }
    with open("info.json", "w") as f:
        json.dump(data, f, indent = 4)

stats = load_stats()
name = stats["name"]
age = stats["age"]
discipline = stats["discipline"]
hunger = stats["hunger"]
health = stats["health"]
happiness = stats["happiness"]

#want a live update of stat in info no clue how (yet)


# main window
window = Tk()
window.geometry("320x320")
window.resizable(False, False)
window.title("Tamagotchi Pet")

info_labels = {}
# Info Window Testing
def show_info():
    info_window = Toplevel(window)
    info_window.geometry("175x150")
    info_window.title("Pet Info")
    info_window.resizable("False", "False")

    global info_labels # allow for live update of variable in info panel
    info_labels = {}

    # Show all stats:
    info_labels["name"] = Label(info_window, text=f"Name: {name}")
    info_labels["name"].pack()

    info_labels["age"] = Label(info_window, text=f"Age: {age}")
    info_labels["age"].pack()

    info_labels["discipline"] = Label(info_window, text=f"Discipline: {discipline}")
    info_labels["discipline"].pack()

    info_labels["hunger"] = Label(info_window, text=f"Hunger: {hunger}")
    info_labels["hunger"].pack()

    info_labels["health"] = Label(info_window, text=f"Health: {health}")
    info_labels["health"].pack()

    info_labels["happiness"] = Label(info_window, text=f"Happiness: {happiness}")
    info_labels["happiness"].pack()

    update_info_window()

def update_info_window():
    if info_labels:
        info_labels["name"].config(text=f"Name: {name}")
        info_labels["age"].config(text=f"Age: {age}")
        info_labels["discipline"].config(text=f"Discipline: {discipline}")
        info_labels["hunger"].config(text=f"Hunger: {hunger}")
        info_labels["health"].config(text=f"Health: {health}")
        info_labels["happiness"].config(text=f"Happiness: {happiness}")

        window.after(300, update_info_window)

info_button = Button(window, text="Info", command=show_info)
info_button.place(x=270, y=20)

# Adding the different ways to interact with your pet:
# Rename Button
def rename():
    user_input = simpledialog.askstring("Input", "What would you like to name your pet?")
    global name
    name = user_input
    save_stats()
    label = Label(window, text = "You renamed your pet!")
    label.pack()
    label.after(1500, label.destroy) #renmove text (label) after 1.5 secs
rename_button = Button(window, text = "Rename", command = rename)
rename_button.place(x=80, y=20)

# Feed Button
def feed():
    label = Label(window, text = "You fed your pet!")
    global hunger, happiness
    hunger = hunger + 5
    happiness = happiness + 5
    save_stats()
    label.pack()
    label.after(1500, label.destroy) #renmove text (label) after 2 secs
feed_button = Button(window, text = "Feed", command = feed)
feed_button.place(x=60, y=270)

# Play Button
def play():
    label = Label(window, text = "You played with your pet!")
    global hunger, happiness
    hunger = hunger - 10
    happiness = happiness + 5
    save_stats()
    label.pack()
    label.after(1500, label.destroy) #renmove text (label) after 2 secs
play_button = Button(window, text = "Play", command = play)
play_button.place(x=140, y=270)

# Train Button
def train():
    label = Label(window, text = "You worked on training your pet!")
    global discipline, happiness
    discipline = discipline + 5
    happiness = happiness - 5
    save_stats()
    label.pack()
    label.after(1500, label.destroy) #renmove text (label) after 2 secs
train_button = Button(window, text = "Train", command = train)
train_button.place(x=220, y=270)

'''
I think that there's no point in it right now since we could use the x
# Exit Button
def exit_program():
    sys.exit(0)
exit_button = Button(window, text = "Exit", command = exit_program)
exit_button.place(x=200, y=270)
'''

#reset stats button
def reset_stats():
    global name, age, discipline, hunger, health, happiness
    name = "Pet"
    age = 1
    discipline = 0
    hunger = 50
    health = 100
    happiness = 50
    save_stats()
reset_button = Button(window, text = "RESET", command = reset_stats)
reset_button.place(x=20, y=20)


#aging
def age_up():
    global age
    age += 1
    save_stats()
    window.after(60000, age_up) #run again in 60 seconds (from tkinter)
age_up()


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