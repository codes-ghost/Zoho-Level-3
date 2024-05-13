from bankDatabase import customerDetails, giftCardDatabase, updateTransaction
from customerClass import Customer


def successfulLogin(Customer):
    print("=======================================")
    while True:
        print("1. Create newGiftCard || 2. TopUp giftCard || 3. Block/Unblock gift card")
        print("4. Transaction History || 5. Logout")
        choice = int(input("Enter you choice : "))
        if choice == 1:
            Customer.createNewGiftCard()
        elif choice == 2:
            cardNumber = int(input("Enter the card number : "))
            Customer.TopUpGiftCard(cardNumber)
        elif choice == 3:
            Customer.activateGiftCard()
        elif choice == 4:
            Customer.getGiftCardTransaction()
        elif choice == 5:
            break


def login():
    print("Welcome you are currently in login Page")
    print("=======================================")
    accountID = int(input("Enter you account ID: "))
    while accountID not in customerDetails:
        accountID = int(input("Enter a valid account ID: "))
    accountPassword = input("Enter you account password: ")
    while accountPassword != customerDetails[accountID].password:
        accountID = input("Enter a valid password : ")
    print("successful Login")
    customer = customerDetails[accountID]
    successfulLogin(customer)


def purchasePage():
    print("You are in puchase page and about to checkout your bill using your giftcard")
    billAmount = int(input("Enter the amount of bill : "))
    if len(giftCardDatabase) == 0:
        print("There are no gift cards available")
        return
    for card in giftCardDatabase:
        print(card, end=" ")
    print("These are the gift cards available")

    giftCardNumber = int(input("Enter the gift card number : "))
    while giftCardNumber not in giftCardDatabase:
        giftCardNumber = int(input("Enter the gift card number : "))
    pinNumber = int(input("Enter the 4 digit PIN : "))
    while giftCardDatabase[giftCardNumber]["pinNumber"] != pinNumber:
        pinNumber = int(input("Enter the 4 digit PIN : "))
    if giftCardDatabase[giftCardNumber]["status"] == False:
        print("Your card has been blocked")
        return
    if billAmount > giftCardDatabase[giftCardNumber]["giftCardBalance"]:
        print("Insufficient balance")
        return
    giftCardDatabase[giftCardNumber]["giftCardBalance"] -= billAmount
    updateTransaction(giftCardNumber, billAmount)
    print(giftCardDatabase)
    pass


def main():
    dummyData = {1: {"accountID": 11, "accountNumber": 1100, "name": "yuvaraj", "balance": 10000, "password": "aa"},
                 2: {"accountID": 22, "accountNumber": 2200, "name": "pavithra", "balance": 20000, "password": "bb"}}
    for data in dummyData:
        i = dummyData[data]

        newCustomer = Customer(i["accountNumber"], i["password"], i["name"], i["balance"])
        customerDetails[i["accountID"]] = newCustomer

    while True:
        print("1.Login || 2.Purchase || 0. EXIT")
        choice = input("Enter you choice : ")
        if int(choice) == 1:
            login()
        elif int(choice) == 2:
            purchasePage()
        elif int(choice) == 0:
            print("EXIT")
            break
        else:
            print("Enter a valid input ")


main()
