     #Rock Paper Scissor Game
import random
l=["scissor","Rock","Paper"]
while True:
    computer_count=0
    user_count=0
    user_choice=int(input('''
Let start The Game.....
1 yes
2 NO | Exit
'''))
    if user_choice==1:
        for a in range(1,6):
            UserInput=int(input('''
            1 Rock
            2 Scissor
            3 Paper'''))
            if UserInput==1:
                user_choice="Rock"
            elif UserInput==2:
                user_choice="Scissor"
            elif UserInput==3:
                user_choice="Paper"
            computer_choice=random.choice(l)
            if computer_choice==user_choice:
                print("computer value:",computer_choice)
                print("user value:",user_choice)
                print("Game Draw")
                user_count=user_count+1
                computer_count=computer_count+1
            elif (user_choice=="Rock" and computer_count=="scissor" )or (user_choice=="Scissor" and computer_choice=="Paper") or (user_choice=="Paper" and computer_choice=="Rock"):
                print("computer value:", computer_choice)
                print("user value:", user_choice)
                print("You Win The Game")
                user_count = user_count + 1
            else:
                print("computer value:", computer_choice)
                print("user value:", user_choice)
                print("Computer Win The Game")
                computer_count = computer_count + 1
    else:
        break