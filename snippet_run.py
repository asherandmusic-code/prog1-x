def calc(x,f,y,ab):
    if f == 1:
        z = x + y
        a = f"{x} + {y} = {z}"

    elif f == 2:
        z = x - y
        a = f"{x} - {y} = {z}"

    elif f == 3:
        z = x * y
        a = f"{x} * {y} = {z}"

    elif f == 4:
        z = x / y
        a = f"{x} / {y} = {z}"

    if ab == 1:
        return z

    elif ab == 2:
        return a

    elif ab == 3:
        print(a)

x1 = int(input("Enter num 1:"))
f1 = int(input("(+:1) , (-:2) , (*:3) , (/:4):"))
y1 = int(input("Enter num 2:"))

calc(x1,f1,y1,3)

'''
List of  Ideas:
Calculator
Calculator history
Calculator history clear
Command line  clear
Command line
time
uptime
Coin toss
Dice roll
Typing  test
Guess the number
Timer
pyrun
'''





    
