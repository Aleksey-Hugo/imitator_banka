from random import randint
import sqlite3
db = sqlite3.connect("card.s3db")
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS card (id INT, number TEXT, pin TEXT, balance INT)''')
db.commit()
 
 
 
class BanckAccount:
    def __init__(self):
        self.accounts = {}
 
    def registr(self):
        iin = "400000"
        card_number_account = str(randint(0, 999999999)).rjust(9, '0')
        checksum = self.luhn_algoritm(iin + card_number_account)
        card = iin + card_number_account + str(checksum)
        pin = str(randint(0, 9999)).rjust(4, '0')
        print(f'\nYour card has been created\n'
              f'Your card number is:\n{card}\n'
              f'Your card PIN:\n{pin}\n')
        self.save_account_info(card, pin)
        if sql.fetchone() is None:
            sql.execute("INSERT INTO card VALUES(?, ?, ?, ?)", (int(card_number_account), card, pin, 0))
            db.commit()
        else:
            print("We have this commit")
    def luhn_algoritm(self, card_number_account):
        total = 0
        count = 0
        y = 0
        checksum = 0
        for digit in card_number_account:
            count += 1
            if count % 2 != 0:
                y = int(digit) * 2
                if y > 9:
                    y = y - 9
            else:
                y = int(digit)
 
            total += y
 
        checksum = total % 10
 
        if checksum > 0:
            checksum = 10 - checksum;
 
        return checksum
    def save_account_info(self, number, pin):
        self.accounts[number] = pin
 
    def log_in(self):
        number = input('Enter your card number:\n')
        pin_num = input('Enter your PIN:\n')
        dict_pin = self.accounts.get(number)
        i = 1
 
        if dict_pin != pin_num:
            print('Wrong card or PIN entered')
        else:
            print('You have successfully logged in!')
            while i > 0:
                choice = int(input('1. Balance\n'
                                   '2. Log out\n'
                                   '0. Exit\n'))
 
                if choice == 1:
                    self.account_details()
                elif choice == 2:
                    print('You have successfully logged out!\n')
                    i = 0
                else:
                    i = -1
 
        return i
    def account_details(self):
        print('Balance: 10000000$\n')
 
    def bank(self):
        i = 1
        while i > 0:
            print('1. Create an account')
            print('2. Log into account')
            print('0. Exit')
            choice = int(input())
            if choice == 1:
                self.registr()
            elif choice == 2:
                if self.log_in() < 0:
                    break
            else:
                break
 
my_account = BanckAccount()
my_account.bank()
