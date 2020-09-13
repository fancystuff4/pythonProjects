#rock paper ans scissor game
import random

wins=0
losses=0
draws=0

while True:
  user_choice=input("select rock(R) or paper(P) or sicssor(S) ,  if you want to quit(Q) : ")
  if user_choice == "q":
    break
  else:
    computer_choice= random.choice(['r','p','s'])
    print("computer selects "+str(computer_choice))
    if computer_choice == user_choice:
     print("draw!")
     draws+=1
    elif (computer_choice == "r" and user_choice == "p") or \
       (computer_choice == "p" and user_choice == "s") or \
       (computer_choice == "s" and user_choice == "r"):
       print("you win!")
       wins+=1
    else:
     print("you loss")
     losses+=1
    
print( " you have won " +str(wins)+ " , loss "+str(losses)+  "  and draws "+str(draws) )