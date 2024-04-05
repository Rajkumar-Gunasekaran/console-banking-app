import random

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Bank:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

class Admin:
    def run(self, bank):
        print("Admin functionalities here")

        def check_bank_details():
            print("Bank has {} users".format(len(bank.users)))

        def check_customer_details(username):
            for user in bank.users:
                if user.username == username and user.role == 'customer':
                    print("Customer username: {}".format(user.username))
                    return
            print("Customer not found")

        def change_customer_amount(username, amount):
            for user in bank.users:
                if user.username == username and user.role == 'customer':
                    user.amount = amount
                    print("Changed amount for customer {}".format(user.username))
                    return
            print("Customer not found")

        while True:
            print("1. Check bank details")
            print("2. Check customer details")
            print("3. Change customer amount")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                check_bank_details()
            elif choice == '2':
                username = input("Enter customer username: ")
                check_customer_details(username)
            elif choice == '3':
                username = input("Enter customer username: ")
                amount = int(input("Enter new amount: "))
                change_customer_amount(username, amount)
            elif choice == '4':
                print("Exiting admin functionalities...")
                break
            else:
                print("Invalid choice!")

class Customer:
    def __init__(self):
        self.balance = 0  # Initialize balance for the customer

    def run(self, bank):
        print("Customer functionalities here")

        def deposit_amount(amount):
            self.balance += amount
            print("Deposited amount: {}. New balance: {}".format(amount, self.balance))

        def withdraw_amount(amount):
            if amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                print("Withdrew amount: {}. New balance: {}".format(amount, self.balance))

        def check_balance():
            print("Current balance: {}".format(self.balance))

        def generate_pin():
            self.pin = random.randint(1000, 9999)
            print("New pin generated: {}".format(self.pin))

        def change_pin(new_pin):
            self.pin = new_pin
            print("Pin changed successfully!")

        def transfer_amount(receiver, amount):
            if amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                receiver.balance += amount
                print("Transferred amount: {}. New balance: {}".format(amount, self.balance))

        while True:
            print("1. Deposit amount")
            print("2. Withdraw amount")
            print("3. Check balance")
            print("4. Generate pin")
            print("5. Change pin")
            print("6. Transfer amount")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                amount = int(input("Enter amount to deposit: "))
                deposit_amount(amount)
            elif choice == '2':
                amount = int(input("Enter amount to withdraw: "))
                withdraw_amount(amount)
            elif choice == '3':
                check_balance()
            elif choice == '4':
                generate_pin()
            elif choice == '5':
                new_pin = int(input("Enter new pin: "))
                change_pin(new_pin)
            elif choice == '6':
                receiver_username = input("Enter receiver's username: ")
                amount = int(input("Enter amount to transfer: "))
                receiver = bank.authenticate_user(receiver_username, "")
                if receiver is not None:
                    transfer_amount(receiver, amount)
                else:
                    print("Receiver not found!")
            elif choice == '7':
                print("Exiting customer functionalities...")
                break
            else:
                print("Invalid choice!")

class BankUser:
    def run(self, bank):
        print("Bank functionalities here")

        def change_user_amount(username, amount):
            for user in bank.users:
                if user.username == username:
                    if hasattr(user, 'balance'):
                        user.balance += amount
                        print("Changed amount for user {}. New balance: {}".format(username, user.balance))
                    else:
                        print("User {} is not a customer and does not have a balance.".format(username))
                    return
            print("User not found")

        def fetch_customer_details(username):
            for user in bank.users:
                if user.username == username and user.role == 'customer':
                    print("Username: {}, Balance: {}, Role: {}".format(user.username, user.balance, user.role))
                    return
            print("Customer not found")

        while True:
            print("1. Change user amount")
            print("2. Fetch customer details")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                username = input("Enter username: ")
                amount = float(input("Enter amount to change: "))
                change_user_amount(username, amount)
            elif choice == '2':
                username = input("Enter username: ")
                fetch_customer_details(username)
            elif choice == '3':
                break

class ATM:
    def __init__(self, bank):
        self.bank = bank

    def run(self):
        while True:
            print("1. Login")
            print("2. Add User")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = self.bank.authenticate_user(username, password)
                if user is not None:
                    if user.role == 'admin':
                        print("Welcome Admin!")
                        admin = Admin()
                        admin.run(self.bank)
                    elif user.role == 'customer':
                        print("Welcome Customer!")
                        customer = Customer()
                        customer.run(self.bank)
                    elif user.role == 'bank':
                        print("Welcome Bank!")
                        bank_user = BankUser()
                        bank_user.run(self.bank)
                    else:
                        print("Invalid role!")
                else:
                    print("Invalid username or password!")
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role: ")
                self.bank.add_user(User(username, password, role))
                print("User added successfully!")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    bank = Bank()
    bank.add_user(User('admin', 'admin123', 'admin'))
    bank.add_user(User('customer', 'customer123', 'customer'))
    bank.add_user(User('bank', 'bank123', 'bank'))
    atm = ATM(bank)
    atm.run()
