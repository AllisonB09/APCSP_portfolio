#Allison Banegas
#Hogwarts

#Init
import time
import random

#Function
def main():
    print("Welcome to Hogwarts")
    name = input("What is your name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".......")
    print( house(name) )

def house(name):
    if name == "Harry" or name == "Ron" or name == "Hermione":
        return "Gryffindor"
    if name == "Draco" or name == "Voldemort" or name == "Severus":
        return "Slytherin"
    if name == "Luna" or name == "Cho" or name == "Filius":
        return "Ravenclaw"
    if name == "Newt" or name == "Nymphadora" or name == "Pomona":
        return "Hufflepuff"
    else:
        num = random.randint(1,4)

    if num == 1:
        return "Gryffindor"
    elif num == 2:
        return "Slytherin"
    elif num == 3:
        return "Hufflepuff"
    elif num == 4:
        return "Ravenclaw"

#main
main()


