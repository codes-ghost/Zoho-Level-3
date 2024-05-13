from backend import *

print("-----WELCOME TO RAILWAY BOOKING SYSTEM-----")
while True:
    print("1. Book ticket | 2. Cancel Ticket | 3. Ticket Details | 0. Break")
    choice = input("Enter your choice : ")
    if choice in "1230.":
        if choice == "0":
            break
        elif choice == "1":
            booking(False, None)
        elif choice == "2":
            cancelTicket()
        elif choice == "3":
            printTicketDetails()
        elif choice == ".":
            printsystemdata()
        else:
            print("Enter a valid input..!!")
