def addNum(name, num, teleDict):
    teleDict.update({name:num})
    print("Updated!\n")
    return

def removeNum(name, teleDict):
    if name in teleDict:
        del teleDict[name]
    else:
        print("Name not found.\n")
    return


def lookUpNum(name, teleDict):
    if name in teleDict:
        print('Name: ', name)
        print(f"Number: {teleDict[name]}\n")
    else:
        print(f"{name} Not Found.\n")
    return


telephone_dict = {'Johnny': '111-111'}
while True:
    usr_choice = input("What would you like to do to the phone book today?\nOptions: Add, Remove, Lookup, Print, EXIT: ")

    if usr_choice == 'Add':
        usr_NameNum = input("Enter new name: ")
        usr_number = input(f"Enter new number of {usr_NameNum}:")
        addNum(usr_NameNum, usr_number, telephone_dict)
    elif usr_choice == 'Remove':
        usr_Remove = input("Enter name to remove: ")
        removeNum(usr_Remove, telephone_dict)
    elif usr_choice == 'Lookup':
        usr_name = input("Enter name: ")
        lookUpNum(usr_name, telephone_dict)
    elif usr_choice == 'Print':
        [print(f"Telephone Book:\n{key}: {value}") for key, value in telephone_dict.items()]
        print()
    elif usr_choice == 'EXIT':
        print(telephone_dict)
        break
    else:
        print("Invalid Option")