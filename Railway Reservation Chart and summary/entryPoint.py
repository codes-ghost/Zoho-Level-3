from backend import *

while True:
    print("1.BOOK | 2.CANCEL | 3.PRINT SUMMARY AND CHART | 4.PRINT STATIONS | 5.EXIT")
    choice = input("Enter your choice : ")
    if choice in "12345":
        if choice == "1":
            src = input("Enter the source : ").upper()
            dst = input("Enter the destination : ").upper()
            n = input("Enter the number of tickets : ")
            book(src, dst, int(n))
        elif choice == "2":
            pnr = input("Enter the PNR number : ")
            n = input("Enter the number of tickets to cancel : ")
            cancel(int(pnr), int(n))
        elif choice == "3":
            chart()
        elif choice == "4":
            printStations()
        elif choice == "5":
            print("THANKYOU...!!!")
            break
