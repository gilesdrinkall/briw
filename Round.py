def create_dictionary(file_path):
    dict = {}
    file = open(file_path, "r")
    for line in file.readlines():
        line = line.split(",")
        key = line[0]
        value = line[1].strip()
        dict[key] = value
    return dict

peeps = create_dictionary("people.txt")
bevs = create_dictionary("drinks.txt")
favourites = create_dictionary("favourites.txt")

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
        for person, drink in self.favourites.items():
           print(f"  {person} - {drink}")

    def display_entries(self, entries):
        print("\n")
        for id, entry in entries.items():
            print(f"\t{id}\t{entry}")

    def get_order_ids(self):
        self.order_ids = {}
        order_open = True
        while order_open:
            name_id = input("\nPlease enter the ID of a member of the team that would like a drink: ")
            drink_id = input('\nPlease enter the ID of the drink they would like: ')
            self.order_ids[name_id] = drink_id
            repeat = input("\nDo you want to add another order (yes/no)?")
            if repeat == "no":
                order_open = False

    def print_drink_list(self):
        for pers_id, drk_id in self.order_ids.items():
            people_name=peeps[pers_id]
            drink_name=bevs[drk_id]
            list_text = people_name + " wants " + drink_name + "."
            self.round.append(list_text)
            print(list_text)

    def persist_round(self):
        file = open("round.txt", "w")
        self.round = "".join(self.round) #Converts list to string
        file.write(self.round)
        file.close()
        print("\n\nRound saved!")


print("\n\nTime to make a round!")
round_maker=input("\nSo, who's making the round?")
print(f"\nGood on you, {round_maker}!")
drink_round=Round(round_maker, pref_mapped)
print("\nHere's a list of team members...")
drink_round.display_entries(peeps)
print("\nand here is a menu of available drinks...")
drink_round.display_entries(bevs)
drink_round.get_order_ids()
print("\n")
print(f"Ok, {round_maker}, here's the details of the round: ")
print("\n")
drink_round.print_drink_list()
drink_round.persist_round()