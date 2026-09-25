#var-init
calc_history = []
#var-init

#support-functions
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
#support-functions

#main-function
def calculator(ms=None):
    
    if ms == None:
        mc = int(input("\nMemStore(1) or Standard(0):"))

        if mc == 1:
            calc.mem()

        elif mc == 0:
            calc.stand()

    elif ms == "mem":
        calc.mem()

    elif ms == "sta":
        calc.stand()

    print("\nAll calculations:")
    for i in calc_history:
        print(i,"\n")

def calc_hist():
    print("\nAll calculations:")
    for i in calc_history:
        print(i,"\n")
#main-function

#call-dictionary
plug = {
    "desc": '''calc           - opens calculator
    /mem       - MemStore
    /sta       - Standard
    /history   - output calculator history''',

    "comms": {
        "calc": calculator,
        "calc/mem": lambda: calculator(ms="mem"),
        "calc/sta": lambda: calculator(ms="sta"),
        "calc/history": calc_hist
    }
}
#call-dictionary
