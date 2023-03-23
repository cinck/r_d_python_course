# ======== PHONEBOOK =========

# record = {name: {} }

# show qty of records
def stats():
    pass


def check_available_name(name, names):
    if not name or name in names:
        if not name:
            print("Entered nothing.")
        else:
            print("Contact already exists.")
        print("Record NOT crated")
        return False
    return True


# add record
def add_contact(phonebook):
    contact_data = {"Phone number": "",
                    "E-mail": "",
                    "Address": ""
                    }
    print("Enter contact name")
    name = input("Name: -> ")

    if check_available_name(name, phonebook.keys()):
        print(f"Enter {name} contact data")
        for data in contact_data.keys():
            contact_data[data] = input(f"{data}: > ")
        phonebook[name] = contact_data
        print(f"Contact '{name}' created.")
        return phonebook

    return phonebook


# remove record by key "name"
def delete_record(name):
    pass


# display all names
def list_names(phonebook: dict):
    if not phonebook.keys():
        print("= There is no contacts yet. =")
    else:
        print("Recorded contacts:")
        for contact in phonebook.keys():
            print(f"@ {contact}")
    return phonebook


# display all data
def show_name(name):
    pass


def show_help():
    pass


# take command
def execute_command(command: str, phonebook: dict) -> dict:
    executable = command.split()
    match executable[0].lower():
        case "stats":
            pass
        case "add":
            return add_contact(phonebook)
        case "delete":
            pass
        case "list":
            return list_names(phonebook)
        case "show":
            pass
        case "help":
            pass
        case _:
            print("Invalid command. Try 'help' for info.")
            return phonebook
    return dict()


def main(phonebook={}):
    command = None
    while command != "exit":
        command = input("@-> ")
        if not command or command == "exit":
            continue
        else:
            phonebook = execute_command(command, phonebook)

    pass


if __name__ == "__main__":
    main()
