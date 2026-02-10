class BankAccount:
    ROI = 10.5   # Class variable (Rate of Interest)

    def __init__(self, name, amount):
        self.Name = name        # Account holder name
        self.Amount = amount    # Account balance

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        depositAmount = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + depositAmount
        print("Amount deposited successfully")

    def Withdraw(self):
        withdrawAmount = float(input("Enter amount to withdraw: "))
        if withdrawAmount <= self.Amount:
            self.Amount = self.Amount - withdrawAmount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


# Creating multiple objects
acc1 = BankAccount("Dipak", 10000)
acc2 = BankAccount("Rahul", 20000)

# Using first account
acc1.Display()
acc1.Deposit()
acc1.Withdraw()
print("Interest:", acc1.CalculateInterest())
print("--------------------------")

# Using second account
acc2.Display()
acc2.Deposit()
acc2.Withdraw()
print("Interest:", acc2.CalculateInterest())
