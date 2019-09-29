def separator():
    print("="*20)


def header(title):
    separator()
    print(f"{title.center(20)}")
    separator()


def print_dict(dictionary):
    for num_id, dict_val in dictionary.items():
        print(f"  {num_id} - {dict_val}")

