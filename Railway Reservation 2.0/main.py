from railwayDatabase import *
def bookTicket():
    if RailwayDatabase.trainsAvailable <= 0:
        print("There are no train tickets available")
        return
    name = input("Enter your name : ")

    for i in range(len(RailwayDatabase.stations)):
        print(f'{i}=>{RailwayDatabase.stations[i]}', end=" ")
    print()
    fromStation = int(input("Enter the source station number : "))
    for j in range(int(fromStation) + 1, len(RailwayDatabase.stations)):
        print(f'{j}=>{RailwayDatabase.stations[j]}', end=" ")
    print()
    toStation = int(input("Enter the destination station number : "))
    coach = input("Enter your coach preference 1. AC || 2. Normal : ")
    while True:
        if coach in "12":
            coach = int(coach)
            break
        else:
            coach = input("Enter your coach preference 1. AC || 2. Normal enter 1 or 2 : ")
    getTicket(name, fromStation, toStation, coach)
def entryPoint():
    while True:
        print("1.Book ticket || 2.Cancel booking || 3.View Ticket || 4. View Revenue || 0. Exit")
        choice = input("Enter your choice : ")
        if choice in ["1", "2", "3", "4", "0"]:
            if int(choice) == 1:
                bookTicket()
            elif int(choice) == 2:
                cancelBookedTickets()
            elif int(choice) == 3:
               viewBookedTickets()
            elif int(choice) == 4:
                viewRevenue()
            elif int(choice) == 0:
                break
        else:
            print("Enter a valid input")
            continue


entryPoint()
