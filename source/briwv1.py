import os
os.system("clear")


people = []
people_file = open("persistence/people.txt", "r")
people_lines = people_file.readlines()
for peep in people_lines:
    people.append(peep.rstrip("\n"))
people_file.close()


drink = []
drink_file = open("persistence/drinks.txt", "r")
drink_lines = drink_file.readlines()
for bev in drink_lines:
    drink.append(bev.rstrip("\n"))
drink_file.close()


favourites = dict(zip(people, drink))


def separator():
    print("="*20)


def heading(type):
    print(f"{type.center(20)}")


def people_table():
    separator()
    heading("PEOPLE")
    separator()
    print()
    for pers in people:
        print(f"{pers.center(20)}")
    print()
    separator()


def drinks_table():
    separator()
    heading("DRINKS")
    separator()
    print()
    for drk in drink:
        print(f"{drk.center(20)}")
    print()
    separator()


menu_text = """ 
                Hello! Welcome to BrIW v1.0! Please choose one of the following options:
                1) Get all people
                2) Get all drinks
                3) Add people
                4) Add drinks
                5) Assign a favourite drink
                6) Get list of favourite drinks
                7) Delete a person and their favourite drink 
                8) Exit
 
                """

while True:

    print(menu_text)
    choice = input("Enter:")

    if choice == "1":
        people_table()
        print()
        print()
        input("Press Enter to return to Main Menu.")

    elif choice == "2":
        drinks_table()
        print()
        print()
        input("Press Enter to return to Main Menu.")

    elif choice == "3":
        people_additions=input("Enter name of new person:")
        person = open("persistence/people.txt", "a")
        person.write(people_additions + "\n")
        person.close()

    elif choice == "4":
        drinks_additions = input("Enter name of new drink:")
        drink = open("persistence/drinks.txt", "a")
        drink.write(drinks_additions + "\n")
        drink.close()

    elif choice == "5":
        person_favourite = input("Who do you wish to set a favourite drink for? Enter name: ")
        drink_favourite = input("what is their favourite drink? Enter drink: ")
        person = open("persistence/people.txt", "a")
        person.write(person_favourite + "\n")
        person.close()
        drink = open("persistence/drinks.txt", "a")
        drink.write(drink_favourite + "\n")
        drink.close()
        print()
        input("Press Enter to return to Main Menu.")

    elif choice == "6":
        separator()
        heading("FAVOURITE DRINKS")
        separator()
        print()
        for key, value in favourites.items():
            print(f"  {key} - {value}")
        print()
        separator()

    elif choice == "7":
        print(people)
        delete_person = input("Who do you wish to remove from the list? Enter name: ")
        print(delete_person)
        people.remove(delete_person)
        people_file = open("persistence/people.txt", "w")
        for line in people:
            people_file.write(line + "\n")
        people_file.close()

    elif choice == "8":
        exit()