import random
dice=(1,2,3,4,5,6,1)
player1=0
player2=0

def roll():
    score=random.choice(dice)
    print(f"\nDice roll gives :{score}")
    return score

print("1st to reach 50 wins.\nAll the best!\n")
while player1<50 and player2<50:
    print("\n\n\nPlayer 1's Turn\n")
    choice='y'
    p=0
    p1Score=0
    while choice != 'n' and p != 1 and p1Score<50:
        v=input("\npress any key to roll the dice : ")
        p=roll()
        if p==1:
            p1Score=0
            print(f"\nRound score reset to 0")
        else:
            p1Score+=p
            print(f"\nyour score in this round :{p1Score}") 
            choice=input("\nwhat to roll agin (y/n): ").lower()    
    player1 +=p1Score
    if player1>=50:
        print("\n\n\nPlayer1 wins!!")
        break

    print("\n\n\nPlayer 2's Turn\n")
    choice='y'
    p=0
    p2Score=0
    while choice != 'n' and p != 1 and p1Score<50 and p2Score<50:
        v=input("\npress any key to roll the dice : ")
        p=roll()
        if p==1:
            p2Score=0
            print(f"\nRound score reset to 0")
        else:
            p2Score+=p
            print(f"\nyour score in this round :{p2Score}")
            choice=input("\nwhat to roll again (y/n): ").lower()
    player2 +=p2Score
    print(f"\n\n\nPlayer 1's Total Score: {player1}")
    print(f"\nPlayer 2's Total Score: {player2}")

if player2>=50:
    print("\n\nPlayer2 wins!!") 