def add_all_args(datatype="numbers", *args):
    if not args:
        return None

    match datatype:
        case "numbers":
            result = 0
        case "text":
            result = ""
        case _:
            return "Invalid data type"

    for item in args:
        result += item

    return result


def enter_elements(datatype):
    entry = True
    values = []
    print("--------------------------------------------------")
    print("Enter your elements (to stop press 'enter').")
    print("--------------------------------------------------")
    while entry:
        entry = input("Add element: -> ")
        if not entry:
            continue
        elif datatype == "text":
            values.append(entry)
        else:
            if not entry.isdigit():
                print("Only natural numbers accepted. Value not added.")
                continue
            else:
                values.append(int(entry))
    return values


def main():
    print("Do you want to add text or numbers?")
    print("'1' - numbers\n'2' - text")

    selection = input("Type '1' or '2': -> ")

    match selection:
        case "1":
            selected_type = "numbers"
        case "2":
            selected_type = "text"
        case _:
            print("----- Retry -----")
            main()

    print(f"{selected_type.upper()} selected")

    all_elements = list(enter_elements(selected_type))

    print(f"RESULT : {add_all_args(selected_type, *all_elements)}")

#    print(add_all_args(selected, *all_elements))
    print("--------------------------------------------------")

    if input("Type 'R' to restart or anything else to finish: -> ").lower() == "r":
        print("--------------------------------------------------")
        main()



if __name__ == "__main__":
    main()
    add_all_args()
