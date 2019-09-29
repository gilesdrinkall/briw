from source.persistence.persist_round import *

def separator():
    print("="*20)

def header(title):
    separator()
    print(f"{title.center(20)}")
    separator()

def create_dictionary(file_path: str):
    dict = {}
    file = open(file_path, "r")
    for line in file.readlines():
        if line != "\n":
            line = line.split(",")
            key = line[0]
            value = line[1].strip()
            dict[key] = value
    return dict

peeps = create_dictionary("persistence/people.txt")
bevs = create_dictionary("persistence/drinks.txt")
favourites = create_dictionary("persistence/favourites.txt")

pref_mapped={}
for person_id, drink_id in favourites.items():
    people_name = peeps[person_id]
    drink_name = bevs[drink_id]
    pref_mapped[people_name] = drink_name

class Round:

    def __init__(self, name_of_maker, favourites):
        self.name = name_of_maker
        self.favourites = favourites
        self.order_ids = {}
        self.round = []

    def get_favourites(self):
        fav_list = []
        for person, drink in self.favourites.items():
            fav_list.append([peeps[person], bevs[drink]])
        return fav_list

    def display_entries(self, entries):
        for id, entry in entries.items():
            print(f"\t{id}" + ") " + f"{entry}")

    def put_order_id(self, name_id, drink_id):
        self.order_ids[name_id] = drink_id

    def print_drink_list(self):
        for pers_id, drk_id in self.order_ids.items():
            people_name=peeps[pers_id]
            drink_name=bevs[drk_id]
            list_text = people_name + " wants " + drink_name + "."
            self.round.append(list_text)
            print(list_text)

    def update_round(self, new_round):
        self.round = new_round

if __name__=="__main__":


    print("\n\nTime to make a round!")
    round_maker=input("\nSo, who's making the round?")
    print(f"\nGood on you, {round_maker}!")
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