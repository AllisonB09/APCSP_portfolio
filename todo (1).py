#Allison Banegas
#Create a to do list

#Init

#Func
list = ["Walk the dog","Buy Milk","Study for chemistry test"]
done = ["Finish APUSH homework", "Make lunch for the week" ]



print("Welcome to your to do list! You have the following options: \033[1mAdd an item, Mark an item as done, Remove or Clear an item, Exit\033[0m" )
option = input("Which one will you choose? ")


if option == "Add an item":
    add_list = input("What would you like to add? ")
    list.append(add_list)
    print(f"My To-do List: {list}")
    print(f"My List of things I've done: {done}")

elif option == "Mark an item as done":
    done_list = input("What would you like to mark done? ")
    list.remove(done_list)
    done.append(done_list)
    print(f"My To-do List: {list}")
    print(f"My List of things I've done: {done}")

elif option == "Remove or Clear an item":
    removeclear_list = input("Would you like to remove an item or clear the entire list? ")
    if removeclear_list == "remove an item":
        remove_list = input("What you item would you like to remove? ")
        try:
            list.remove(remove_list)
        except:
            print("Error Occured")

        print(f"My To-do List: {list}")
        print(f"My List of things I've done: {done}")

    if removeclear_list == "clear the entire list":
        list.clear()
        print(f"My To-do List: {list}")
        print(f"My List of things I've done: {done}")

elif option == "Exit":
    print("Exiting To-do List...")
    quit()



