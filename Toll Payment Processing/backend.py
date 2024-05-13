from classes import *

tolls = {}


def initiatingTolls():
    t1 = Toll("1", False, 0)
    t2 = Toll("2", True, 50)
    t3 = Toll("3", True, 60)
    t4 = Toll("4", False, 0)
    t5 = Toll("5", True, 80)
    tolls[1] = t1
    tolls[2] = t2
    tolls[3] = t3
    tolls[4] = t4
    tolls[5] = t5





def calculateShortestPath(src, dst):
    src, dst = int(src), int(dst)
    forward = 0
    for i in range(src, dst + 1):
        if i in tolls:
            toll = tolls[i]
            if toll.ischargeable:
                forward += toll.payment
    reverse = 0
    curr = dst
    while True:
        if curr == src+1:
            break
        toll = tolls[curr]
        if toll.ischargeable:
            reverse += toll.payment
        curr += 1
        if curr not in tolls:
            curr = 1
    if forward > reverse:
        return ["Reverse", reverse]
    else:
        return ["Forward", forward]



def calculatePaths():
    # printing the toll names
    print("----PRINTING THE POINT NAMES---")
    for id in tolls:
        toll = tolls[id]
        print(toll.name, end=" ")
    print()
    src = int(input("ENTER THE SOURCE POINT TO : "))
    dst = int(input("ENTER THE DESTINATION POINT :"))

    dir, tot = calculateShortestPath(src, dst)

    vechileNumber = input("ENTER YOUR VEHICLE NUMBER : ")
    isVip = input("ENTER 1.VIP/2.NORMAL USER : ")
    if isVip == "1":
        isVip = True
    else:
        isVip = False
    if dir == "Reverse":
        print(f'TOTAL COST FOR THE JOURNEY WOULD BE : {tot}')
        print("---THE CURRENT PATH IS---")
        curr = src
        while True:
            if curr == dst-1:
                break
            print(curr, end="->>")
            toll = tolls[curr]
            amountPaid = toll.payment
            if isVip:
                amountPaid = toll.payment - (toll.payment* (20))//100
            toll.vechicleDetails.append(f"VEHICLE NUMBER : {vechileNumber} passed {amountPaid} collected")
            toll.revenue += amountPaid
            curr -= 1
            if curr not in tolls:
                curr = max(tolls.keys())
    else:
        # print(f'TOTAL COST FOR THE JOURNEY WOULD BE : {tot}')
        print("---THE CURRENT PATH IS---")
        for i in range(src, dst):
            toll = tolls[i]
            amountPaid = toll.payment
            if isVip:
                amountPaid = toll.payment -(toll.payment*20)//100
            toll.revenue += amountPaid
            toll.vechicleDetails.append(f"VEHICLE NUMBER : {vechileNumber} passed {amountPaid} collected")
            print(i, end="->>")
    print()
    print("ROUTE CALCULATED SUCESSFULLY....")



def viewTollDetails():
    for id in tolls:
        toll = tolls[id]
        print(f'name {toll.name} revenue {toll.revenue}')
        for j in toll.vechicleDetails:
            print(j)