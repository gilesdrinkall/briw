
from source.format.format import *


print("\n\nHello! Welcome to BrIW v1.0!")

print("\n\nTime to make a round!")
round_maker=input("\n\nSo, who's making the round?")
print(f"\nGood on you, {round_maker}! Go ahead and choose one of the following options:")

menu_text = """

                1) Get all people
                2) Get all drinks
                3) Add people
                4) Add drinks
                5) Delete people
                6) Delete drink
                5) Assign a favourite drink
                6) Get list of favourite drinks
                7) Delete a person and their favourite drink 
                8) Exit       

"""

while True:

    print(menu_text)
    choice = input("Enter:")

    if choice == "1":
        people_dict = create_dictionary("Person", "person_id", "first_name")
        header("THE TEAM")
        print_dict(people_dict)
        separator()
        input("\n\nPress Enter to return to Main Menu.")

    elif choice == "2":
        drinks_dict = create_dictionary("Drink", "drink_id", "name")
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
        person_favourite = input("Who do you wish to set a favourite drink for? Enter name: ")
        drink_favourite = input("what is their favourite drink? Enter drink: ")
        person=open("people.txt", "a")
        person.write(person_favourite + "\n")
        person.close()
        drink=open("drinks.txt", "a")
        drink.write(drink_favourite + "\n")
        drink.close()
        print()
        input("Press Enter to return to Main Menu.")

    elif choice == "8":
        separator()
        heading("FAVOURITE DRINKS")
        separator()
        print()
        for key, value in favourites.items():
            print(f"  {key} - {value}")
        print()
        separator()

    elif choice == "9":
        print(people)
        delete_person = input("Who do you wish to remove from the list? Enter name: ")
        print(delete_person)
        people.remove(delete_person)
        people_file = open("people.txt", "w")
        for line in people:
            people_file.write(line + "\n")
        people_file.close()

    elif choice == "10":
        exit()



drink_round=Round(round_maker, pref_mapped)





print("\nHere's a list of team members...")
print("\n")
header("THE TEAM")
drink_round.display_entries(peeps)
separator()
print("\nand here is a menu of available drinks...")
print("\n")
header("DRINKS")
drink_round.display_entries(bevs)
separator()
name_id = input("\nPlease enter the ID of a member of the team that would like a drink: ")
drink_id = input("\nPlease enter the ID of the drink they would like: ")
drink_round.put_order_id(name_id, drink_id)
print("\n")
print(f"Ok, {round_maker}, here's the details of the round: ")
print("\n")
drink_round.print_drink_list()
persist_round(drink_round)






















    # people = []
    # people_file = open("people.txt", "r")
    # people_lines = people_file.readlines()
    # for peep in people_lines:
    #     people.append(peep.rstrip("\n"))
    # people_file.close()
    #
    # drink = []
    # drink_file = open("drinks.txt", "r")
    # drink_lines = drink_file.readlines()
    # for bev in drink_lines:
    #     drink.append(bev.rstrip("\n"))
    # drink_file.close()
    #
    # favourites = dict(zip(people, drink))
    #
    #
    # def people_table():
    #     separator()
    #     heading("PEOPLE")
    #     separator()
    #     print()
    #     for pers in people:
    #         print(f"{pers.center(20)}")
    #     print()
    #     separator()
    #
    #
    # def drinks_table():
    #     separator()
    #     heading("DRINKS")
    #     separator()
    #     print()
    #     for drk in drink:
    #         print(f"{drk.center(20)}")
    #     print()
    #     separator()
