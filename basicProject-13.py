#charity money

class charity:
  def __init__(self,balance=100000):
    self.balance= balance
  def save_fund(self,amount):
    self.balance+= amount
  def spend_funds(self,amount):
    self.balance-=amount
  def investment(self, investment_return):
    self.balance*=1+investment_return
  def get_balance(self):
    if self.balance< 0 :
      print("ypu got a deficit balance"+str(self.balance))
    return self.balance
  def is_danger(self):
    if self.balance< 50000 and self.balance>=1:
      print("you are in danger "+str(self.balance)+" balance left")
    return self.balance<50000

money= charity()
money.spend_funds(20000)
print(money.get_balance())
money.save_fund(10000)
print(money.get_balance())
money.investment(0.10)
print(money.get_balance())
money.investment(-0.10)
print(money.get_balance())
money.spend_funds(60000.10)
print(money.get_balance())
print(money.is_danger())