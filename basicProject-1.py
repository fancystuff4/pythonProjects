# Number guessing game

import random

play_game = "y"

while( play_game == 'y'):
  answer = random.randint(1,50)
  try_number = int(input(' choose a number b/w 1-50 to win the game. '))
  counter = 1 

  while answer != try_number:
    if try_number > answer:
      print("guess number is large")
      print ('you have taken ' + str(counter)+ ' chances')
    if try_number < answer:
      print("guess number is small")
      print ('you have taken ' + str(counter)+ ' chances')
    try_number = int(input('wrong , guess it again  '))
    counter = counter + 1
  print ('you win , you have taken '+ str(counter)+' chances ')
  play_game = input('do you want to continue if yes then enter y , if not press N ')
