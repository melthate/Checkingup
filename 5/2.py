st = 0
ag = 0
oi = 0
mu = 0
mx = 10
choice = None
statchoice = None
statchoice2 = None

while choice != "0":
    print(
        """
        Heroes generator
        0-exit
        1-add stat
        2-remove stat
        """)
    choice = input("Choice: ")
    print()
    if choice == "0":
        print("Bye!")

    elif choice == "1":
        while statchoice != "0":
            print("\nYou have left ", mx, " points")
            print("\nYour strength is: ", st)
            print("\nYour agility is: ", ag)
            print("\nYour intellect is: ", oi)
            print("\nYour wisdom is: ", mu)
            print(
            """
            0-exit from stats
            1-strength
            2-agility
            3-intellect
            4-wisdom
            """)
            statchoice = input("Stat choice: ")
            if statchoice == "1":
                a = int(input("how many do you want to up?: "))
                while a > mx or a < 0:
                    print("error")
                    a = int(input("how many do you want to up?: "))
                st += a
                mx -= a
            if statchoice == "2":
                a = int(input("how many do you want to up?: "))
                while a > mx or a < 0:
                    print("error")
                    a = int(input("how many do you want to up?: "))
                ag += a
                mx -= a
            if statchoice == "3":
                a = int(input("how many do you want to up?: "))
                while a > mx or a < 0:
                    print("error")
                    a = int(input("how many do you want to up?: "))
                oi += a
                mx -= a
            if statchoice == "4":
                a = int(input("how many do you want to up?: "))
                while a > mx or a < 0:
                    print("error")
                    a = int(input("how many do you want to up?: "))
                mu += a
                mx -= a

    elif choice == "2":
        while statchoice2 != "0":
            print("\nYou have left ", mx, " points")
            print("\nYour strength is: ", st)
            print("\nYour agility is: ", ag)
            print("\nYour intellect is: ", oi)
            print("\nYour wisdom is: ", mu)
            print(
            """
            0-exit from stats
            1-strength
            2-agility
            3-intellect
            4-wisdom
            """)
            statchoice2 = input("Stat choice: ")
            if statchoice2 == "1":
                a = int(input("how many do you want to down?: "))
                while a > st or a < 0:
                    print("error")
                    a = int(input("how many do you want to down?: "))
                st -= a
                mx += a
            if statchoice2 == "2":
                a = int(input("how many do you want to down?: "))
                while a > ag or a < 0:
                    print("error")
                    a = int(input("how many do you want to down?: "))
                ag -= a
                mx += a
            if statchoice2 == "3":
                a = int(input("how many do you want to down?: "))
                while a > oi or a < 0:
                    print("error")
                    a = int(input("how many do you want to down?: "))
                oi -= a
                mx += a
            if statchoice2 == "4":
                a = int(input("how many do you want to down?: "))
                while a > mu or a < 0:
                    print("error")
                    a = int(input("how many do you want to down?: "))
                mu -= a
                mx += a
                
