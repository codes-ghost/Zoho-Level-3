flights = {}
customerDetails = {}
bId = 1


def loadFlights(n):
    for i in range(n):
        flights[i + 1] = 50


loadFlights(2)


def calculateTicketPrice(ticketsAvailable, ticketsRequired):
    ticketsSold = 50 - ticketsAvailable
    sugePrice = ticketsSold * 200
    if int(ticketsRequired) <= ticketsAvailable:  # number of tickets available is greater than required
        print("Ticket booking successful..!!")
    elif ticketsAvailable < 0:  # number of tickets available is lesser than required
        print(f"{ticketsAvailable} tickets have been booked successfully")


def booking():
    global bId
    print()
    print(f"{list(flights.keys())} are the flightID's")
    choice = input("Enter your flight ID : ")
    if int(choice) in flights:
        ticketsAvailable = flights[int(choice)]
    else:
        print("Enter a valid flight ID..!!")
        return
    if tickets <= 0:  # returning from the function due to flight is full
        print("There are no available tickets in the selected flight")
        return
    print(f"{choice} flight has been selected --- {ticketsAvailable} tickets are available.")
    ticketsRequired = input("Enter the number of tickets to book : ")


    price = calculateTicketPrice(ticketsAvailable, int(ticketsRequired) )
    cust = Customer(bId, int(choice), int(ticketsRequired), ticketPrice)
    bId += 1
