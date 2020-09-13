#tax of businessmen , empolyee , person 

class person:
  def __init__(self, id_number):
    self.id_number= id_number
  def pay_tax(self , taxable_income , rate):
    tax = taxable_income*rate
    print("the tax is : " +str(tax))
    return tax

class business(person):
  def pay_tax(self , taxable_income , business_allowance, tax_rate):
    tax= (taxable_income - business_allowance)*tax_rate
    print("the tax is : " +str(tax))
    return tax

class empolyee(person):
  def refund_tax(self, amount):
    print("the refund is : " +str(amount))
    return amount

boss = business('90987')
boss.pay_tax(60000,8000,0.3)

boy = person('8765')
boy.pay_tax(30000, 0.25)

worker = empolyee("9788975")
worker.pay_tax(40000,0.2)
worker.refund_tax(2000)