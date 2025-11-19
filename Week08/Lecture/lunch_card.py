class LunchCard:
    def __init__(self, init_balance, name, id):
        self.balance = init_balance
        self.name = name
        self.id = id
    
    def payLunch(self, bill_amount):
        if isinstance(bill_amount, int) or isinstance(bill_amount, float):
            if self.balance >= bill_amount:
                self.balance -= bill_amount
                print("Payment was successful for", self.id, self.name)
            else:
                print("Insufficent funds")
        else:
            print("Bill amount must be numerical value!")
    
    def displayCurrentBalance(self):
        print("Current balance for student", self.id, self.name, "is", self.balance)

    def depositMoney(self, newMoney):
        if isinstance(newMoney, int) or isinstance(newMoney, float):
            if newMoney <= 1000:
                self.balance += newMoney
            else:
                print("We do not allow to deposit money more than 1000")
        else:
            print("Parameter should be numerical")