'''
    Test to make sure it works.
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