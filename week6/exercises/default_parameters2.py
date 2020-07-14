# Write a function, that will add people to the list of person in class
# Function will take a string, with a names, separated with a coma,
# and a list of already signed up people which is empty by default


def list_of_people(add_name, participants=None):
    if participants is None:
        participants = []
    add_names = add_name.split(",")
    for name in add_names:
        participants.append(name)
    return participants

attendees_names = "Jack, John, Marry"
monday_classes = list_of_people(attendees_names)
print(monday_classes)
attendees_names = "Ola, Adam"
monday_classes = list_of_people(attendees_names, participants=monday_classes)
print(monday_classes)

attendees_names = "Ania"
friday_classes = list_of_people(attendees_names)
print(friday_classes)