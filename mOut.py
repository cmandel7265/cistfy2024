def sCart():
        sList = input("Please write a list of what you wish to purchase. ")
        print(sList)
        mod = input("Do you wish to modify your list? ")
        if mod == "yes":
            while mod == "yes":
                modType = input("What do you wish to do? ")
                if modType == "add":
                    slistAdd = input("Please input what you wish to add to your list. ")
                    print(sList)
                    print(slistAdd)
                    finalize = input("Are you done adding to your list? ")
                    if finalize == "yes":
                        print(sList)
                        print(slistAdd)
                        print("Thank you for your list. Have a nice day! ")
                        exit()
                    elif finalize == "no":
                        slistAdd = input("Please input what you wish to add to your list. ")
                    else:
                        print("Sorry, that input was unrecognized. Please restart the program to try again. ")
                if modType == "redo":
                        slist = input("Please write a list of what you wish to purchase? ")
                        print(sList)
                else:
                        print("Sorry, that input was unrecognized. Please restart the program to try again. ")
                
        elif mod == "no":
                print(sList)
                print("Thank you for your time. Have a nice day! ")
        else:
                print("Sorry, that input was unrecognized. Please restart the program to try again. ")
    sCart()