# ======== PHONEBOOK =========
# Stores and displays contact's information.
# Creates records of contacts by their names with phone number, e-mail and address info.
# Once created record can't be edited, only removed.
# Contact names can't duplicate.

# Displays quantity of existing records in phonebook
def show_stats(phonebook: dict):
    if not phonebook:
        print("= PHONEBOOK IS EMPTY =")
    else:
        print(f"= You have {len(phonebook)} contacts =")
    return phonebook


# Confirms if name is valid to be recorded or rejects it
def check_available(name: str, contacts):
    if not name or name.isspace() or name in contacts:
        print("= Record NOT created. Reason :", end=" ")
        if not name:
            print("Entered nothing =")
        elif name.isspace():
            print("Can't accept only spaces =")
        else:
            print("Contact already exists =")
        return False
    return True


# Adds new contact record to phonebook
def add_contact(phonebook: dict):
    contact_data = {"Phone number": "",
                    "E-mail": "",
                    "Address": ""
                    }
    print("Enter contact name")
    name = input("Name: -> ")

    if check_available(name, phonebook.keys()):
        print(f"Enter < {name} > contact data")

        for info in contact_data.keys():
            contact_data[info] = input(f"{info}: > ")

        phonebook[name] = contact_data
        print(f"Contact < {name} > created.")

    return phonebook


# Removes contact record from phonebook
def delete_contact(name: str, phonebook: dict):
    if name in phonebook.keys():
        if input(f"Type 'yes' if you agree to delete < {name} >: -> ").lower() == "yes":
            phonebook.pop(name)
            print(f"= Contact < {name} > deleted =")
    else:
        print(f"= Contact < {name} > doesn't exist =")
    return phonebook


# Displays all contacts which have any matches with searched name
def search(match: str, phonebook: dict):
    found = []
    for name in phonebook.keys():
        if match.lower() in name.lower():
            found.append(name)
    if not found:
        print(f"< {match} > not found")
    else:
        print("Matches found in:")
        for finding in found:
            print(f"< {finding} >")
    return phonebook


# Displays all recorded names in phonebook
def list_names(phonebook: dict):
    if not phonebook.keys():
        print("= There is no contacts yet =")
    else:
        print("Recorded contacts:")
        for contact in phonebook.keys():
            print(f" < {contact} >")
    return phonebook


# Displays selected contact info
def show_name(name: str, phonebook: dict):
    if name not in phonebook.keys():
        print(f"= There is no contact < {name} > =")
    else:
        print(f"< {name} >")
        for info, data in phonebook[name].items():
            print(f" - {info}: {data}")
    return phonebook


# Extracts name parameter from user's query
def extract_name(entry: str):
    entry = entry.strip()
    if len(entry) >= 3 and entry[0] == "<" and entry[-1] == ">":
        name = entry[1:-1].strip()
        return name
    return ""


# Extracts command from user's query
def extract(executable: str):
    first_space = executable.find(" ")
    command = executable.strip()[:first_space]
    if first_space == -1:
        command = executable.strip()
    name = extract_name(executable[first_space:])
    return {"command": command, "name": name}


# Displays list of commands with descriptions
def show_help():
    help_info = {"=COMMAND=": "=DESCRIPTION=",
                 "add": "create new contact",
                 "delete <name>": "delete selected contact",
                 "exit": "finish program operation",
                 "help": "show description of all commands",
                 "list": "show all contacts names",
                 "search <name>": "show contacts with matches in name",
                 "show <name>": "show selected contact data",
                 "stats": "show total records quantity"
                 }

    for item, description in help_info.items():
        spaces = " " * (15 - len(item))
        separator = "  -  "
        if item == "=COMMAND=":
            separator = "     "
        print(f"{item+spaces}{separator}{description}")


# Executes user's command
def execute_command(command: str, phonebook: dict) -> dict:
    executable = extract(command)

    match executable["command"].lower():
        case "stats":
            return show_stats(phonebook)

        case "add":
            return add_contact(phonebook)

        case "delete":
            if executable["name"]:
                return delete_contact(executable["name"], phonebook)
            print("= Invalid syntax or no name entry =")

        case "list":
            return list_names(phonebook)

        case "show":
            if executable["name"]:
                return show_name(executable["name"], phonebook)
            print("= Invalid syntax or no name entry =")

        case "search":
            if executable["name"]:
                return search(executable["name"], phonebook)
            print("= Invalid syntax or no name entry =")

        case "help":
            show_help()

        case _:
            print(f"= Invalid command \'{executable['command']}\'. Try 'help' for info =")

    return phonebook


# Starts program and receives user's commands
def main(phonebook={}):
    print("       ========= PHONEBOOK  V.0.1.1 =========")
    print("              = Welcome to PHONEBOOK =")
    print("       You can always execute 'help' for info")
    command = ""
    while command.lower() != "exit":
        print("--------------------------------------------------------")
        command = input("@-> ")
        if not command or command == "exit":
            continue
        else:
            print("--------------------------------------------------------")
            phonebook = execute_command(command, phonebook)


if __name__ == "__main__":
    main()
