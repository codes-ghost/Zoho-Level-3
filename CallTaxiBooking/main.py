from backend import *

while True:
    print("1. Booking | 2. Taxi Details | 0. Exit")
    choice = input("Enter your choice : ")
    if choice in " 120":
        if choice == "1":
            booking()
        elif choice == "2":
            taxiDetails()
        elif choice =="0":
            break
        else:
            print("Enter a valid input!")
