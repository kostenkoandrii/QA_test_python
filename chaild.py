
def generator_age_button(arg):
    list_age_buttons = []
    for i in range(11):
        list_age_buttons.append([f"select[data-group-child-age='{i}']", i])
    for item in list_age_buttons:
        if item[1] == arg:
            return item[0]

def generator_age(arg):
    list_ages = []
    for i in range(18):
        list_ages.append([f" option[value='{i}']", i])
    for item in list_ages:
        if item[1] == arg:
            return item[0]
