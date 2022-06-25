
import random

comp_wins=0
player_wins=0

def Choose_Option():
    user_choice=input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock","rock","R","r"]:
        user_choice="r"
    elif user_choice in ["Paper","paper","p","P"]:
        user_choice="p"
    elif user_choice in ["Scissors","scissors","S","s"]:
        user_choice="s"
    else:
        print("I Don't Understand U !!!")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice ="r"
    elif comp_choice==2:
        comp_choice="p"
    else:
        comp_choice="s"
    return comp_choice


while True:
    print("")
    user_choice =Choose_Option()
    comp_choice=Computer_Option()
    print("")

    if user_choice=="r":
        if comp_choice=="r":
            print("You Chose Rock.  The Computer Chose Rock.  You Tied:)")

        elif comp_choice=="p":
            print("You Chose Rock.  The Computer Chose paper.  You Lose:(")
            comp_wins+=1

        else:
            print("You Chose Rock.  The Computer Chose Scissors.  You Win:):)")
            player_wins+=1

    
    elif user_choice=="p":
        if comp_choice=="r":
            print("You Chose Paper.  The Computer Chose Rock.  You Win:):)")
            player_wins+=1

        elif comp_choice=="p":
            print("You Chose Paper.  The Computer Chose paper.  You Tied:)")

        else:
            print("You Chose Paper.  The Computer Chose Scissors.  You Lose:(")
            comp_wins+=1


    if user_choice=="s":
        if comp_choice=="r":
            print("You Chose Scissors.  The Computer Chose Rock.  You Lose:(")
            comp_wins+=1

        elif comp_choice=="p":
            print("You Chose Scissors.  The Computer Chose paper.  You Win:):)")
            player_wins+=1
            
        else:
            print("You Chose Scissors.  The Computer Chose Scissors.You Tied:)")
    
    print("")
    print("Player Wins:"+str(player_wins))
    print("Computer Wins:"+str(comp_wins))
    print("")

    user_choice=input("Do you want to Play Again (y/n)")
    if user_choice in ["y","y","Yes","yes"]:
        pass
    elif user_choice in ["n","N","No","no"]:
        break
    else:
        break
