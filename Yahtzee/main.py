import random
keep=True
while keep:
    dice=[0,0,0,0,0]
    for x in range(5):
        dice[x]=random.randint(1,6)
    print("you have:",dice)
    dice.sort()
    if dice[0]==dice[4]:
        print("5 in a row")
    elif dice[0]==dice[3] or dice[1]==dice[4]:
        print(" not bad 4 in a row")
    elif dice[0]==dice[2] or dice [2]==dice[4] or dice [1]==dice[3]:
        print("You have 3 in a row")
    else:
        print("sorry you dont win,try again")
    keep=(input("Press enter to continue or press any other key to exit")=="")
