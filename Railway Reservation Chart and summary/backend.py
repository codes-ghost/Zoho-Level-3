from passenger import Passenger

stations = {"A": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]},
            "B": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]},
            "C": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]},
            "D": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]},
            "E": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]}, }
stationChart = {"A": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]},
                "B": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]},
                "C": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]},
                "D": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]},
                "E": {"seats": [1, 2, 3, 4, 5, 6, 7, 8], "wl": ["WL1", "WL2"]}, }
bookingDetails = []
pnr = 1
passengerDetails = {}
waitingListPassenger = {}


def bookingNotPossible(src, dst, n):
    for station in range(ord(src), ord(dst) + 1):
        if len(stations[chr(station)]["seats"]) + len(stations[chr(station)]["wl"]) < n:
            bookingDetails.append("No seats available..!!")
            return True
    return False


def printStations():
    for key in stations:
        seats = stations[key]["seats"]
        hold = stations[key]["wl"]
        print(f"station : {key} | Available : {seats} | HOLD:{hold}")


def updateStationChartAfterBooking(src, dst, n):
    for key in range(ord(src), ord(dst) + 1):
        temp = n
        while temp > 0 and len(stationChart[chr(key)]["seats"]) > 0:
            stationChart[chr(key)]["seats"].pop(0)
            temp -= 1
        while temp > 0 and len(stationChart[chr(key)]["wl"]) > 0:
            stationChart[chr(key)]["wl"].pop(0)
            temp -= 1


def chooseSeats(src, dst, n):
    confirmedSeats, seatsOnHold = set(), set()
    for key in range(ord(src), ord(dst)):
        temp = n
        while temp > 0 and len(stations[chr(key)]["seats"]) > 0:
            confirmedSeats.add(stations[chr(key)]["seats"].pop(0))
            temp -= 1
        while temp > 0 and len(stations[chr(key)]["wl"]) > 0:
            seatsOnHold.add(stations[chr(key)]["wl"].pop(0))
            temp -= 1
    return [list(confirmedSeats), list(seatsOnHold)]


def book(source, destination, numberOfTickets):
    global pnr
    if bookingNotPossible(source, destination, numberOfTickets):
        print("Tickets not available")
        return
    confirmedSeats, seatsOnHold = chooseSeats(source, destination, numberOfTickets)
    passenger = Passenger(pnr, source, destination, confirmedSeats, seatsOnHold)
    bookingDetails.append(f"PNR : {pnr} src:{source}->dst{destination} | seats:{confirmedSeats} |holding:{seatsOnHold}")
    # updating the stations to print the chart
    updateStationChartAfterBooking(source, destination, numberOfTickets)
    passengerDetails[pnr] = passenger
    if len(seatsOnHold) > 0:
        waitingListPassenger[(source, destination)] = passenger
    pnr += 1


def chart():
    for i in bookingDetails:
        print(i)
    seats = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], "wl1": [], "wl2": []}
    for i in range(1, 9):
        for station in stationChart:
            if i in stationChart[station]["seats"]:
                seats[i].append("_")
            else:
                seats[i].append("*")

    print("  A B C D E")
    i = 1
    for k in seats:
        if i == 9:
            break
        print(i, " ".join(seats[k]))
        i += 1
    print(" ".join(seats["wl1"]))
    print(" ".join(seats["wl2"]))

    for key in stationChart:
        seats = stationChart[key]["seats"]
        hold = stationChart[key]["wl"]
        print(f"station : {key} | Available : {seats} | HOLD:{hold}")


def checkPossibilitiesForEveryWaitingListPassengers():
    for key in waitingListPassenger:
        passenger = waitingListPassenger[key]
        src, dst = passenger.src, passenger.dst
        n = len(passenger.seatsOnHold)
        canAccomodate = False
        for station in range(ord(src), ord(dst) + 1):
            if len(stations[chr(station)]["seats"]) >= n:
                canAccomodate = True
        if canAccomodate:
            confirmedSeats, seatsOnHold = chooseSeats(src, dst, n)
            passenger.seatsConfirmed = confirmedSeats
            passenger.seatsOnHold = seatsOnHold
            bookingDetails.append(
                f"PNR : {passenger.pnr} src:{src}->dst{dst} | seats:{confirmedSeats} |holding:{seatsOnHold}")
            updateStationChartAfterBooking(src, dst, n)
            waitingListPassenger.pop(key)
            break


def checkPossibilitiesForWaitingList(s, d):
    if (s, d) in waitingListPassenger:
        passenger = waitingListPassenger[s, d]
        wlSeatsBooked = passenger.seatsOnHold
        newSeats = set()
        for i in range(len(wlSeatsBooked)):
            wlSeatRevoked = set()  # a set to make a note of cancelled seat number and
            wlSeatRevoked.add(passenger.seatsOnHold.pop(0))
            for station in range(ord(s), ord(d)):
                for seatNumber in stations[chr(station)]["wl"]:
                    wlSeatRevoked.add(seatNumber)
                stations[chr(station)]["wl"] = list(wlSeatRevoked)
                newSeats.add(stations[chr(station)]["seats"].pop(0))

            for station in range(ord(s), ord(d) + 1):
                stationChart[chr(station)]["wl"] = list(wlSeatRevoked)
                stationChart[chr(station)]["seats"].pop(0)
        for seat in passenger.seatsConfirmed:
            newSeats.add(seat)
        passenger.seatsConfirmed = list(newSeats)
        bookingDetails.append(f"PNR : {passenger.pnr} src:{s}->des{d} | seats : {passenger.seatsConfirmed}")
        waitingListPassenger.pop((s, d))
    checkPossibilitiesForEveryWaitingListPassengers()


def cancel(pnrNumber, ticketsToCancel):
    passenger = passengerDetails[pnrNumber]
    src, dst = passenger.src, passenger.dst
    cancelledWaitingList, cancelledConfirmSeats = set(), set()
    while ticketsToCancel > 0 and len(passenger.seatsOnHold) > 0:
        cancelledWaitingList.add(passenger.seatsOnHold.pop(0))
        ticketsToCancel -= 1
    while ticketsToCancel > 0 and len(passenger.seatsConfirmed) > 0:
        cancelledConfirmSeats.add(passenger.seatsConfirmed.pop(0))
        ticketsToCancel -= 1
    cancelledSeats = []
    for s in cancelledWaitingList:
        cancelledSeats.append(s)
    for s in cancelledConfirmSeats:
        cancelledSeats.append(s)
    # updating stations:
    for key in range(ord(src), ord(dst)):
        for seat in stations[chr(key)]["seats"]:
            cancelledConfirmSeats.add(seat)
        for seat in stations[chr(key)]["wl"]:
            cancelledWaitingList.add(seat)
        stations[chr(key)]["seats"] = sorted(list(cancelledConfirmSeats))
        stations[chr(key)]["wl"] = sorted(list(cancelledWaitingList))

    # updating stationChart:
    for key in range(ord(src), ord(dst) + 1):
        for seat in stationChart[chr(key)]["seats"]:
            cancelledConfirmSeats.add(seat)
        for seat in stationChart[chr(key)]["wl"]:
            cancelledWaitingList.add(seat)
        stationChart[chr(key)]["seats"] = sorted(list(cancelledConfirmSeats))
        stationChart[chr(key)]["wl"] = sorted(list(cancelledWaitingList))
    bookingDetails.append(
        f"PNR : {pnrNumber} src:{src}->dst{dst} | seats:{passenger.seatsConfirmed} |seatsCancelled:{list(cancelledSeats)}")

    checkPossibilitiesForWaitingList(src, dst)
