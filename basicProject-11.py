# PRODUCT PRICE DISCOUNT
def get_price(product, quantity):
  subtotal = price_diction[product] * quantity
  return subtotal

buying_diction={"biscuits":2 , "chicken":3, "fruits":5}
price_diction={"biscuits":3 , "chicken":15.5, "fruits":10}

bill_price=0
membership = 'golden'

for key ,value in buying_diction.items():
   bill_price+=get_price(key,value)
print("Actual price is " +str(bill_price))

for key , value in buying_diction.items():
      print("product " +key+ " and quantity " +str(value)+ " , price is " + str(price_diction[key]*value))

print("But you get dicount")

if bill_price>50:
    if membership =='golden':
      bill_price=bill_price*0.75
      discount = 25
    elif membership =='silver':
      bill_price=bill_price*0.85
      discount = 15
    print('your member ships is '+membership+" and you got discount of " +str(discount)+ " % and your actual bill is " +str(bill_price))