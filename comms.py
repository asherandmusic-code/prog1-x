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
            print(a)

    def mem():
        print("MemStore Calculator")
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
        print("Standard Calculator")
        i = True
        
        while i == True:
            x = float(input("Enter num:"))
            f = int(input("+(1), -(2), *(3), /(4):"))
            y = float(input("Enter num:"))
            
            calc_history.append(calc.func(x,f,y,2))
            calc.func(x,f,y,3)
            
#Pre-define

#Comms functions
        
def calculator(ms=None):
    if ms == None:
        mc = int(input("MemStore(1) or Standard(0)"))

    elif ms == "mem":
        calc.mem()

    elif ms == "sta":
        calc.stand()
    
