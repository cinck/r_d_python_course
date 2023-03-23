# ======== PHONEBOOK =========

# record = {name: {} }

# show qty of records
def stats(phonebook):
    if not phonebook:
        print("= PHONEBOOK IS EMPTY =")
    else:
        print(f"= You have {len(phonebook)} contacts recorded =")
    return phonebook


def check_available_name(name, names):
    if not name or name in names:
        print("Record NOT crated. Reason :", end=" ")
        if not name:
            print("Entered nothing.")
        else:
            print("Contact already exists.")
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
def delete_contact(name, phonebook):
    return phonebook
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


#  display all data
# todo: write func
def show_name(name: str, phonebook: dict):
    return phonebook
    pass


def extract_name(entry: str):
    entry = entry.strip()
    if len(entry) >= 3 and entry[0] == "<" and entry[-1] == ">":
        name = entry[1:-1].strip()
        return name
    return ""


def extract(executable: str):
    first_space = executable.find(" ")
    command = executable.strip()[:first_space]
    name = extract_name(executable[first_space:])
    return {"command": command, "name": name}


def show_help():
    pass


# take command
def execute_command(command: str, phonebook: dict) -> dict:
    executable = extract(command)
    match executable["command"].lower():
        case "stats":
            return stats(phonebook)

        case "add":
            return add_contact(phonebook)

        case "delete":
            if executable["name"]:
                return delete_contact(executable["name"], phonebook)
            print("= Invalid name entry =")

        case "list":
            return list_names(phonebook)

        case "show":
            if executable["name"]:
                return show_name(executable["name"], phonebook)
            print("= Invalid name entry =")

        case "help":
            show_help()

        case _:
            print(f"Invalid command \'{executable['command']}\'. Try 'help' for info.")

    return phonebook


def main(phonebook={}):
    command = ""
    while command.lower() != "exit":
        command = input("@-> ")
        if not command or command == "exit":
            continue
        else:
            phonebook = execute_command(command, phonebook)

    pass


if __name__ == "__main__":
    main()
