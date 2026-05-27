## Netflix Recommender System
# This program recommends a Netflix movie or TV show based on user preferences.
# Uses a CSV dataset from Kaggle containing Netflix titles, types, genres, ratings, etc.

import random
import pandas as pd

# Load the Netflix dataset and convert relevant columns to Python lists
data = pd.read_csv("netflix.csv")

type = data["Type"].tolist()
title = data["Title"].tolist()
country = data["Country"].tolist()
data_added = data["Data Added"].tolist()
release_year = data["Release Year"].tolist()
rating = data["Rating"].tolist()
genre = data["Genre"].tolist()
# 'results' stores the titles of movies that meet the citeria of each filtering step
results = []

def reset_results():
    return list(range(len(title)))


#Filters titles based on user's category
def age_check(age_sorting):
    global results
    new_results = []
    age_sorting = age_sorting.lower()
    for i in results:
            if age_sorting == "kid":
                if rating[i] in ["TV-Y7", "TV-Y7-FV", "TV-PG", "PG"]:
                    new_results.append(i)

            elif age_sorting == "preteen":
                if rating[i] in ["TV-Y7", "TV-Y7-FV", "TV-PG", "PG"]:
                    new_results.append(i)

            elif age_sorting == "early teen":
                if rating[i] in ["TV-Y7", "TV-Y7-FV", "TV-PG", "TV-Y", "PG", "PG-13"]:
                    new_results.append(i)

            elif age_sorting == "late teen":
                if rating[i] in ["TV-PG", "TV-14", "PG-13"]:
                        new_results.append(i)

            elif age_sorting == "adult":
                if rating[i] in ["TV-14", "TV-MA", "R", "NR"]:
                        new_results.append(i)

    results = new_results

def type_option(film_option):     #Filters titles by type: 'Movie' or 'TV Show'.
    global results      #Updates the global results list.
    new_results = []
    film_option = film_option.lower()
    for i in results:
        if film_option == "movie":
            if "movie" in type[i].lower():
                new_results.append(i)
        elif film_option == "tv show":
            if "tv show" in type[i].lower():
                new_results.append(i)


    results = new_results



def language_option(language):          #Filters TV shows by language preference.
    global results                #Skips titles without a genre entry to prevent errors.
    new_results = []
    language = language.lower()
    for i in results:
        if not genre[i]:
            continue  # skip empty cells
        g = genre[i].lower()
        if language == "spanish":
            if "Spanish-Language TV Shows" in g:
                    new_results.append(i)
        elif language == "english":
            if "Spanish-Language TV Shows" not in g:
                new_results.append(i)

    results = new_results

def international_option(choice):   #Filters titles based on whether they are International or not.
    global results
    new_results = []
    choice = choice.lower()
    for i in results:
        if choice == "yes":
            if "International" in genre[i]:
                new_results.append(i)

        elif choice == "no":
            if "International" not in genre[i]:
                new_results.append(i)

    results = new_results



def genre_optionShows(choiceTV):
    global results
    new_results = []
    choiceTV = choiceTV.lower()
    for i in results:
        if choiceTV == "romance":
            if "Romantic TV Shows" in genre[i]:
                new_results.append(i)
        elif choiceTV == "comedy":
            if "TV Comedies" in genre[i]:
                new_results.append(i)
        elif choiceTV == "drama":
            if "TV Dramas" in genre[i]:
                new_results.append(i)
        elif choiceTV == "action & adventure":
            if "TV Action & Adventure" in genre[i]:
                new_results.append(i)
        elif choiceTV == "horror":
            if "TV Horror" in genre[i]:
                new_results.append(i)
        elif choiceTV == "reality tv":
            if "Reality TV" in genre[i]:
                new_results.append(i)
        elif choiceTV == "crime":
            if "Crime TV Shows" in genre[i]:
                new_results.append(i)
        elif choiceTV == "docuseries":
            if "Docuseries" in genre[i]:
                new_results.append(i)
        elif choiceTV == "nature":
            if "Science & Nature TV" in genre[i]:
                new_results.append(i)

    results = new_results


