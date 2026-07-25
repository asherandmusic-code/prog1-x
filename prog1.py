#Program 1

#-----import-libs-----

from datetime import datetime
import comms

#-----import-libs-----

#-----Variable-Initialisation-----

log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
i = True

#-----Variable-Initialisation-----

#-----Log-In-----
mt = input(":")
user = str(input("User ID:"))
password = str(input("Password:"))
#-----Log-In-----


if mt == "" and user == "MoonBeatsxo" and password == "314159" :

    print(f"Welcome {User}")

    def c():
        commands = {
            "help" : "help"
                    }

        while i == True:
            c = str(input("c/"))

            if c in commands:
                comms.commands[c]()
                    
    fxc = str(input("File(f) or Command line(c):"))

    if fxc == "f":
        print("In progress - redirect to Command line")
                          
        
    
