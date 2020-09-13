# die game with user and compute
import random

start_place = 0
end_place = 40
user_place=0
computer_place = 0
quit_game = False
user_win = False
computer_win = False
counter = 0 

while not user_win and not computer_win:
  user_input= input('Press "D" to throw die or to quit press "Q" :  ')
  if user_input == 'q':
    quit_game = True
    break
  if user_input == 'd':
    user_move = random.randint(1,6)
    user_place += user_move
    counter = counter + 1
    print("you have to move " + str(user_move)+ " steps")
    print("this is your  " + str(counter) + " time")
    if user_place > end_place:
      extra_steps = user_place-end_place
      user_place = end_place - extra_steps
    print("Now your are at position " + str(user_place))
    if user_place == end_place:
      user_win = True
      break
  
  computer_move = random.randint(1,6)
  computer_place += computer_move
  print("computer have to move " + str(computer_move)+ " steps")
  if computer_place > end_place :
    extra_steps = computer_place-end_place
    computer_place = end_place - extra_steps
  print("computer position is at " + str(computer_place))  
  if computer_place == end_place: 
      computer_win = True
      break

if user_win:
  print("you win")
if computer_win:
  print("computer win")
if quit_game:
  print ( " you need " + str(end_place-user_place) + " steps to win the game ")