def genre_optionsMovies(choiceM):      #Filters movies by genre. Accepts user input like 'drama' or 'thrillers'.
    global results
    new_results = []
    choiceM = choiceM.lower()
    for i in results:
        if choiceM == "romance":
            if "Romantic Movies" in genre[i]:
                new_results.append(i)
        elif choiceM == "comedy":
            if "Comedies" in genre[i]:
                new_results.append(i)
        elif choiceM == "drama":
            if "Dramas" in genre[i]:
                new_results.append(i)
        elif choiceM == "action & adventure":
            if "Action & Adventure" in genre[i]:
                new_results.append(i)
        elif choiceM == "horror":
            if "Horror Movies" in genre[i]:
                new_results.append(i)
        elif choiceM == "sports":
            if "Sports Movies" in genre[i]:
                new_results.append(i)
        elif choiceM == "independent films":
            if "Independent" in genre[i]:
                new_results.append(i)
        elif choiceM == "documentaries":
            if "Documentaries" in genre[i]:
                new_results.append(i)
        elif choiceM == "thrillers":
            if "Thrillers" in genre[i]:
                new_results.append(i)


    results = new_results


def recently_film(came_out):   #Filters titles based on whether they were added recently (2020 in this example).
    global results
    new_results = []
    came_out = came_out.lower()
    for i in results:
        if came_out == "yes":
            if "2020" in str(data_added[i]):
                new_results.append(i)
        elif came_out == "no":
            new_results.append(i)

    results = new_results

