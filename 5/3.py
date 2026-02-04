choice = None

papa = {
    "1" : "2",
    "2" : "3"
    }

while choice != "0":
    print(
        """
        Papa connect
        0-exit
        1-find connection
        2-add connection
        3-remove connection
        4-grandfather connection
        """)
    choice = input("Choice: ")
    print()
    if choice == "0":
        print("Bye!")

    elif choice == "1":
        pap = input("Papa's name: ")
        if pap in papa:
            son = papa[pap]
            print("\n", pap, " is father for ", son)
        else:
            print("smth is wrong")
    elif choice == "2":
        pap = input("Father's name: ")
        if pap not in papa:
            son = input("\nSon's name: ")
            papa[pap] = son
            print("Done!")
        else:
            print("\nAlready exist")
    elif choice == "3":
        pap = input("Father's name: ")
        if pap in papa:
            del papa[pap]
            print("Done!")
        else:
            print("\nNobody have seen your father")
    elif choice == "4":
        pap = input("Grandfather's name: ")
        if pap in papa:
            grandson = papa[papa[pap]]
            print("\n", pap, " is grandfather for ", grandson)
        else:
            print("No connection")
