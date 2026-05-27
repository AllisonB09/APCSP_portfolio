# DOG BREED
#The purpose of this program is to help users find a dog that fits their needs

#Goal 1
import webbrowser
import pandas as pd
import random

data = pd.read_csv("dog.csv")

name = data["Name"].tolist()
weight = data["Minimum Weight"].tolist()



#Goal 3
image = data["Image"].tolist()
temperament = data["Temperament"].tolist()
#Goal 4
bredfor = data["BredFor"].tolist()

#Init

#Functions
#Goal 2
def getDogSize(size):
#Goal 2

    tiny = []
    small = []
    medium = []
    large = []

    for i in range(len(name)):
        if weight[i] <= 10:
            tiny.append(name[i])
        elif weight[i] >= 11 and weight[i] <= 25:
            small.append(name[i])
        elif weight[i]>= 26 and weight[i] <= 60:
            medium.append(name[i])
        elif weight[i] > 60:
            large.append(name[i])

    if size == "tiny" or size == "Tiny":
        if tiny != []:
            print("A tiny dog you might like: " + random.choice(tiny))
        else:
            print("No tiny dogs found.")
    elif size == "small" or size == "Small":
        if small != []:
            print("A small dog you might like: " + random.choice(small))
        else:
            print("No small dogs found.")
    elif size == "medium" or size == "Medium":
        if medium != []:
            print(f"Medium dogs you might like: {medium}")
        else:
            print("No medium dogs found.")
    elif size == "large" or size == "Large":
        if large != []:
            print(f"Large dogs you might like: {large}")
        else:
            print("No large dogs found.")
    else:
        print("Size not recognized. Please choose Tiny, Small, Medium, or Large.")


#Goal 3
def look_up(breed_name):
    found = 0
    for i in range(len(name)):
        if breed_name == name[i]:
            webbrowser.open(image[i])
            print(f"Temperament of {name[i]}: {temperament[i]} ")
            found = 1
            break
    if found == 0:
        print(f"Breed {breed_name} not found")

#Goal 4
def information(purpose):
    found = 0
    for i in range(len(name)):
        if purpose in bredfor[i]:
            found = found + 1
            print(f"{name[i]} is a good dog bred for the trait you searced!")
    if found == 0:
        print("No breed with the following trait are found.")

def menu():
    while True:
        print("Hello! I'm here to help you pick a dog out!")
        option = input("""What information would you like to see?
            Options:
            - see a certain size range of dogs
            - see the temperament and image of differenent dogs
            - see which dogs fit a specific trait
            - quit
        Answer Here: """)
        if option == "see a certain size range of dogs":
            option_size = input("Size (Tiny, Small, Medium, Large): ")
            getDogSize(option_size)

        elif option == "see the temperament and image of a dog":
            breed = input("Enter the breed name: ")
            look_up(breed)

        elif option == "see which dogs fit a specific trait":
            trait = input("Enter the trait (e.g., guarding, companion): ")
            information(trait)

        elif option == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

getDogSize()
look_up("Akita")
information("mean")
menu()
#Main


#Sources of Information
#Dataset Source Information:
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source: https://thedogapi.com/en

