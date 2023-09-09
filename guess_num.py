import random
cont="Y"
tot_score=0
while cont=="Y":
    g_num=random.randint(1,20)
    attempts=8
    score=1000
    while attempts>0:
        num=int(input("Guess the number between 1 to 20 :"))
        if g_num==num:
            print("Guess was right")
            tot_score+=score
            break
        elif num>g_num:
            print("Guess was high")
            score-=100
        elif num<g_num:
            print("Guess was low")
            score-=100
        else:
            print("Error!!")
            break
        attempts-=1
        if attempts==0:
            print("The number was :",g_num)

    print("Score of this round :",score)
    cont=input("Do you want to continue(Y/N):").upper()
print("Total score:",tot_score)





