def menu():
    print("sel 1")
    print("sel 2")
    print("sel 3")

menu()
menu_selection = int(input("enter your selection: "))
while menu_selection != 0:
    if menu_selection == 1:
        print("punk")
        #do opt 1
    elif menu_selection == 2:
        print("ass")
        #do opt 2
    elif menu_selection == 3:
        print("bitch")
        #do opt 3
    else:
        print("not a vailid selection")