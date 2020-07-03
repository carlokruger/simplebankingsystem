# Write your code here
import random

def mainmenu():
    print("1. Create and account")
    print("2. Log into account")
    print("0. Exit")


iin = "400000"
account = ""
pin = ""
cards = {}

while True:
    mainmenu()
    action = input()

    if action == "1":
        for i in range(9):
            account += str(random.randint(0, 9))
        checksum = str(random.randint(0, 9))
        card_number = iin + account + checksum

        for j in range(4):
            pin += str(random.randint(0, 9))

        cards.update({card_number: pin})

        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN")
        print(pin)
        print()

    elif action == "2":
        print("Enter your card number:")
        card_in = input()
        print("Enter your PIN:")
        pin_in = input()

        if card_in in cards:
            if cards[card_in] == pin_in:
                print("You have successfully logged in!")
            else:
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")


    elif action == "0":
        break
