def separator():
    print("="*20)


def header(title):
    separator()
    print(f"{title.center(20)}")
    separator()


def print_dict(dictionary):
    for num_id, dict_val in dictionary.items():
        print(f"  {num_id} - {dict_val}")


def render_dict(dict):
    html_str = ""
    for pers_nm, drk_nm in dict.items():
        html_str += f'<li>{pers_nm} - {drk_nm}</li>'
    return html_str

