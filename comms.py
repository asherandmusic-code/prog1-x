from pathlib import Path
import winsound
import time

calc_history = []

#Pre-define
class calc():
    def func(x,f,y,ab):
        if f == 1:  #+
            z = x + y
            a = f"{x} + {y} = {z}"

        elif f == 2:  #-
            z = x - y
            a = f"{x} - {y} = {z}"

        elif f == 3:  #*
            z = x * y
            a = f"{x} * {y} = {z}"

        elif f == 4:  #/
            z = x / y
            a = f"{x} / {y} = {z}"

        if ab == 1:#value return
            return z

        elif ab == 2:#expression return
            return a

        elif ab == 3:#expression print
            print("\n",a,"\n")

    def mem():
        print("\nMemStore Calculator\n")
        i = True
        
        x = float(input("Enter num:"))
        
        while i == True:
            f = int(input("+(1), -(2), *(3), /(4):"))
            y = float(input("Enter num:"))
            
            calc_history.append(calc.func(x,f,y,2))
            calc.func(x,f,y,3)
            x = calc.func(x,f,y,1)

            cont = input("Continue:")
            if cont == "":
                continue
            elif cont == "x":
                break

    def stand():
        print("\nStandard Calculator")
        i = True
        
        while i == True:
            x = float(input("Enter num:"))
            f = int(input("+(1), -(2), *(3), /(4):"))
            y = float(input("Enter num:"))
            
            calc_history.append(calc.func(x,f,y,2))
            calc.func(x,f,y,3)

            cont = input("Continue:")
            if cont == "":
                continue
            elif cont == "x":
                break
            
#Pre-define

#Comms functions
        
def calculator(ms=None):
    if ms == None:
        mc = int(input("\nMemStore(1) or Standard(0):"))

    if ms == "mem" or mc == 1:
        calc.mem()

    elif ms == "sta" or mc == 0:
        calc.stand()

    calc_hist()

def calc_hist():
    print("\nAll calculations:")
    for i in calc_history:
        print(i,"\n")

def timer():
    SOUND = Path(__file__).parent / "t.wav"
    x = int(input("Enter seconds:"))
    time.sleep(x)

    winsound.PlaySound(
        str(SOUND),
        winsound.SND_FILENAME | winsound.SND_ASYNC
    )

    input("dismiss:")
    winsound.PlaySound(None, 0)

def help():
    print('''
Available commands:
help           - shows all available commands
end            - ends program
time           - shows current time
clear          - clears command line
calc           - opens calculator
    /mem       - MemStore
    /sta       - Standard
    /history   - output calculator history
timer          - simple tune-playing timer
''')

