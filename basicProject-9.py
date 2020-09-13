# random password generator 
import random

def get_char(list, num):
  character=[]
  for i in range(num):
    character.append(random.choice(list))
  return character
while True:
  num_char= int(input("Total number of int in password : "))
  num_Upper=int(input("number of uppercharacter in password : "))
  num_lower=int(input("number of lower character in password : "))
  num_digits=int(input("number of digits in password : "))
  num_symbol=int(input("number of symbols in password : "))

  if num_char < num_digits + num_lower + num_symbol + num_Upper:
    print (" Character number does not match ")
  else :
    break

upper_list=[chr(i) for i in range(65 , 91)]
upper_char=get_char(upper_list,num_Upper)
lower_list=[chr(i) for i in range(97, 97+26)]
lower_char=get_char(lower_list,num_lower)
digits_list=[str(i) for i in range(0,10)]
digits_char=get_char(digits_list,num_digits)
symbol_list=[chr(i) for i in range(32,48)]
symbol_list=[chr(i) for i in range(58,65)]
symbol_list=[chr(i) for i in range(91,97)]
symbol_list=[chr(i) for i in range(123,127)]
symbol_char=get_char(symbol_list,num_symbol)

whole_list= upper_list+lower_list+digits_list+symbol_list

miss_num = num_char-(num_digits+num_lower+num_symbol+num_Upper)

miss_char = get_char(whole_list, miss_num)

password= upper_char + lower_char + digits_char + symbol_char + miss_char

random.shuffle(password)
password = ''.join(password)
print(password)