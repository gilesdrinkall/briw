from source.persistence.database import *
from source.format.format import *


print("\n\nHello! Welcome to BrIW v1.0!")

print("\n\nTime to make a round!")
round_maker = input("\n\nSo, who's making the round?")
add_maker(round_maker)
print(f"\nGood on you, {round_maker}! Go ahead and choose one of the following options:")

menu_text = """

                1) Get all people
                2) Get all drinks
                3) Add people
                4) Add drinks
                5) Delete people
                6) Delete drink
                7) Create a round 
                8) Exit       

"""

while True:

    print(menu_text)
    choice = input("Enter:")

    if choice == "1":
        people_dict = create_dictionary("person", "person_id", "first_name")
        header("THE TEAM")
        print_dict(people_dict)
        separator()
        input("\n\nPress Enter to return to Main Menu.")

    elif choice == "2":
        drinks_dict = create_dictionary("drink", "drink_id", "name")
        header("DRINKS")
        print_dict(drinks_dict)
        separator()
        input("\n\nPress Enter to return to Main Menu.")

    elif choice == "3":
        people_dict = create_dictionary("Person", "person_id", "first_name")
        header("THE TEAM")
        print_dict(people_dict)
        separator()
        name_add = input("Enter name of new person:")
        add_person(name_add)
        print("Name added!")

    elif choice == "4":
        drinks_dict = create_dictionary("Drink", "drink_id", "name")
        header("DRINKS")
        print_dict(drinks_dict)
        separator()
        drink_add = input("Enter name of new drink:")
        add_drink(drink_add)
        print("Drink added!")

    elif choice == "5":
        people_dict = create_dictionary("Person", "person_id", "first_name")
        header("THE TEAM")
        print_dict(people_dict)
        separator()
        person_delete = input("Enter id of person you wish to delete:")
        delete_person(person_delete)
        print("Name deleted!")

    elif choice == "6":
        drinks_dict = create_dictionary("Drink", "drink_id", "name")
        header("DRINKS")
        print_dict(drinks_dict)
        separator()
        drink_delete = input("Enter id of drink you wish to delete:")
        delete_drink(drink_delete)
        print("Drink deleted!")

    elif choice == "7":
        pass
        input("\nPress Enter to return to Main Menu.")

    elif choice == "10":
        exit()
