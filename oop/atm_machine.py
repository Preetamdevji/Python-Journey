class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
            while True:
                user_input = input("""
                    How would you like to proceed:
                    1: Enter 1 to create pin
                    2: Enter 2 to deposit
                    3: Enter 3 to withdraw
                    4: Enter 4 to check balance
                    5: Enter 5 to exit
                    """) 
        
                if user_input == '1':
                    self.create_pin()
                elif user_input == '2':
                    self.deposit()
                elif user_input == '3':
                    self.withdraw()
                elif user_input == '4':
                    self.check_balance()
                elif user_input == '5':
                        print("Goodbye!")
                        break
                else:
                    print("Invalid choice. Please enter a valid option.")

    def create_pin(self):
        self.pin = input("Enter your new pin: ")
        print("Pin Set Successfully")

    def deposit(self):
        temp = input("Enter your pin for deposit: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin for withdraw: ")
        if temp == self.pin:
            amount = int(input("Enter the withdraw amount: "))
            if amount <= self.balance:
                self.balance -= amount  
                print("Withdrawal Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin") 

    def check_balance(self):
        temp = input("Enter the pin for checking balance: ")
        if temp == self.pin:
            print("Your balance: ", self.balance)
        else:
            print("Invalid Pin")

user = Atm()
