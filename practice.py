class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method 
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Rs.", amount, "was debited")
            print("total balance =", self.get_balance())


    #credit method 
    def credit (self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 123456789)
acc2 = Account(8000, 987654321)
acc1.debit(500)
acc2.credit(9000)