import heapq

from taxi import Taxi
bookingId = 1
points = ['a','b','c','d','e']
taxis = {} # id : taxi(object)
def loadTaxi():#initializes the taxi
    for i in range(2):
        taxi = Taxi(i+1)
        taxis[i+1] = taxi
loadTaxi()


def updateDetails(chosenOne, pickupPoint, dropPoint, time):
    global bookingId
    taxi = taxis[chosenOne]
    taxi.currentPoint = dropPoint
    timeTook = abs(ord(pickupPoint) - ord(dropPoint))
    taxi.freeTime = timeTook + int(time)
    totalDistance = 15 * timeTook
    amount = 100 + ((totalDistance-5) * 10)
    taxi.earnings += amount
    taxi.journeyDetails.append(f"{bookingId}.) PICKUP POINT : {pickupPoint.upper()}-->DROP POINT : {dropPoint.upper()} PICKUP TIME : {taxi.freeTime-timeTook}-> DROP TIME {taxi.freeTime}: Earnings : {amount}")
    bookingId += 1

def booking():
    pickupPoint = input("Enter your pickup point : ")
    dropPoint = input("Enter your drop point : ")
    time = int(input("Enter your pickup time : "))
    freeTaxiIds = []
    for id in taxis:
        taxi = taxis[id]
        if taxi.currentPoint == pickupPoint and taxi.freeTime <= time:
            freeTaxiIds.append(id)
    nearByTaxis = []
    if not freeTaxiIds:
        for id in taxis:
            taxi = taxis[id]
            distance = abs(ord(pickupPoint) - ord(taxi.currentPoint))
            if taxi.freeTime <= time:
                nearByTaxis.append([distance, id])
    chosenOne = 0
    currMax = float("inf")
    if len(freeTaxiIds) > 0:
        for id in freeTaxiIds:
            taxi = taxis[id]
            if taxi.earnings < currMax:
                chosenOne = id
                currMax = taxi.earnings
    elif len(nearByTaxis) > 0:
        nearByTaxis.sort()
        dist, id = nearByTaxis[0]
        chosenOne = id
    else:
        print("CURRENTLY THERE ARE NO TAXIS AVAILABLE FOR YOUR REQUIREMENTS.")
    print()
    if chosenOne != 0:
        print(f'Taxi {chosenOne} allocated successfully !!!!!!')
        print()
        updateDetails(chosenOne, pickupPoint, dropPoint, time)

def taxiDetails():
    print()
    print("=======PRINTING THE DETAILS OF THE TAXI=======")
    for id in taxis:
        taxi = taxis[id]
        print(f"TAXI-ID : {taxi.id} | AVAILABLE FROM : {taxi.freeTime} |TOTAL EARNINGS : {taxi.earnings}")
        for d in taxi.journeyDetails:
            print(d)
        print("--------------------------------------------------------")
    print()
    print("***************  DETAILS OF THE TAXIS HAVE BEEN PRINTED  ****************")
    print()
