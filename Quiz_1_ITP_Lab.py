topList = []
midList = []
bottomList = []
x = 1

def menu():
    print("Choose a Fridge")
    print("[1] Top Fridge")
    print("[2] Mid Fridge")
    print("[3] Bottom Fridge")
    print("[0] Exit")
    choose = int(input("Select a number : "))

    if(choose == 1):
        print("TOP FRIDGE")
        print("[1] Put a item")
        print("[2] Take a item")
        print("[3] See item")
        choose1 = int(input("Select a number : "))
        if (choose1 == 1):
            input_top()
        elif (choose1 == 2):
            take_top()
        elif (choose1 == 3):
            for o in range(len(topList)):
                print(o + 1, ".", topList[o])
            menu()

    elif (choose == 2):
        print("MID FRIDGE")
        print("[1] Put a item")
        print("[2] Take a item")
        print("[3] See item")
        choose1 = int(input("Select a number : "))
        if (choose1 == 1):
            input_mid()
        elif (choose1 == 2):
            take_mid()
        elif (choose1 == 3):
            for o in range(len(midList)):
                print(o + 1, ".", midList[o])
            menu()

    elif (choose == 3):
        print("BOTTOM FRIDGE")
        print("[1] Put a item")
        print("[2] Take a item")
        print("[3] See item")
        choose1 = int(input("Select a number : "))
        if (choose1 == 1):
            input_bottom()
        elif (choose1 == 2):
            take_bottom()
        elif (choose1 == 3):
            for o in range(len(bottomList)):
                print(o + 1, ".", bottomList[o])
            menu()
    elif choose == 0:
        exit()
    else:
        print("Wrong Input")

def input_top():
    item = input("Input a item : ")
    length = int(input("Input a amount : "))
    if length <= 15 and length >= 0:
        for i in range(length):
            topList.append(item)
        menu()
    else:
        print("You input too many item (Max 15)")
        input_top()

def input_mid():
    item = input("Input a item : ")
    length = int(input("Input a amount : "))
    if length <= 15 and length >= 0:
        for i in range(length):
            midList.append(item)
        menu()
    else:
        print("You input too many item (Max 15)")
        input_mid()

def input_bottom():
    item = input("Input a item : ")
    length = int(input("Input a amount : "))
    if length <= 15 and length >= 0:
        for i in range(length):
            bottomList.append(item)
        menu()
    else:
        print("You input too many item (Max 15)")
        input_bottom()

def take_top():
    for o in  range(len(topList)):
        print(o+1,".", topList[o])
    inp1 = int(input("Select an item you want to take : "))
    del topList[inp1-1]
    for o in  range(len(topList)):
        print(o+1,".", topList[o])
    menu()

def take_mid():
    for o in  range(len(midList)):
        print(o+1,".", midList[o])
    inp1 = int(input("Select an item you want to take : "))
    del midList[inp1-1]
    for o in  range(len(midList)):
        print(o+1,".", midList[o])
    menu()

def take_bottom():
    for o in  range(len(bottomList)):
        print(o+1,".", bottomList[o])
    inp1 = int(input("Select an item you want to take : "))
    del bottomList[inp1-1]
    for o in  range(len(bottomList)):
        print(o+1,".", bottomList[o])
    menu()
menu()


