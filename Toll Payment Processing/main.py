from backend import *
initiatingTolls()
while True:
    print('1. PLAN JOURNEY | 2. VIEW TOLL DETAILS | 0. EXIT')
    choice = input("Enter your choice : ")
    if choice in "120":
        if choice == "1":
            calculatePaths()
        elif choice == "2":
            viewTollDetails()
        elif choice == "0":
            print("EXIT")
            break
        else:
            print("Enter a valid input....")
