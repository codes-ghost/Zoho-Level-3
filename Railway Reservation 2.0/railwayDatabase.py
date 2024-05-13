class RailwayDatabase:
    stations = ["chennai", "katpadi", "salem", "erode", "coimbatore"]
    revenue = 0
    AC = 2
    ACWaitList = 2
    ACWaitlistPassengerList = []
    normal = 5
    normalWaitList = 2
    normalWaitListPassengerList = []
    trainsAvailable = 1
    normalFare = 10
    acFare = 20
    surgePrice = 0
    bookedTickets = {}


def viewBookedTickets():
    if len(RailwayDatabase.bookedTickets) == 0:
        print("Currently there are no tickets booked")
        print("================================================================================")
        return
    print("================================================================================")
    for data in RailwayDatabase.bookedTickets:
        amount, berth, name = RailwayDatabase.bookedTickets[data]
        if berth == 1:
            print(f"{name} has booked a AC ticket")
            print("================================================================================")
        else:
            print(f"{name} has booked a Normal ticket")
            print("================================================================================")
    return


def getTicket(name, source, destination, coach):
    ticketID = len(RailwayDatabase.bookedTickets) + 1
    if coach == 1:
        if RailwayDatabase.AC <= 0 and RailwayDatabase.ACWaitList <= 0:
            print("There are no AC coach available")
        elif RailwayDatabase.AC <= 0 < RailwayDatabase.ACWaitList:
            RailwayDatabase.ACWaitlist -= 1
            RailwayDatabase.ACWaitlistPassengerList.append([name, source, destination, coach])
        ticketPrice = (destination - source) * RailwayDatabase.acFare + (RailwayDatabase.surgePrice * 5)
        RailwayDatabase.AC -= 1
        RailwayDatabase.bookedTickets[ticketID] = [(destination - source) * RailwayDatabase.acFare, 1, name]
    else:
        if RailwayDatabase.normal <= 0 and RailwayDatabase.normalWaitList <= 0:
            print("There are no seats available")
        elif RailwayDatabase.AC <= 0 < RailwayDatabase.normalWaitList:
            RailwayDatabase.normalWaitList -= 1
            RailwayDatabase.normalWaitListPassengerList.append([name, source, destination, coach])
        ticketPrice = (destination - source) * RailwayDatabase.normalFare
        RailwayDatabase.normal -= 1
        RailwayDatabase.bookedTickets[ticketID] = [ticketPrice, 0, name]
    RailwayDatabase.revenue += ticketPrice
    RailwayDatabase.surgePrice += 1
    print("================================================================================")
    print(ticketID, " : ticketID has been booked successfully for ", ticketPrice, " amount")
    print("================================================================================")
    return


def cancelBookedTickets():
    # Checking if any tickets has been booked
    if len(RailwayDatabase.bookedTickets) == 0:
        print("There are no tickets booked")
        return
    print("================================================================================")
    print("Tickets booked : ", end="")
    print("================================================================================")
    for i in RailwayDatabase.bookedTickets:
        print(i, end=" ")
    print()
    ticketToCancel = int(input("Enter the ticket ID : "))
    amount, coach, name = RailwayDatabase.bookedTickets[ticketToCancel]
    # Cancelling AC ticket
    if coach == 1:
        print(amount, coach, " coach amount has been refunded")
        RailwayDatabase.bookedTickets.pop(ticketToCancel)
        RailwayDatabase.AC += 1
    # Cancelling normal tickets
    else:
        print(amount, " amount has been refunded")
        RailwayDatabase.bookedTickets.pop(ticketToCancel)
        RailwayDatabase.normal += 1
    RailwayDatabase.revenue -= amount
    RailwayDatabase.surgePrice -= 1
    print("================================================================================")
    # updating AC waitlist to confirm ticket
    if coach == 1:
        name, source, destination, coach = RailwayDatabase.ACWaitlistPassengerList[0]
        getTicket(name, source, destination, coach)
        RailwayDatabase.ACWaitlistPassengerList.pop(0)
    # updating  waitlist to confirm ticket
    else:
        name, source, destination, coach = RailwayDatabase.normalWaitListPassengerList[0]
        getTicket(name, source, destination, coach)
        RailwayDatabase.normalWaitListPassengerList.pop(0)


def viewRevenue():
    print(f"Currently the train has generated {RailwayDatabase.revenue} amount")
    print("================================================================================")
