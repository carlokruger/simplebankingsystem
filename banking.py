# Write your code here
import random


def mainmenu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")


def cardmenu():
    print("1. Balance")
    print("2. Log out")
    print("0. Exit")

def generate_checksum(account):
    account_list = []
    checksum_sum = 0

    for x in account:
        account_list.append(int(x))

    for idx, el in enumerate(account_list):
        if (idx + 1) % 2 != 0:
            account_list[idx] = el * 2

    for idy, y in enumerate(account_list):
        if account_list[idy] > 9:
            account_list[idy] -= 9

    for z in account_list:
        checksum_sum += z

    return str(10 - ( checksum_sum % 10))


iin = "400000"
account = ""
pin = ""
cards = {}
loop = True

while loop:
    mainmenu()
    action = input()

    if action == "1":
        for i in range(9):
            account += str(random.randint(0, 9))
        checksum = generate_checksum(iin+account)
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
        account = ""
        checksum = ""
        card_number = ""
        pin = ""

    elif action == "2":
        print("Enter your card number:")
        card_in = input()
        print("Enter your PIN:")
        pin_in = input()

        if card_in in cards:
            if cards[card_in] == pin_in:
                print("You have successfully logged in!")
                print()
                while True:
                    cardmenu()
                    logged_in_action = input()

                    if logged_in_action == "1":
                        print("Balance: 0")
                        print()
                    elif logged_in_action == "2":
                        break
                    elif logged_in_action == "0":
                        loop = False
                        print()
                        print("Bye!")
                        break

            else:
                print("Wrong card number or PIN!")
        else:
            print("Wrong card number or PIN!")

    elif action == "0":
        print("Bye!")
        break
