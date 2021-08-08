import random
user=None
options=["r","p","s"]
rounds=int(input(("Total points to win?:")))
user_score=0
computer_score=0
while(True ):
    user=input("press r for Rock,s for scissors and p for paper:").lower()
    if(user!='r' and user!='p' and user!='s'):
        print("Enter proper character")
        
    else:
        computer_choice=random.choice(options)
        print("Computer choice:",computer_choice)
        if(user=='r' and computer_choice=='p' or user=='p' and computer_choice=='s' or user=='s' and computer_choice=='r'):
            computer_score+=1
        elif(user=='p' and computer_choice=='r' or user=='s' and computer_choice=='p' or user=='r' and computer_choice=='s'):
            user_score+=1
        else:
            print("Its a tie")
        if(user_score==rounds or computer_score==rounds):
            print("Game over:")
            print("Your score:",user_score,end=" ")
            print("Computer score:",computer_score)
            if(user_score>computer_score):
                print("You Won")
            else:
                print("Computer Won, better luck next time mate")
                break
        else:
            print("Your score:",user_score,end=" ")
            print("Computer score:",computer_score)



