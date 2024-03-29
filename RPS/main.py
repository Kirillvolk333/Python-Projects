import random
print("welcome to the game of rock paper scissors")
print("You have 3 rounds")
print("K=rock, N=scissors, B=paper")
igrok_score=0
igrok_choice=0
bot_score=0
bot_choice=0
print("-----Beginning of the game-----")
for i in range(3):
    print("---ROUND"+str(i+1)+ "---")
    bot_choice=random.choice(['K', 'N', 'B'])
    igrok_choice=input("Your choice:").upper()
    print("Your choice:"+igrok_choice+" VS Bot's choice:"+bot_choice)
    if igrok_choice==bot_choice:
        print("draw")
    elif igrok_choice=="K":
        if bot_choice=="N":
            igrok_score=igrok_score+1
            print("you won this round")
        else:
            bot_score=bot_score+1
            print("the bot won this round")
    elif igrok_choice=="N":
        if bot_choice=="B":
            igrok_score = igrok_score + 1
            print("you won this round")
        else:
            bot_score=bot_score+1
            print("the bot won this round")
    elif igrok_choice=="B":
        if bot_choice=="K":
            igrok_score = igrok_score + 1
            print("you won this round")
        else:
            bot_score=bot_score+1
            print("the bot won this round")
if igrok_score==bot_score:
    print("DRAW :", igrok_score,":",bot_score)
elif igrok_score>bot_score:
   print("you won! VICTORY IS YOURS! :", igrok_score,":",bot_score)
elif igrok_score<bot_score:
   print("Bot's victory. You lose! \n", igrok_score,":",bot_score)
