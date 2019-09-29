
from source.persistence.persist_round import *





#bevs = create_dictionary("drinks.txt")
#favourites = create_dictionary("favourites.txt")

# pref_mapped={}
# for person_id, drink_id in favourites.items():
#     people_name = peeps[person_id]
#     drink_name = bevs[drink_id]
#     pref_mapped[people_name] = drink_name

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

