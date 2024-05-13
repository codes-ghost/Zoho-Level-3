from collections import deque

from passenger import Passenger

ticketDetails = {}
racDetails = {}
wlDetials = {}
racQueue = deque()
wlQueue = deque()
bId = 1
upperBerths = 1
lowerBerths = 1
middleBerths = 1
rac = 1
wl = 1


def booking(isarg, parameters):
    global lowerBerths, middleBerths, upperBerths, rac, wl, bId
    if not isarg:
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        gender = input("Enter your gender M/F : ").upper()
        isHavingChild = False
        if gender == "F":
            choice = input("Do you have a child 1.Yes / 2.No : ")
            if choice == "1":
                isHavingChild = True
        berth = input("Enter your berth preference L/U/M : ").upper()
        age = int(age)
    else:
        name, age, gender, isHavingChild, berth = parameters
    passenger = Passenger(name, age, gender, isHavingChild, berth)
    passenger.allotedBerth = None
    if passenger.age < 5:
        ticketDetails[bId] = passenger
        print("TICKET BOOKED SUCCESSFULLY!!")
    elif lowerBerths > 0 and (passenger.age >= 65):
        print("special previlage !!!")
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "lowerBerths"
        lowerBerths -= 1
    elif lowerBerths > 0 and (passenger.gender == "F" and isHavingChild):
        print("special previlage !!!")
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "lowerBerths"
        lowerBerths -= 1
    elif passenger.berth == "L" and lowerBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "lowerBerths"
        lowerBerths -= 1
    elif passenger.berth == "M" and middleBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "middleBerths"
        middleBerths -= 1
    elif passenger.berth == "U" and upperBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "upperBerths"
        upperBerths -= 1
    elif upperBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "upperBerths"
        upperBerths -= 1
    elif middleBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "middleBerths"
        middleBerths -= 1
    elif lowerBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "lowerBerths"
        lowerBerths -= 1
    elif rac > 0:
        passenger.allotedBerth = "rac"
        rac -= 1
        racQueue.append([passenger, bId])
        racDetails[bId] = passenger
    elif wl > 0:
        passenger.allotedBerth = "wl"
        wl -= 1
        wlQueue.append([passenger, bId])
        wlDetials[bId] = passenger
    else:
        print("CURRENTLY THERE ARE NO TICKETS AVAILABLE..!!")
        return
    print()
    print("Ticket booking successful..!!")
    print(passenger.allotedBerth, " has been booked..!!")
    print()
    bId += 1


def allocateSeatFromWL():
    global wl

    passenger, bId = wlQueue.popleft()
    passenger.allotedBerth = "rac"
    wl += 1
    wlDetials.pop(bId)
    racQueue.append([passenger,bId])
    racDetails[bId] = passenger

def allocateSeatFromRac():
    global upperBerths, middleBerths, lowerBerths, rac
    passenger, bId = racQueue.popleft()
    if upperBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "upperBerths"
        upperBerths -= 1
    elif middleBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "middleBerths"
        middleBerths -= 1
    elif lowerBerths > 0:
        ticketDetails[bId] = passenger
        passenger.allotedBerth = "lowerBerths"
        lowerBerths -= 1
    rac += 1
    racDetails.pop(bId)
    if wlQueue:
        allocateSeatFromWL()

def cancelTicket():
    global lowerBerths, upperBerths, middleBerths
    print(f"{list(ticketDetails.keys())} are the confirmed booking ID's")
    print(f"{list(racDetails.keys())} are the RAC booking ID's")
    print(f"{list(wlDetials.keys())} are the WL booking ID's")
    bookingId = int(input("Enter your booking Id : "))
    print()
    if bookingId in ticketDetails:
        passenger = ticketDetails[bookingId]
        print(f'YOUR TICKET {passenger.allotedBerth} berth HAS BEEN CANCELLED SUCCESSFULLY..!!')
        if passenger.allotedBerth == "lowerBerths":
            lowerBerths += 1
        elif passenger.allotedBerth == "upperBerths":
            upperBerths += 1
        elif passenger.allotedBerth == "middleBerths":
            middleBerths += 1
        ticketDetails.pop(bookingId)
        if racQueue:
            allocateSeatFromRac()
    elif bookingId in racDetails:
        racDetails.pop(bookingId)
        allocateSeatFromRac()
    elif bookingId in wlDetials:
        wlDetials.pop(bookingId)
        allocateSeatFromWL()

def printTicketDetails():
    print()
    for id in ticketDetails:
        passenger = ticketDetails[id]
        print(f"{id}.) NAME : {passenger.name} | BERTH : {passenger.allotedBerth}")
    for id in racDetails:
        passenger = racDetails[id]
        print(f"{id}.) NAME : {passenger.name} | BERTH : {passenger.allotedBerth}")
    for id in wlDetials:
        passenger = wlDetials[id]
        print(f"{id}.) NAME : {passenger.name} | BERTH : {passenger.allotedBerth}")
    print()
    print("========================================================================")
    print()

def printsystemdata():
    print("lowerBerths : ", lowerBerths)
    print("upperBerths : ", upperBerths)
    print("middleberths : ", middleBerths)

# booking(True,)