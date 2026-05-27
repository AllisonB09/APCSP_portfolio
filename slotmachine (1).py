#Allison Banegas
#Slotmachine

#init
import random
symbols = [ "♥", "♦", "7", "☆"]

#function
def slotmachine():
        credit = 0

        while True:

                print("Welcome to Big Money Slot Machine!")
                print(f"You have {credit} credits. Each spin cost 10 credits")
                value = input("Would you like to add more credits? ")
                if value == "yes" or value == "Yes":
                                value = int(input("How many credits would you like to add? "))
                                credit = credit + value

                menu = input("Would you like to play or quit? ")

                #main
                if menu == "play" or menu == "Play":
                        menu = input("Type pull down to see if you get lucky! ")
                        credit = credit - 10

                if menu == "quit" or menu =="Quit":
                        print("Thank you for playing!")
                        print(f"Total Amount of Credits: {credit}")
                        break


                if menu == "pull down"  or menu == "Pull Down":
                        symbols1 = random.choice(symbols)
                        symbols2 = random.choice(symbols)
                        symbols3 = random.choice(symbols)
                print(f"{symbols1} - {symbols2} - {symbols3}")

                if symbols1 == "7" and symbols2 == "7" and symbols3 == "7":
                        credit = credit + 50
                        print("JACKPOT!!!")
                        print("You won 100 credits!")


                if symbols1 == symbols[1] and symbols2 == symbols[1] and symbols3 == symbols[1]:
                        credit = credit + 10
                        print("Small Win!")
                        print("You won 25 credits!")


                if symbols1 == symbols[2] and symbols2 == symbols[2] and symbols3 == symbols[2]:
                        credit = credit + 10
                        print("Small Win!")
                        print("You won 25 credits!")

                if symbols1 == symbols[3] and symbols2 == symbols[3] and symbols3 == symbols[3]:
                        credit = credit + 10
                        print("Small Win!")
                        print("You won 25 credits!")

                else:
                        print("You Lost! :(")
#main
slotmachine()
