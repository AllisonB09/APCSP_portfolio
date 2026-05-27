#Allison Banegas
#Nickname
#Students ask the user a few questions to see what their nickname is

#Functions
def nickname():
    print("I'm going to ask you different questions, but you'll end up with your nickname!")
    #Collect 1st input from user
    color = input("green or orange? ")

    #Color Question
    if color == "green":
        flower= input("Okay now choose either a lily or tulip. ")
        if flower == "tulip":
            animal = input("Now choose between a bird or bunny. ")
            if animal == "bunny":
                print("Your nickname will be Happy Hopper!")
            elif animal == "bird":
                print("Your nickname will be Funny Flier")
        elif flower == "lily":
            animal = input("Now choose between a frog or fish. ")
            if animal == "frog":
                print("Your nickname will be Happy Jumper Joy!")
            elif animal == "fish":
                print("Your nickname will be Silly Swimmer!")
    elif color == "orange":
        flower = input("Okay now choose either a rose or sunflower. ")
        if flower == "rose":
            animal = input("Now choose between a bear or sloth. ")
            if animal == "bear":
                print("Your nickname will be Hopeful Hunter!")
            elif animal == "sloth":
                print("Your nickname will be Sleepy Sweetheart")
        if flower == "sunflower":
            animal = input("Now choose between a goat or dog. ")
            if animal == "goat":
                print("Your nickname will be Gracious Genius!")
            elif animal == "dog":
                print("Your nickname will be Bold Buddy!")
#Main
nickname()
