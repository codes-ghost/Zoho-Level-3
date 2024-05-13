from collections import defaultdict

customerDetails = {}
giftCardDatabase = {}
transactionHistory = defaultdict(list)
# redeemPoint = {}


def updateTransaction(cardnumber, amountUsed):
    transactionHistory[cardnumber].append(f'{amountUsed} has been spent on card Number {cardnumber}')
    if amountUsed >= 100:
        point = amountUsed / 100
        giftCardDatabase[cardnumber]["redeemPoints"] += point
        ptsRedeemed = 0
        while giftCardDatabase[cardnumber]["redeemPoints"] >= 10:
            ptsRedeemed += 1
            giftCardDatabase[cardnumber]["redeemPoints"] -= 10
        giftCardDatabase[cardnumber]["giftCardBalance"] += ptsRedeemed
        print(f"Rs: {ptsRedeemed} has been added to the giftCard balance successfully")

    card = giftCardDatabase[cardnumber]


def updateTopUpTransaction(cardNumber, amountUsed, topup):
    transactionHistory[cardNumber].append(f'{amountUsed} has been used for top-up')
