import random
sum=0
print("Welcome to the game")
en=input("Do you want to start the game(y|n)")
if en.lower()=='y':
    print("Do you want to roll the dise(y|n):")
    roll_choice=input()
    if roll_choice.lower()=='y':
        while True:
            dise=random.randint(1,6)
            sum=sum+dise
            if dise==1:
                sum=0
                print("You Rolled '1'\nGame Over")
                break
            if sum==50:
                print("You won")
                break
            print("You Rolled:",dise)
            print("Your score:",sum)
            user_choice=input("Do you want to continue the game(y|n):")
            if user_choice.lower()=='n':
                break
print("Your total score:",sum)