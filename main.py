import random
print("Welcome to the game")
en=input("Do you want to start the game(y|n)")
player_no=1
if en.lower()=='y':
    print("Enter number of Players(0-4):")
    num_players=int(input())
    players_score=[0 for _ in range(num_players)]
    if 0<num_players<=4:
        while player_no<=4:
            print("player number:",player_no)
            print("Do you want to roll the dise(y|n):")
            roll_choice=input()
            if roll_choice.lower()=='y':
                while True:
                    dise=random.randint(1,6)
                    players_score[player_no-1]=players_score[player_no-1]+dise
                    if dise==1:
                        players_score[player_no-1]=0
                        print("You Rolled '1'\nGame Over")
                        break
                    if players_score[player_no-1]==50:
                        print("You won")
                        break
                    print("You Rolled:",dise)
                    print("Your score:",players_score[player_no-1])
                    user_choice=input("Do you want to continue the game(y|n):")
                    if user_choice.lower()=='n':
                        break
            player_no+=1
    print(players_score)
    winner=max(players_score)
    winner_index=players_score.index(winner)
    winner_index+=1
    print("Winner is player:",winner_index)
    print("Winner's Score is:",winner)