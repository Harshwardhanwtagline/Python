class BankAccount:
    def __init__(self, acc_name, acc_number, balance, pin):
        self.acc_name = acc_name
        self.acc_number=acc_number
        self.balance=balance
        self.pin=pin
    
    def check_pin(self, pin):
        if self.pin == pin:
            return "Account Holder Name: {}\nAccount Number: {}\nTotal Balance: {}".format(self.acc_name, self.acc_number, self.balance)
        else:
            return "Please Enter Correct Pin"
    
    def deposit(self, pin, amount):
        if (self.pin == pin):
            self.balance += amount
            return "{} rupees are successfully added to your account.".format(amount)
        return "Please Enter Correct Pin"

    def withdraw(self, pin, amount):
        if (self.pin == pin):
            if self.balance > amount:
                self.balance -= amount
                return "Here {} has {} rupees in his bank and he trying to withdraw {}.".format(self.acc_name, self.balance, amount)
            return "Your account don't have sufficient balance"
        return "Please Enter Correct Pin"
    
    def __str__(self) -> str:
        return "Account Holder Name: {}\nAccount Number: {}\nTotal Balance: {}".format(self.acc_name, self.acc_number, self.balance)

        



if __name__ == "__main__":
    b1 = BankAccount(acc_name="Ram",acc_number= 12345, balance=1000, pin=3456)

    print(b1.check_pin(3456))
    print(b1.deposit(3456, 1000))
    print(b1.withdraw(3456, 1200))
    print(b1)