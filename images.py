#Allison Banegas
#Images

#Initialize


import webbrowser

url = ["https://tinyurl.com/4xw6mras", #Capybara
       "https://tinyurl.com/mphcvyes", #Guinea Pig
       "https://tinyurl.com/4cfm8yn8", #Chinchillas
       "https://tinyurl.com/tv85jbcu"  #Hamster
       ]

description = ["""Cabybaras are one of the biggest rodents on Earth (77-150 pounds)! They need a tropical environment, lots of land to roam
               around, and water to swim around. They are also very calm.""",
               """Guiena Pigs are very tiny rodents (8-12 inches) that are very gentle. They are very social rodents that love
               to play with other Guiena pigs and are very energetic!""",
               """Chinchillas are average sized rodents (1-2 pounds). They need a cold environment (the cold hurts them) and can either live
               indoor or outdoor. They are also shy at first but eventually are friendly.""",
               """Hamsters are very small rodents (2-6 inches) that are very calm. They don't like to be with other hamsters and they
               like to stay quiet and to themselves."""]





#Functions
def rodent():
       print("Hi! I see you're shopping for a rodent pet. Answer a few questions and we'll find the perfect one for you!")
       size = input("Okay let's start! Would you like a rodent pet that is on the smaller or larger side? ")

    #Determing/Questions....
       if size == "Smaller" or size == "smaller" or size == "smaller side" or size == "smaller side":
              behavior = input("Would you like a more social/loud or anti-social/quiet rodent pet? ")
              if behavior == "anti-social/quiet" or behavior == "anti-social/quiet rodent pet":
                            webbrowser.open(url[3])
                            print(description[3])
              elif behavior == "social/loud" or behavior == "social/loud rodent pet":
                            webbrowser.open(url[1])
                            print(description[1])
       elif size == "Larger" or size == "larger" or size == "larger side" or size == "Larger side":
              environment = input("Do you live in an tropical environment or in a cold environment? ")
              if environment == "tropical environment" or environment == "tropical":
                            webbrowser.open(url[0])
                            print(description[0])
              elif environment == "cold environment" or environment == "cold":
                            webbrowser.open(url[2])
                            print(description[2])

#Main
rodent()


#Sources of Information

#Picture of Capybara Face Front
#Website Name: rainforest-alliance.org
#URL: https://www.rainforest-alliance.org/species/capybara/
#Author Name: N/A
#Date: September 19, 2023
#Article Title: Capybara Hydrochaeris hydrochaeris

#Picture of Guinea Pig
#Website Name: humanerescuealliance.org
#URL: https://www.humanerescuealliance.org/blog/posts/everything-you-need-to-know-about-guinea-pigs
#Author Name: N/A
#Date: N/A
#Article Title: Everything You Need to Know About Guinea Pigs

#Picture of Chinchilla
#Website Name: stkittsvet.co.uk
#URL: https://stkittsvet.co.uk/st-kitts-veterinary-group-advice/chinchillas-rough-guide-owning-chinchillas
#Author Name: N/A
#Date: N/A
#Article Title: Chinchillas – A rough guide to owning Chinchillas

#Picture of Hamster
#Website Namemonticelloveterinary.com
#URL: https://monticelloveterinary.com/articles/627576-hamsters
#Author Name: N/A
#Date: N/A
#Article Title: Hamsters


