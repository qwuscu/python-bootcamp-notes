class Account:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'Account owner: {self.name}\nAccount balance: ${self.amount}'

    def deposit(self,deposit_amount):
        print("Deposit Accepted")
        self.amount += deposit_amount

    def withdraw(self,withdraw_amout):
        if self.amount < withdraw_amout:
            print("Funds Unavailable!")
        else:
            self.amount -= withdraw_amout
            print("Withdrawal Accepted")


acct1 = Account('Jose',100)
print(acct1)
acct1.deposit(50)
print(acct1.amount)
acct1.withdraw(200)


