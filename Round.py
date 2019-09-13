def create_dictionary(file_path):
    dict = {}
    file = open(file_path, "r")
    for line in file.readlines():
        line = line.split(",")
        key = line[0]
        value = line[1].strip()
        dict[key] = value
    return dict

people = create_dictionary("people.txt")
drinks = create_dictionary("drinks.txt")
favourites = create_dictionary("favourites.txt")

pref_mapped={}
for person_id, drink_id in favourites.items():
    people_name=people[person_id]
    drink_name=drinks[drink_id]
    pref_mapped[people_name]=drink_name

class Round:

    def __init__(self, name_of_maker,favourites):
        self.name=name_of_maker
        self.favourites=favourites
        self.order_ids={}
        self.round=[]

    def get_favourites(self):
        for person, drink in self.favourites.items():
           print(f"  {person} - {drink}")

    def display_entries(self, entries):
        for id, entry in entries.items():
            print(f"\t{id}\t{entry}")

    def get_order_ids(self):
        input_ids = input("\n\nWhich team members want a drink and what do they want? Enter the respective IDs separated commas:").split(",")
        for input in input_ids:
            self.order_ids[input_ids[0]]=input_ids[1]

    def drinks_list(self):
        for match in self.order_ids:
            favourite_text = "\n" + match + " would like " + favourites[match]
            self.round.append(favourite_text)
            print(favourite_text)

    def persist_round(self):
        file = open("round.txt", "w")
        self.round = "".join(self.round) #Converts list to string
        file.write(self.round)
        file.close()
        print("Round saved")

print("\n\nTime to make a round!")
round_maker=input("\n\nSo, who's making the round?")
print(f"\n\nGood on you, {round_maker}!")
drink_round=Round(round_maker, pref_mapped)
print("\n\nHere's a list of team members...")
print("\n")
drink_round.display_entries(people)
print("\n\nand here is a menu of available drinks...")
print("\n")
drink_round.display_entries(drinks)
drink_round.get_drinkers()
drink_round.drinks_list()
drink_round.persist_round()