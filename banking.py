

org = 10000
dep=0
amount = int(org + dep)
base=5000


def info(self):
    name = input('Enter your name: ')
    print(name)
    Account = int(input('Enter your account no.: '))
    print(Account)
    pin = int(input('Enter the pin: '))
    print(pin)

info('info')

class Invalid_Account(Exception):
    pass


class Bank():

    def deposit(self):
        global dep
        global amount
        a = 50000
        try:
            dep = int(input('Enter the deposit Amount'))
            print(dep)
            amount=int(org+dep)
            print(f'Total amount is : {amount}')

            if (dep > a):
                raise Invalid_Account
            else:
                print(f'The amount entered is {dep}')
        except Invalid_Account:
            print("Exception occurred: Invalid input")


    def withdraw(self):
        global amount
        global base
        try:
            draw = int(input('Enter the withdraw Amount'))
            print(draw)
            left=int(amount)-int(draw)

            if left in range(0,base):
                raise Invalid_Account
            else:
                print(f'The amount entered is {draw}')
                print(f'Available balance : {left}')
        except Invalid_Account:
            print("Exception occurred: Invalid input")

person1=Bank()
person1.deposit()
person1.withdraw()






