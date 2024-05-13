import bankDatabase
from bankDatabase import giftCardDatabase, transactionHistory, updateTopUpTransaction


class Customer:


    def __init__(self, accountNumber, password, name, balance):
        self.accountNumber = accountNumber
        self.password = password
        self.name = name
        self.balance = balance
        self.accountID = str(accountNumber)[:2]
        self.giftCards = {}
        print(f'Account ID : {self.accountID} for {self.name} has been created')

    def authenticateGiftcards(self):
        for card in self.giftCards:
            giftCardDatabase[card] = {}
            giftCardDatabase[card] = self.giftCards[card]

    def createNewGiftCard(self):
        giftCardNumber = int(input("Enter 5 digit for your giftcard number : "))
        pinNumber = int(input("Enter 4 digit PIN number : "))
        self.giftCards[giftCardNumber] = {}
        self.giftCards[giftCardNumber]["pinNumber"] = pinNumber
        self.giftCards[giftCardNumber]["status"] = True
        giftCardBalance = self.TopUpGiftCard(giftCardNumber)
        self.giftCards[giftCardNumber]["giftCardBalance"] = giftCardBalance
        self.giftCards[giftCardNumber]["redeemPoints"] = 0
        self.authenticateGiftcards()

        print(self.giftCards)

    def TopUpGiftCard(self, giftCardNumber):
        if giftCardNumber not in self.giftCards:
            for c in self.giftCards:
                print(c, end=" ")
            print()
            giftCardNumber = int(input("Enter the valid gift card number : "))
        amount = int(input("Enter the amount to topUp : "))
        while amount > self.balance:
            print("Insufficient balance")
            amount = int(input("Enter the amount to topUp : "))
        self.balance -= amount
        print("Top up successful")
        self.authenticateGiftcards()
        updateTopUpTransaction(giftCardNumber, amount, True)
        return amount

    def activateGiftCard(self):
        cardNumber = int(input("Enter the card number : "))
        status = input("Enter 1 to block or 0 to unblock : ")
        if cardNumber not in self.giftCards:
            print("Incorrect card details")
            return
        if int(status) == 1:
            self.giftCards[cardNumber]["status"] = False
            print(f"CARD NUMBER : {cardNumber} HAS BEEN BLOCKED SUCCESSFULLY")
        else:
            self.giftCards[cardNumber]["status"] = True
            print(f"CARD NUMBER : {cardNumber} HAS BEEN UN-BLOCKED SUCCESSFULLY")
        self.authenticateGiftcards()
        print(giftCardDatabase)
        print()
        return

    def getGiftCardTransaction(self):
        for card in self.giftCards:
            if card in transactionHistory:
                res = transactionHistory[card]
                for data in res:
                    print(data)


