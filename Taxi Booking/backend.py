import heapq
from collections import defaultdict

from taxi import *
bookingId = 1
taxis = defaultdict(dict)
def createTaxi():
    for i in range(1,5):
        taxis[i] = Taxi(i)
def viewTaxi():
    for id in taxis:
        taxi = taxis[id]
        print(f"TaxiID - {taxi.taxiId} || TAXIEARNINGS-{taxi.earnings} || CURRENTPOINT-{taxi.currentPoint} ||FREETIME - {taxi.freeTime}")


def allocateTaxi(pickupPoint, pickupTime):
    chosenId = [] # distance between pickup and current location, taxiId
    for id in taxis:
        taxi = taxis[id]
        if taxi.freeTime <= pickupTime :
            chosenId.append([abs(ord(taxi.currentPoint)-ord(pickupPoint)), id])
    heapq.heapify(chosenId)
    print(chosenId)
    chosenOne = None
    for i in range(len(chosenId)-1):
        distance, id = chosenId[i]
        nextDistance, nextId = chosenId[i+1]
        if distance != nextDistance:
            return id
        if taxis[id].earnings <= taxis[nextId].earnings:
            return id
        else:
            chosenOne = nextId
    return chosenOne


def calculateAmount(pickupPoint, dropPoint):
    amt = 100
    amt += 10 *((abs(ord(pickupPoint) - ord(dropPoint)) * 15)-5 )
    return amt
def journeyDetails():
    for id in taxis:
        print(f"==>>Taxi {id} ==>>JOURNEY DETAILS==>>Earnings : {taxis[id].earnings}")
        taxi = taxis[id]
        if len(taxi.journeyDetails) == 0:
            print("No bookings ")
            continue
        for i in taxi.journeyDetails:
            print(i)
        print("--------------------------------------------------------------------")
def booking(customerId, pickupPoint, dropPoint, pickupTime):
    print(customerId, pickupPoint, dropPoint, pickupTime)
    taxiID = allocateTaxi(pickupPoint, pickupTime)

    if taxiID:
        print(f'TaxiID {taxiID} allocated successfully')
        amount = calculateAmount(pickupPoint, dropPoint)
        taxi = taxis[taxiID]
        taxi.freeTime = pickupTime + abs(ord(pickupPoint) - ord(dropPoint))
        taxi.earnings += amount
        taxi.currentPoint = dropPoint
        taxi.journeyDetails.append(f'PICKUP-{pickupPoint}==>>DROP==>>{dropPoint}|| EARNING==>>{amount}')
    else:
        print("currently there are no taxis available..")