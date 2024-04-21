import jumble
from numpy import choose
import random
def choose():
    words=["hello","rainbow","hell","world","heaven","man", "rail" ]
    return random.choice(words)
def jumbled(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def play():
    p1 = input("Enter your name: ")
    p2= input("Enter your name: ")
    pp1=0
    pp2=0
    turn=0
    while True:
        #Computer's task
        picked_words=choose()
        jn=jumbled(picked_words)
        print(jn)
        #player1
        if turn%2==0:
            print(p1," your turn. ")
            ans=input("Enter the answer")
            if ans==picked_words:
                pp1+=1
                print("your score is ",pp1)
            else:
                ("failed:",pp1)
            c=input("Do you want to continue, if yes then 1 else 0 ")
            if c==0:
                break



                #player 2
        else:
            print(p2," your turn. ")
            ans=input("Enter the answer")
            if ans==picked_words:
                pp2+=1
                print("your score is ",pp2)
            else:
                ("failed:",pp2)
            c=input("Do you want to continue, if yes then 1 else 0 ")
            if c==0:
                break
                #player 2
        turn=turn+1


play()