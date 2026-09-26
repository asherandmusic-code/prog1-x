#Program 1

#-----import-libs-----

from datetime import datetime
import comms

#-----import-libs-----

#-----Variable-Initialisation-----

log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#-----Variable-Initialisation-----

#-----Log-In-----
mt = input(":")
user = str(input("User ID:"))
password = str(input("Password:"))
#-----Log-In-----


if mt == "" and user == "SunxMoon" and password == "1945" :

    print(f"\nWelcome {user}")

    def c():
        commands = {
            "help" : comms.help,
            "calc" : comms.calculator,
            "calc/mem" : lambda : comms.calculator(ms="mem"),
            "calc/sta" : lambda : comms.calculator(ms="sta"),
            "calc/history":comms.calc_hist,
            "timer":comms.timer
                    }

        while True:
            cmd = str(input("c/"))

            if cmd in commands:
                commands[cmd]()
                
            elif cmd == "end":
                print("Thanks for using prog1")
                break

            elif cmd == "time":
                print("\n",datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"\n")

            elif cmd == "clear":
                print("\n"*25)
          
            elif cmd not in commands:
                print("\nCommand not available...Try again.\n") 
                    
    fxc = str(input("File(f) or Command line(c):"))

    if fxc == "f":
        print("\nIn progress - redirect to Command line\n")
        c()

    elif fxc == "c":
        c()
        
    
