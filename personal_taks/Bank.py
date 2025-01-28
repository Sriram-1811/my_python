class Bank:
    def __init__(self,acc_number,acc_balance):
        self.acc_number=acc_number
        self.acc_balance=acc_balance

    def credit(self,amount):
        self.acc_balance+=amount
        print("INR",amount,"has been credited in your acount number",self.acc_number,"\nthe balance amount is:",self.acc_balance)

    def debit(self, amount):
        if amount <= self.acc_balance:
            self.acc_balance-=amount
            print('INR',amount,"has bee debited form your account number",self.acc_number,"\nthe balance amount is:",self.acc_balance)
        else:
            print("Payment failed!!! \nthe amount you were requesting to debit is more than the current balance")


a1=Bank(192207,50000)
print(a1.acc_balance)
a1.credit(10000)
a1.debit(100000)
a1.debit(1010)
print(a1.acc_balance)