def menu():      #Main user interface. Guides the user through the questionnaire then displays random reommendation from filtered reuslts
    while True:
        print("""
\033[1mWelcome to Neflix Recommender! We're here to give you the movie you're looking rather than you spending an hour looking for one!\033[0m""")
        options = input("""

                                                    == MENU ==

                                            - Start Questionnaire
                                            - Quit

                                            Choose Here: """).lower()
        if options == "start questionnaire":
            global results
            results = reset_results()
            while True:
                age_sorting = input("""

                                                    == AGE ==

                    Before we start your questionnaire please type in your age range (Don't type the numbers):
                    - Kid (7-9)
                    - Preteen (10-12)
                    - Early Teen (13-15)
                    - Late Teen (16-17)
                    - Adult (18+)

                    Answer here: """).lower()

                if age_sorting in ["kid", "preteen", "early teen", "late teen", "adult"]:
                    age_check(age_sorting)
                    break
                else:
                    print("""                Invalid input, try again.""")

            while True:
                film_option = input("""
                                                  == FILM TYPE ==

                            Okay Now we're starting the questionnare! What film type do you want to watch?
                            Options:
                            - TV Show
                            - Movie

                            Answer Here: """).lower()

                if film_option in ["movie", "tv show"]:
                    type_option(film_option)
                    break
                else:
                    print("""                  Invalid input, try again.""")

            if film_option == "tv show":
                while True:
                    language = input("""

                                                    == LANGUAGE ==

                                    What languages are you trying to watch the show in?
                                    Options:
                                    - Spanish
                                    - English

                                    Answer Here: """)
                    before = results.copy()
                    language_option(language)

                    if results != before:
                        break

                    else:
                         print("""
                                            Invalid input, try again.""")

                while True:
                    choice = input("""
                                                    == INTERNATIONAL ==

                                        Do you want to watch an international show?
                                        - Yes
                                        - No

                                        Answer Here: """).lower()

                    if choice in ["yes", "no"]:
                        international_option(choice)
                        break
                    else:
                         print("""                          Invalid input, try again.""")

                genre_choice1 = input("""
                                                    == GENRE ==

                            What genre are you most feeling? (PICK 2 OR 1 YOU WANT IN A TV SHOW)
                            - Romance
                            - Comedy
                            - Drama
                            - Action & Adventure
                            - Horror
                            - Reality TV
                            - Crime
                            - Docuseries
                            - Nature

                            First Choice: """).lower()

                genre_choice2 = input("""
                            Second Choice (press Enter to skip): """).lower()
                original_results = results.copy()

                # First genre
                results = original_results.copy()
                genre_optionShows(genre_choice1)
                results1 = results.copy()

                # Second genre
                if genre_choice2 != "":
                    results = original_results.copy()
                    genre_optionShows(genre_choice2)
                    results2 = results.copy()
                    results = list(set(results1) & set(results2))
                else:
                    results = results1

                while True:
                    came_out = input("""
                                                == NEWLY ADDED ==

                            Do you want to watch something that just came out on Netflix?
                            - Yes
                            - No

                            Answer Here: """).lower()
                    if came_out in ["yes", "no"]:
                        recently_film(came_out)
                        break

                    else:
                         print("" \
                         "                                      Invalid input, try again.")

                if results:
                    choice = random.choice(results)
                    print(f"""
                                                            == RESULTS ==

                                                Your recommendation is....

                                                \033[1m{(title[choice])}\033[0m""")

                else:
                    print("""
                                            == RESULTS ==

                        "Sorry we couldn't find a TV show that fits your needs. Try again!""")

            elif film_option == "movie":
                while True:
                    choice = input("""

                                                == INTERNATIONAL ==

                                    Do you want to watch an international movie?
                                    - Yes
                                    - No

                                    Answer Here: """).lower()

                    if choice in ["yes", "no"]:
                        international_option(choice)
                        break

                    else:
                        print("""
                                Invalid input, try again.""")

                genre_choice1 = input("""


                                                    == GENRE ==

                                What genre are you most feeling? (PICK 2 OR 1 YOU WANT IN A MOVIE)
                                Options:
                                - Romance
                                - Comedy
                                - Drama
                                - Action & Adventure
                                - Horror
                                - Sports
                                - Independent Films
                                - Documentaries
                                - Thrillers

                                First Choice: """).lower()
                genre_choice2 = input("""
                                Second Choice (press Enter to skip): """).lower()


                original_results = results.copy()

                # First genre
                results = original_results.copy()
                genre_optionsMovies(genre_choice1)
                results1 = results.copy()

                # Second genre
                if genre_choice2 != "":
                    results = original_results.copy()
                    genre_optionsMovies(genre_choice2)
                    results2 = results.copy()
                    results = list(set(results1) & set(results2))
                else:
                    results = results1
                while True:
                    came_out = input("""

                                                == NEWLY ADDED ==

                                Do you want to watch something that just came out on Netflix?
                                - Yes
                                - No

                                Answer Here: """).lower()
                    if came_out in ["yes", "no"]:
                        recently_film(came_out)
                        break

                    else:
                         print("""              Invalid input, try again.""")

                if results:
                   choice = random.choice(results)
                   print(f"""

                                                        == RESULTS ==

                                                    Your recommendation is....
                                                        \033[1m{(title[choice])}\033[0m""")

                else:
                    print("""
                                                    == RESULTS ==

                                Sorry we couldn't find a movie that fit your needs. Try again!""")
        elif options == "quit":
            print("""
                            Goodbye! Hope we were able to help you find a movie or TV show!""")
            break
        else:
            print("""
                                        Sorry invalid choice. Please try again.""")

menu()

#Sources of Information
#Dataset Source Information:
#Netlix Dataset on Netflix Content
#Website Name (Source used for Dataset): Kaggle.com
#Dataset URL: https://docs.google.com/spreadsheets/d/1GzPPziG7pEvL1XrqO5DewWLU1s12NNbAQ2nqJ5CjUJw/edit?gid=0#gid=0
#Dataset Source URL: https://www.kaggle.com/datasets/shivamb/netflix-shows
































