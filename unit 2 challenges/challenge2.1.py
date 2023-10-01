#CHALLENGE 2.1

class BankAcc:
  def __init__(self,account_number,account_holder_name,intial_bal:0.0):
      self.account_number=account_number
      self.account_holder_name=account_holder_name
      self.account_balance=intial_bal

  def deposit(self,amount):
    if amount>0:
      self.account_balance+=amount
      print("Deposited rs {} \nNew balance : rs {}".format(amount,self.account_balance))
    else:
      print("invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self,amount):
    if amount>0 and amount <= self.account_balance:
      self.account_balance-= amount
      print("withdraw rs {} \nNew balance: rs {}".format(amount,self.account_balance))
    else:
      print("Invalid Withdrawal amount or insufficient balance")


  def display(self):
    print("account balance for {} (account #{}): rs {}".format(self.account_holder_name,self.account_number,self.account_balance))



#creating instance of class

account=BankAcc(account_number="123456789", account_holder_name="jayashri",intial_bal=50000.0)

#test deposit and withdrawal functionlity
account.display()
account.deposit(5000.0)
account.withdraw(10000.0)
account.display()