#Number guess by computer game .

import random

play_game = 'y'
start = 1
end = 50 


while play_game == 'y':
  smallest = start
  largest = end
  print('select a number b\w 1-50 in your mind ')
  try_number = random.randint(start,end)
  print (try_number)
  counter = 0
  direction = "N"
  
  while direction != "c":
    direction = input("Is it too large(L) or too small(s) or correct(c) ")
    if direction == 's':
      if try_number > smallest:
        try_number = random.randint(try_number+1,largest)
      print(try_number)
    if direction == 'l':
      if try_number < largest:
        try_number = random.randint(smallest,try_number - 1)
      print(try_number)
  counter = counter + 1
  print( ' i got it ! , i tried ' + str(counter) + ' time . ')
  play_game= input('continue?')