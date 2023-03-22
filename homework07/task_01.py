# ======== PHONEBOOK =========

# record = {name: {} }

# show qty of records
def stats():
    pass


# add record
def add():
    pass


# remove record by key "name"
def delete_record(name):
    pass


# display all names
def list_names():
    pass


# display all data
def show_name(name):
    pass


# take command
def execute_command(command, record_book):
    pass


def main():
    phonebook = {}
    command = None
    while command != "exit":
        command = input("@-> ")
        if not command or command == "exit":
            continue
        else:
            pass
    pass


if __name__ == "__main__":
    main()
