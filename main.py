import random
options={"s":1,"w":-1,"g":0}
a_option={1:"Snake",-1:'Water',0:"Gun"}
yourChoice=input("Enter your choice:")
computer=random.choice([0, 1, -1])
you=options[yourChoice]

print(f"You choose {a_option[you]} Computer choose {a_option[computer]}")

if(computer==you):
    print("It's a tie!")

else:
    if(computer==1 and you==-1):
        print('You Lost')
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print('You Lost')
    elif(computer==0 and you==1):
        print("You Lost")
    elif(computer==0 and you==-1):
        print("You Win!")
