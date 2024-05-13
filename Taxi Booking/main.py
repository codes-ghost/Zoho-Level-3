from backend import *
def main():
    createTaxi()

    customerId = 1
    while True:
        print("1.Booking |2.JourneyDetials | 5.TaxiDetails | 0.Exit")
        choice = input("Enter your choice : ")
        if choice == "1":
            pickupPoint = input("Enter the pickup point : ").upper()
            dropPoint = input("Enter the drop point : ").upper()
            pickupTime = input("Enter the pickup Time : ")
            booking(customerId, pickupPoint,dropPoint, int(pickupTime))
        elif choice == "2":
            journeyDetails()
        elif choice == "0":
            break
        elif choice == "5":
            viewTaxi()
        else:
            print("Enter a valid input...")

main()